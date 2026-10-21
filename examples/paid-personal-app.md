# Example: add sign-in and paid exports to a personal notes app

Illustrative bridge plan, not tested code or a migration template. Read only the [identity](../specs/identity.md), [ownership](../specs/ownership.md) and [subscription](../specs/subscriptions.md) sections needed. Add [management mapping](../specs/management.md) if the requested screen needs it.

## Existing app and requested outcome

Assume the host already has `users.id`, `projects.id`, `projects.owner_id` and `notes.project_id`. The current founder is an existing user; old projects have that known owner. A backend project guard exists. If inspection contradicts those assumptions, revise the plan before implementing it.

Request: allow Google sign-in, keep each person's notes private, sell recurring paid exports, and show a notes dashboard. Users do not share projects. No workspace, membership or new role system is needed.

## Decisions before implementation

For this example only: allow new signups; new users start with no projects; reading/editing remains free; exports require an active paid grant; one recurring offering; no trial or payment grace; scheduled cancellation retains access to the confirmed paid-through boundary. A failed renewal does not extend it. If provider state is unavailable, exports require a still-valid verified cached grant or wait for verification; free operations continue.

These choices require product agreement in an actual host. They are not AppLift-wide defaults. The founder's existing data is linked only after authenticated proof; matching an email alone is insufficient.

## Map only the missing information

| Needed meaning | Resolve from | Smallest change / authority |
| --- | --- | --- |
| Local actor | Existing `users.id` | Preserve IDs. Use managed auth directly if it already resolves this key; otherwise add one issuer/subject-to-user mapping with native uniqueness. |
| Session validity | Auth service's supported verifier | Attach verification to existing backend middleware; add no session table. |
| Note owner | `note.project_id -> project.owner_id` | Reuse the project guard for list/detail/write/export. Add no `note.owner_id`. Validate parent selection on note creation/moves. |
| Paid recipient | Existing user | Associate checkout with the server-authorized actor. No access-owner entity. |
| Provider agreement | Provider-scoped subscription reference mapped to that user | Reuse an existing billing association if present. Otherwise retain the smallest recoverable association using trusted host storage or provider-supported server-controlled metadata. No full local billing ledger. |
| Paid capability | One configured plan -> `export` | Configuration, not another catalog or entitlement table. |
| Current export permission | Verified provider facts + the above policy | Derive access. Cache only if needed; retain verification time/cutoff with any cached decision. |
| Dashboard values | Existing scoped project/note query | Map fields and totals. No new domain entities or global totals filtered in the browser. |

## Workflow and attachment points

1. **Login callback / session middleware:** verify provider identity, resolve the local user, and provision only under the signup policy. Repeated callback resolves the same user. Existing records retain their IDs and owner. Expiry uses the auth SDK's refresh; rejected refresh clears private context and offers sign-in.
2. **Project/note queries and commands:** derive the actor from the verified session and use the existing enforcing guard. Scope counts and child records too. Another user's project ID is denied. A sensitive write must keep its permission check coupled to the native mutation boundary.
3. **Checkout command:** backend selects the allowed offering and establishes the user association. Use one stable purchase-operation reference where needed. A timed-out create is inspected/retried with supported idempotency rather than starting another purchase.
4. **Provider event handler or authoritative reconciliation:** authenticate the observation, resolve the correct account/environment/subscription/user and recompute the export grant. Duplicate or older observations cannot extend or overwrite newer access; reconcile current facts when ordering is uncertain. A browser return shows pending until verification.
5. **Export command:** require both project ownership and effective paid access. Payment for one user never unlocks another user's notes. Failed renewal/cancellation applies the policy's cutoff; verified payment recovery restores exports. Show the authorized payer the provider's hosted payment-update/management flow.
6. **Dashboard:** reuse the scoped query and map its response to the selected template. Reset private caches on account change. Hide unsupported management actions and reject them on the backend.

## Operator setup, checks and recovery

Operator setup: approved OAuth application/redirects and consent, billing offering/portal/recovery settings, and authenticated provider delivery if events are used. No credentials or endpoint are provisioned by this plan.

Essential checks: repeat login preserves user identity; user B cannot read/export user A's notes; verified purchase grants only its mapped user; redirect spoofing grants nothing; duplicate observation has no extra effect; failure/cancellation/recovery changes exports under the selected policy. Preserve free workflows and old IDs.

Before host changes, record the affected paths and take the host's normal reversible migration checkpoint. Preserve new records and mapping data if reverting an integration; do not restore an old snapshot over subsequent customer data. If billing activation is incomplete, leave existing free behavior usable and surface paid access as pending/denied, not falsely enabled.

## What AppLift contributes

The saved design decisions are explicit: no team model, no duplicate note-owner field, no custom session store, no full billing ledger, no entitlement table, no new dashboard database. The remaining work is host-specific callback/guard/query wiring, the small subscription association and provider setup. Whether this actually reduces agent effort remains to be tested independently.
