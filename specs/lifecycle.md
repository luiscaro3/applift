# Account and paid-capability lifecycle defaults

Use when adding subscriptions or service credits to an existing app. Propose these defaults, preserve an already agreed product policy, and ask only about meaningful exceptions. They are configurable product decisions, not universal provider rules or legal promises. Reuse existing accounts, guards and jobs; no new entities or lifecycle engine are implied.

Authentication identifies the actor. Account activation establishes valid onboarding/ownership. Subscription or credit eligibility permits selected chargeable operations. Keep these decisions separate: an expired subscription does not by itself invalidate identity, ownership or the account. Free accounts need no subscription.

## Recommended starting policy

| Event | Default app behavior |
| --- | --- |
| Signup / account activation | Establish the existing user or workspace independently of paid capability eligibility. Explain the chosen offer before purchase; never treat a successful redirect as payment verification. |
| Subscription cancellation | Stop renewal through the provider; retain paid capabilities until the verified paid-through cutoff. Immediate termination is an explicit exception. A scheduled cancellation is not account deletion. |
| Subscription expires / payment remains unresolved | Keep sign-in, authorized existing-data viewing/export and billing recovery available; block chargeable mutations. Do not delete data as a side effect. Propose no additional grace unless the product needs it. |
| Credits are insufficient | Keep the same account/data boundary; decline new chargeable work without debiting or performing its effect, and offer replenishment. Apply the [credit contract](credits.md) for atomic, idempotent grants/debits and recovery of already accepted operations. No subscription is required. |
| Scheduled / queued chargeable work executes | Recheck current ownership, authorization and eligibility before side effects; enqueue-time eligibility is insufficient. Credit jobs reuse their accepted debit rather than require payment twice. Pause or decline ineligible work using native job state. Preserve completed business progress. |
| Renewal / replenishment | Restore eligible capabilities after verification. Do not unexpectedly release an externally consequential backlog: publishing-like queues default to explicit resume after reviewing missed work. Harmless retries can retain the host's agreed automatic behavior. |
| Account deletion | Treat as a separate, explicitly confirmed action. Stop new work, resolve subscription/Checkout cancellation under the agreed policy, and purge only the authorized account scope. Reuse native progress/retry mechanisms for partial failure; report pending until required steps finish. Disclose retained provider records, backups or shared data truthfully; do not promise deletion of the person's external identity. |

## Resolve exceptions, not engineering details

Present the applicable default and its user-visible effect. Ask when the host/product needs different cancellation timing, grace, data viewing/export, retention/deletion scope or backlog resumption. The developer must choose and disclose retention/export exceptions; if export is unavailable, say so rather than promise it. Do not invent an export framework or retention schedule for completeness.

Map eligible capabilities to actual operations, including workers. Keep ownership authorization enforced even where viewing is free. Use verified provider facts and the host's freshness/outage policy for paid decisions; account availability is not permission for unlimited paid work. Record the agreed choices briefly in existing working notes. Use [subscriptions](subscriptions.md) and [background work](background-work.md) for the implementation boundaries; keep provider calls outside retryable database transactions.

## Acceptance checklist for the chosen transition

- Cancel renewal: verify the effective cutoff; canceling does not delete the account or prematurely end agreed paid-through access.
- At expiry/insufficient credits: sign-in, authorized data access and billing recovery follow policy; chargeable requests cannot bypass the backend guard.
- Retry/concurrency: credit grants/debits cannot duplicate or overdraw; an accepted operation resumes without a second charge.
- Queue execution: revoked authority or lost eligibility prevents new side effects. Restoring funds/access does not silently publish the missed backlog.
- Explicit deletion: unrelated owners' data stays intact; partial failure remains visible and safely retryable; retained-data statements match actual behavior.

Check only affected paths. This guide is a recommended decision contract, not evidence that a host or provider has implemented it.
