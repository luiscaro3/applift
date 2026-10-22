# AppLift

<img src="assets/applift-logo.png" alt="AppLift" width="720">

**LLM-first integration specs for adding authentication, multi-user access, subscriptions and admin dashboards to existing apps.**

**Keep your existing app and chosen providers.** AppLift supplies logical models and short design contracts for connecting new capabilities to existing users, data and workflows. Stripe explains how to create a subscription; AppLift helps map it to the customer and the operations paid access should unlock. Use it alongside official provider documentation when that host mapping is unresolved; skip it when the provider's short recipe already solves the task.

**Lifecycle focus: MVP to an early operating startup.** Comprehensive observability platforms, disaster-recovery programs and enterprise governance are outside default scope. Authorization, customer isolation, data preservation and ordinary workflow recovery still matter. Additional operational needs depend on the actual host; adopting AppLift does not certify whole-product readiness.

Draft 0.2. Instruction-only specs and an optional agent skill; no runtime dependency, required database or generated code.

The logical models are designed to map onto existing relational or document databases using their native mechanisms. SQLite and Firestore below identify trial environments, not required technologies; those trials do not establish compatibility with every database.

## Start here

Read the relevant spec from the table below, or install the skill from your consuming project with the optional [Skills CLI](https://skills.sh/docs/cli):

```sh
npx skills add luiscaro3/applift --skill applift-specs --agent codex
```

Replace `codex` with your supported agent, such as `claude-code`. Preview with `npx skills add luiscaro3/applift --list`. The CLI is an installation tool, not an AppLift runtime dependency.

Explicitly request `$applift-specs` or ask the agent to read [SKILL.md](SKILL.md). Automatic selection depends on the host and task; installation does not guarantee it. Direct reading works without installation.

## Choose your transition

| User outcome | Read |
| --- | --- |
| Add Google/provider sign-in and session recovery | [Identity and session recovery](specs/identity.md) |
| Add private users or shared teams / multi-tenant ownership | [Ownership and sharing](specs/ownership.md) |
| Let each customer connect their own mailbox or service | [Connections and reconnection](specs/connections.md) |
| Keep imports, workers and search private; preserve completed work on replay | [Background work and business progress](specs/background-work.md) |
| Charge subscriptions and enforce paid features | [Subscriptions and access](specs/subscriptions.md) |
| Connect an admin template or dashboard to the database | [Management mapping](specs/management.md) |

Use one contract if that is enough; skip solved decisions. AppLift describes relationships, authority and workflow guarantees. The agent chooses implementation from the actual app. No whole-kit adoption or general redesign is required; personal data does not need workspaces by default.

## One small bridge

Illustrative request: "Let other customers connect their own mailbox. Keep their work private and don't reset fulfilled requisitions."

Suppose the app already links requisitions to campaigns and campaigns to customers, but uses one shared mailbox:

| Existing app | Design decision supplied by AppLift |
| --- | --- |
| `requisition -> campaign -> customer` | Resolve ownership through that path and enforce it on affected backend reads/writes; avoid copying an owner field everywhere. |
| One shared mailbox | Associate each customer's authorized connection with their imports and delayed jobs; never fall back to the founder's connection. |
| Imports can encounter the same email again | Refresh imported facts while preserving fulfillment status and manual notes. |

Read the ownership, connections or background-work contract only where a decision is missing. This mapping is illustrative, not a measured savings claim. The [full mailbox example](examples/personal-mailbox-app.md) covers a different starting point without existing ownership; the [notes example](examples/paid-personal-app.md) starts with an established model.

## Apply it

1. Follow the host's instructions. Use [SKILL.md](SKILL.md) for consumer guidance; this repository's contributor rules do not override the host.
2. Inspect existing entities, IDs, auth, access checks and operations. Map only the requested transition using the selected spec.
3. Keep needed mappings, affected operations and observable checks in existing working notes or the optional [bridge plan](BRIDGE-PLAN.md). It adds no approval ceremony.
4. For a planning request, provide the plan. For an authorized implementation, continue through the bounded change and relevant checks. Ask founders business questions; derive engineering details from the host and contracts.

Field names are semantic examples, not a migration checklist. **Resolve values from existing data, provider state or derivation before adding storage.** Add a field only for information the chosen workflow needs and cannot otherwise obtain. Use native authorization mechanisms and maintained provider SDKs; keep provider defaults unless a concrete requirement justifies an override.

## Evidence and limits

A [Node/SQLite implementation attempt](evidence/private-customer-trial.md) passed with simulated providers and no maintainer engineering correction. An [existing-host Scout subscription pilot](evidence/scout-subscription-pilot.md) needed two corrections, then passed clean installation, normal builds, focused checks and four Firestore emulator checks. These are bounded observations, not proof of universal compatibility, live-provider acceptance, automatic activation or reduced effort.

See [scope and validation status](STATUS.md), [logical-model diagrams](MODELS.md) and [project background](HISTORY.md) as needed. Full workflow engines, marketplace billing and additional provider wrappers remain outside this kit.

## Reuse and contribute

[MIT licensed](LICENSE). Copy and adapt the specs into an agent's context; no attribution screen is required. Keep the license notice with substantial copies.

For manual skill loading, copy `SKILL.md`, `BRIDGE-PLAN.md`, `MODELS.md`, `LICENSE`, `specs/` and `examples/` together into the host's supported skill location, for example `.agents/skills/applift-specs/`. The directory name matches the skill name. Do not copy `.git` or replace the host's `AGENTS.md`; consult your agent's setup guide for supported paths.

Contributors must read [AGENTS.md](AGENTS.md). Improvements should remove a concrete mapping ambiguity or unnecessary host change; include the smallest relevant example and avoid speculative framework support.
