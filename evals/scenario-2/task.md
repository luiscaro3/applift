# Make service credits retry-safe

Write PLAN.md for adding service-credit consumption to an existing individual image-generation app. Plan only: no provider calls, charges, deployment, dependency installation or implementation. Preserve existing IDs, signup and architecture. Include concrete operations and acceptance checks.

Inspected host:

```text
users(id, creditBalance)
jobs(id, userId, requestKey, prompt, cost, state, providerRef, result)
payments(id, userId, providerPaymentRef, applied)
```

The database supports native transactions and uniqueness constraints. Managed auth already resolves an actor. Free signup and saved-image viewing already work; the product does not use subscriptions. `grantPurchasedCredits(event)` is called from verified payment notifications, but duplicate events for the same payment can currently increment twice. The authenticated payment includes a server-created order mapping to user and amount. `startGeneration(actor, requestKey, prompt)` currently reads balance, calls an external image provider, then separately subtracts the client-supplied cost and creates a job. Concurrent submissions can overspend. Existing `resumeJob(actor, jobId)` retries the provider request. `getJob` checks ownership.

Agreed policy: one generation costs 3 credits, fixed on acceptance; accepted jobs debit once and can resume without another debit even when remaining balance is zero. Insufficient funds reject new work. A confirmed failure refunds once. An unknown external outcome stays pending until reconciled; it must not be called a confirmed failure. The provider adapter supports request idempotency and status lookup. A restarted request may reuse its requestKey; reuse with changed prompt or owner must not reuse an unrelated operation. Payments may have multiple notification IDs for the same provider payment.

Describe the smallest safe grant/accept/resume/refund mapping using existing records. Cover duplicates, concurrency, process interruption after provider acceptance but before recording its result, cross-owner attempts and credit replenishment. Explain which decisions are observed versus proposed and which checks remain unrun.
