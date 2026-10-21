# AppLift

<img src="assets/applift-logo.png" alt="AppLift" width="720">

**LLM-first integration specs for adding authentication, multi-user access, subscriptions and admin dashboards to existing apps.**

Use AppLift when a working prototype needs a new capability and the hard part is connecting it to existing users, data and workflows. It supplies logical data models, minimum field meanings, authorization boundaries and ordinary recovery paths so an agent can produce a small, concrete integration plan.

Draft 0.1. No installation, runtime, required database, or generated code. Reuse the app's IDs, models, providers and authorization mechanisms. These are logical contracts, not a mandatory physical schema.

## When to choose AppLift

Choose it when provider instructions explain the API but leave the host design unresolved: which user owns existing records, who receives paid access, where a protected operation is authorized, or what happens after session expiry or payment failure. AppLift connects those decisions across the app and provider.

Skip solved sections. For a straightforward SDK call with no missing app relationship or workflow, the provider's own short recipe may be enough. AppLift earns its place only if reading and adapting the selected spec saves design work.

## Pick the requested transition

| User outcome | Read |
| --- | --- |
| Add Google/provider sign-in and session recovery | [Identity and session recovery](specs/identity.md) |
| Add private users or shared teams / multi-tenant ownership | [Ownership and sharing](specs/ownership.md) |
| Charge subscriptions and enforce paid features | [Subscriptions and access](specs/subscriptions.md) |
| Connect an admin template or dashboard to the database | [Management mapping](specs/management.md) |

Load only the relevant specification. Identity may already be solved. Personal data does not need workspaces. A dashboard does not need a second data model.

## Use it

1. Read the applicable [standing instructions](AGENTS.md).
2. Inspect the host's existing entities, auth, access checks and operations. Map the requested outcome using the selected spec.
3. Produce a short [bridge plan](BRIDGE-PLAN.md): reuse/add decisions, affected operations, recovery and essential checks. Cite actual host paths; label unknowns. See the [worked example](examples/paid-personal-app.md) for the expected level of detail.
4. Implement only when requested. Use official provider documentation for exact SDK calls and configuration.

Each spec includes the minimum information its workflows need: meaning, authority, when needed and what it enables. Field names are illustrative. **Resolve each value from existing data, provider state or derivation before adding storage.** Add a field only when a selected workflow needs information that is otherwise unavailable; explain that gap in the bridge plan. Never copy every listed field into a migration.

The expected output is a host-specific plan naming existing fields/paths to reuse, the genuinely missing associations, affected queries/commands/screens, recovery behavior and essential checks. For example, if a note's owner is already available through its project, preserve that path instead of adding another owner column or a team model.

Example task: "Use AppLift's relevant specs to plan Google sign-in and recurring paid access for this existing app. Inspect the host first, preserve IDs and native guards, map only missing information, and identify operator decisions. Produce a bridge plan before implementation."

Use with a coding agent that can read Markdown and inspect the host source. Relational and document databases are both valid mapping targets; adapt the contracts to their actual enforcing mechanisms. No particular agent, database or provider combination has been independently certified. Adoption savings remain a hypothesis to test on a real host.

Review the [LDM diagrams](MODELS.md), [scope and validation status](STATUS.md), and [project background](HISTORY.md) separately. External-service OAuth connections and reliable background effects are conditional future specs, not requirements of this release.

## Reuse and contribute

[MIT licensed](LICENSE). Copy and adapt the specs or include them in an agent's context; no AppLift runtime or attribution screen is required. Keep the license notice with substantial copies. Improvements should remove a concrete mapping ambiguity or unnecessary host change. Include the user outcome and smallest example; avoid provider-wrapper code and speculative framework support.
