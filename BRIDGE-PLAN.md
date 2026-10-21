# A small host-specific bridge plan

Fill this in for the requested capability. Use actual paths and existing names. Omit irrelevant sections; stop before implementation unless requested.

1. **Outcome and fit:** requested user behavior; relevant spec; existing mechanisms that already solve part of it.
2. **Mapping:** mark each mapping **observed** (inspected source/evidence), **proposed** (a change), or **unresolved** (missing fact/decision). For selected workflow values only, write `meaning -> actual host field/path, provider source or derivation -> authority -> workflow that needs it`. Add storage only for an identified gap; name that gap. Map relationships and the actual backend authorization boundary. Do not reproduce the full spec's field list.
3. **Changes:** affected routes, queries, commands, screens and existing records. Describe old-data assignment before migration. No automatic database rewrite.
4. **Workflow:** actor + trigger -> precondition/authoritative read -> local effect and commit boundary -> user outcome. State what happens on repeat, interruption and ordinary failure.
5. **Decisions/setup:** unresolved business choices; provider configuration/consent owned by the operator; official instructions needed. Do not guess credentials or silently choose a merchant/sharing policy.
6. **Checks and recovery:** connect each consequential requirement to an actual host operation and observable result: `requirement -> route/query/worker -> check -> observed result or unrun`. Include affected background/search paths, ordinary recovery and preservation of user-managed progress. State how to reverse the bounded change without losing subsequent data.
7. **Value and limits:** decisions this spec supplied, glue still needed, ambiguities/manual help. No invented time/token savings.

An incomplete mapping is a valid plan if its unknowns are explicit. It is not an implemented or validated integration.

Ask the user business questions in ordinary language: whether people share work, who pays, or whether cancellation ends access now or later. Derive engineering decisions from inspected source and the contracts. Requiring the user to explain ownership propagation, credential scope or replay safety is engineering rescue, not normal clarification. If implementation is already requested, use this as a working note and continue through the authorized change and checks.

Example of a sufficient mapping: `private note owner -> note.projectId -> project.ownerId -> existing authorized project lookup -> list/read/write notes`. If this already resolves the right owner, add no `note.ownerId` and no workspace/membership model. If subscriptions later target that owner, map the purchase to that existing user; do not create an access-owner table. This is an illustrative decision, not an executed host trial.
