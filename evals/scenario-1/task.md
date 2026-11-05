# Keep cancellation and background work consistent

Write PLAN.md for correcting subscription access mapping in an existing individual publishing app. Preserve its product concept and native architecture. Plan only: do not implement, deploy or contact a payment provider. Include operation-level acceptance checks and evidence limits.

Inspected host:

```text
users(id, billingCustomerId, subscriptionId, priceId,
      allowedCapabilities, verifiedAt, paidThrough, revision)
posts(id, authorId, body, status)
jobs(id, postId, stage, state)
```

The app owner is the merchant. Verified subscription state is already stored on the existing user, with fixed merchant/test context in configuration. The billing adapter supplies authenticated events and an authoritative subscription read outside database transactions. `requirePostOwner(actor, postId)` protects the existing user/post relationship. `canPublish(user, now)` currently trusts `allowedCapabilities` without checking verification age or cutoff. `publishPost(actor, postId)` calls that guard, while the worker `prepare -> generate -> publish -> commit` checks only at enqueue time. A Checkout success redirect currently sets `allowedCapabilities` directly from a query parameter. Events may arrive twice or out of order, and a slow refresh may race a newer cancellation event.

Agreed product policy: free signup and reading one's own saved content remain available. Canceling renewal retains publishing until the verified paid-through time; after expiry no new chargeable effects. No extra grace period. Verified state may be reused for at most 10 minutes and never beyond paidThrough; an outage cannot extend either limit. After replenishment/renewal, missed publishing jobs need explicit resume. Deletion is separate. Provider portal and payment retries already exist.

Propose the smallest changes for purchase activation, scheduled cancellation, expiry, recovery and multi-stage jobs. Include what happens with fresh versus stale facts, a provider outage, an ownership change between stages and reordered/racing updates. Do not create a new billing platform or change the agreed policy.
