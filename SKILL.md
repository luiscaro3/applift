---
name: applift-specs
description: Grow an existing personal app into private customer access. Use when adding sign-in, customer-owned data or connections, background imports, subscriptions, or an admin screen to existing code and the missing work is mapping ownership and workflows. Skip unrelated app creation and straightforward SDK calls whose host mapping is already solved.
license: MIT
---

# Apply AppLift to an existing app

Follow the user's request and the host's own instructions. This skill supplies integration guidance; AppLift's contributor `AGENTS.md` does not replace the host's rules. Use normal provider documentation/SDKs for mechanics. No AppLift runtime is needed.

Inspect existing entities, IDs, auth, global credentials, queries and background operations. Mark mappings observed, proposed or unresolved. Ask the user business questions in ordinary language; derive engineering details from the host and selected contracts rather than asking the founder to design ownership or retry logic.

Read only the relevant contracts:

- Sign-in, local actor and session recovery: [identity](specs/identity.md).
- Personal/private versus shared data, existing-owner assignment: [ownership](specs/ownership.md).
- Each customer's external account and reconnection: [connections](specs/connections.md).
- Workers, source replay, search and preservation of fulfillment/manual progress: [background work](specs/background-work.md).
- Recurring paid access: [subscriptions](specs/subscriptions.md).
- Existing template/dashboard to authorized backend: [management](specs/management.md).

Reuse IDs, native guards and provider-managed state. Resolve ownership through existing parents when possible; no owner column at every step, team model, role engine or mirrored billing ledger by default. A repeated import must preserve user-managed business progress. Re-evaluate current authority before committing delayed results.

Preserve native/provider defaults unless a concrete requirement justifies an override. State the reason for each custom setting; omit unnecessary configuration.

Use the short [bridge plan](BRIDGE-PLAN.md) as a working note: connect each consequential requirement to a host operation and observable check. For a planning request, identify changes and unknowns. When implementation is requested, continue through the bounded changes and checks within authorization. Preserve existing data/behavior and record business clarifications separately from engineering rescue.

Consult [relationship diagrams](MODELS.md) or the [global personal-app example](examples/personal-mailbox-app.md) only if the mapping remains unclear. Report implemented versus unrun behavior and simulated versus live provider evidence. One passing case does not establish broad compatibility, organic discovery or reduced effort.
