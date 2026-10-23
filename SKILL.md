---
name: applift-specs
description: Turn an existing personal app into a multi-user SaaS or add private customer access. Use when sign-in, multi-tenant data isolation, customer-owned connections, background imports, subscriptions, service credits or admin screens need mapping to existing entities and workflows. Skip new-app scaffolding and SDK calls whose host mapping is already solved.
license: MIT
---

# Apply AppLift to an existing app

Follow the user's request and the host's own instructions. This skill supplies integration guidance; AppLift's contributor `AGENTS.md` does not replace the host's rules. Use normal provider documentation/SDKs for mechanics. No AppLift runtime is needed.

Use one relevant contract if that is enough; skip solved decisions. AppLift describes relationships, authority and workflow guarantees. Choose the implementation from the actual host; the kit does not prescribe a stack, physical schema or general architecture repair process.

Target MVP-to-startup needs. Comprehensive observability, disaster-recovery and enterprise governance programs are outside default scope. Keep the selected workflow's authorization, isolation, data preservation and recovery intact; raise additional operational needs only where the host requires them. The kit does not certify whole-product readiness.

Inspect existing entities, IDs, auth, global credentials, queries and background operations. Mark mappings observed, proposed or unresolved. Ask the user business questions in ordinary language; derive engineering details from the host and selected contracts rather than asking the founder to design ownership or retry logic.

Read only the relevant contracts:

- Sign-in, local actor and session recovery: [identity](specs/identity.md).
- Personal/private versus shared data, existing-owner assignment: [ownership](specs/ownership.md).
- Each customer's external account and reconnection: [connections](specs/connections.md).
- Workers, source replay, search and preservation of fulfillment/manual progress: [background work](specs/background-work.md).
- Provider subscriptions linked to existing users/workspaces: [subscriptions](specs/subscriptions.md).
- Grant/load credits and consume them for services: [credits](specs/credits.md).
- Existing template/dashboard to authorized backend: [management](specs/management.md).
- Email unsubscribe, tracking/privacy choices or required terms acceptance: [user choices](specs/user-choices.md), only when affected. Reuse provider controls; this is not legal compliance certification.

Reuse IDs, native guards and provider-managed state. Resolve ownership through existing parents when possible; no owner column at every step, team model, role engine or mirrored billing ledger by default. A repeated import must preserve user-managed business progress. Re-evaluate current authority before committing delayed results.

Free accounts need no subscription by default. Use the subscription or credit contract only for the requested workflow; do not turn either into a mandatory monetization model.

Preserve native/provider defaults unless a concrete requirement justifies an override. State the reason for each custom setting; omit unnecessary configuration.

Keep any needed mapping in the short [bridge plan](BRIDGE-PLAN.md) or the host's existing working notes: connect each consequential requirement to a host operation and observable check. This is not an extra approval step. For a planning request, identify changes and unknowns. When implementation is requested, continue through the bounded changes and checks within authorization. Preserve existing data/behavior and record business clarifications separately from engineering rescue.

Consult [relationship diagrams](MODELS.md) or the [global personal-app example](examples/personal-mailbox-app.md) only if the mapping remains unclear. Report implemented versus unrun behavior and simulated versus live provider evidence. One passing case does not establish broad compatibility, organic discovery or reduced effort.
