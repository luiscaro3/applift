"""Stage AppLift's existing docs in the resource directories Tessl reviews collect."""
import argparse
import json
import posixpath
import re
import shutil
from pathlib import Path
from urllib.parse import unquote, urlsplit


def stage(source, destination):
    source, destination = Path(source).resolve(), Path(destination).resolve()
    if destination == source or source in destination.parents:
        raise ValueError("Stage outside the source tree so generated copies cannot enter source packages")
    if destination.exists():
        raise ValueError("Destination already exists; choose a fresh staging directory")
    resources = [Path("BRIDGE-PLAN.md"), Path("MODELS.md")]
    resources += sorted(Path("specs") / p.name for p in (source / "specs").glob("*.md"))
    resources += sorted(Path("examples") / p.name for p in (source / "examples").glob("*.md"))
    for path in [Path("SKILL.md"), Path("LICENSE"), Path(".tessl-plugin/plugin.json"), *resources]:
        if not (source / path).is_file():
            raise ValueError(f"Required source resource missing: {path}")

    names = [path.name.casefold() for path in resources]
    if len(names) != len(set(names)):
        raise ValueError("Reference basenames collide; assign unique names before flattening")
    targets = {path.as_posix(): path.name for path in resources}

    def rewrite_links(text, current):
        def resource_link(match):
            target = match.group(1)
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                return match.group(0)
            resolved = posixpath.normpath(posixpath.join(
                posixpath.dirname(current), unquote(parsed.path)))
            if resolved not in targets:
                raise ValueError(f"{current} link has no staged resource: {target}")
            path = targets[resolved]
            if current == "SKILL.md":
                path = "references/" + path
            mapped = parsed._replace(path=path).geturl()
            return match.group(0).replace(f"({target})", f"({mapped})")
        return re.sub(r"\[[^\]]*\]\(([^)]+)\)", resource_link, text)

    skill = rewrite_links((source / "SKILL.md").read_text(encoding="utf-8"), "SKILL.md")
    documents = {path.name: rewrite_links((source / path).read_text(encoding="utf-8"),
                                          path.as_posix()) for path in resources}
    destination.mkdir(parents=True)
    (destination / "SKILL.md").write_text(skill, encoding="utf-8", newline="\n")
    shutil.copyfile(source / "LICENSE", destination / "LICENSE")
    for name, text in documents.items():
        target = destination / "references" / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8", newline="\n")
    manifest = json.loads((source / ".tessl-plugin/plugin.json").read_text(encoding="utf-8"))
    manifest["skills"] = ["."]
    (destination / ".tessl-plugin").mkdir()
    (destination / ".tessl-plugin/plugin.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Staged SKILL.md and {len(resources)} reference documents with flattened links at {destination}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", help="Fresh output directory outside the source tree")
    args = parser.parse_args()
    stage(Path(__file__).resolve().parents[1], args.destination)
