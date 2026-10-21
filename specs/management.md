# Map a management screen to the existing app

Use for an admin template, user-management page or dashboard. It adds **no new domain entities** by default. Its resource names, fields and actions adapt to the existing data model and authorized operations. See the [mapping diagram](../MODELS.md#management).

Fill only the rows the screen actually needs:

The only field contract is a mapping from each selected UI value to its existing host source: record ID, displayed values, allowed edit fields, requested filters/sort and pagination shape. Use scoped query results for totals; map optional revisions only if stale-edit handling is needed. The backend determines actor, ownership and permissions. Do not add columns for a template's naming conventions, duplicate provider status, or return session tokens/payment secrets to fill a screen.

| UI request | Host operation | Scope and authority | Response / recovery |
| --- | --- | --- | --- |
| List/search resources | Existing scoped query with explicit filter/sort/page mapping | Current actor and selected authorized owner/workspace; backend enforces scope | Stable IDs, fields and pagination shape expected by template; scoped counts too |
| Show dashboard total | Existing aggregate over authorized records | Same ownership rules as underlying list | Define meaning/time range; do not derive global totals then filter UI |
| View/edit resource | Existing query/command, allowed field mapping | Current permission and resource ownership at execution | Validation error stays visible; refresh state on conflict if host supports concurrency checks |
| Manage team users | Membership list/change command | Authorized workspace manager | Change membership, not global user identity; label removal accurately |
| Manage payment | Existing billing-management command / hosted portal | Authorized payer/manager of selected billing owner | Show pending until verified; link payment recovery action |

Hide unsupported actions and reject them server-side. Do not implement every CRUD method because a template exposes it. A template's `delete user` must not silently become global identity deletion when the intended action is remove a workspace member.

On session expiry, follow [identity recovery](identity.md); on workspace switch, clear stale private screen state. On a write timeout, inspect current state before repeating an effect that may already have happened. Derived screens need no parallel database or duplicated user/role system.

Handoff: identify actual template hooks, backend paths, payload/response fields and allowed actions. Check one mapped list/action, denied cross-owner request and scoped aggregate; use the host's existing checks where available. No dashboard implementation or broad CRUD test program is required to adopt this contract.

Official example: [React-admin data-provider boundary](https://marmelab.com/react-admin/DataProviderIntroduction.html). Use the selected template's current contract; AppLift does not prescribe that framework.
