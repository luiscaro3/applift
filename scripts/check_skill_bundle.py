"""Check SKILL.md relative resources in a directory or Tessl .tgz, without extraction."""
import argparse
import posixpath
import re
import tarfile
from pathlib import Path
from urllib.parse import unquote, urlsplit


def check(source, review_scope=False):
    source = Path(source)
    if source.is_dir():
        skill = (source / "SKILL.md").read_text(encoding="utf-8")
        exists = lambda name: (source / name).is_file()
    else:
        with tarfile.open(source, "r:gz") as archive:
            files = {}
            for member in archive.getmembers():
                if not member.isfile():
                    continue
                name = member.name.removeprefix("./").removeprefix("package/")
                files[name] = member
            if "SKILL.md" not in files:
                raise ValueError("Archive has no root SKILL.md")
            skill = archive.extractfile(files["SKILL.md"]).read().decode("utf-8")
        exists = lambda name: name in files
    links = re.findall(r"\[[^\]]*\]\(([^)]+)\)", skill)
    missing = []
    checked = 0
    for link in links:
        target = urlsplit(link.strip("<>"))
        if target.scheme or target.netloc or not target.path:
            continue
        checked += 1
        name = posixpath.normpath(unquote(target.path))
        if name.startswith("../") or name.startswith("/") or not exists(name):
            missing.append(link)
        elif review_scope and name.split("/", 1)[0] not in {"references", "scripts", "assets"}:
            missing.append(link + " (outside Tessl review resource directories)")
        elif review_scope and len(name.split("/")) > 2:
            missing.append(link + " (deeper than one reference level)")
    return checked, missing


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", help="Skill directory or packed .tgz")
    parser.add_argument("--review-scope", action="store_true",
                        help="Require links to survive Tessl 0.117.0 review resource collection")
    args = parser.parse_args()
    checked, missing = check(args.source, args.review_scope)
    if missing:
        raise SystemExit(f"{len(missing)}/{checked} relative links unavailable: " + ", ".join(missing))
    print(f"Verified all {checked} SKILL.md relative link targets in {args.source}")
