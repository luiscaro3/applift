# Credits and service consumption

Use when an existing user or workspace receives credits and spends them on services. Free accounts without subscriptions are valid. This optional contract is independent of [subscriptions](subscriptions.md). It maps credit ownership, trusted additions and spending without duplicate charges.

## Minimum logical model

**Credit owner** is the existing user OR workspace. **Available credits** belong to that owner. A **grant** adds credits; **consumption** spends them. These effects can use existing payment/job records; no new wallet or ledger is required. See [models](../MODELS.md#credits).

| Needed meaning | Authority and simplest source | Required behavior |
| --- | --- | --- |
| Credit owner | Existing user/workspace relationship | Preserve ownership across grants, consumption, results and retries. |
| Available amount | Host balance or existing credit history | Enforce sufficient availability at the mutation boundary; browser values are display only. |
| Grant amount/source | Trusted app decision or verified payment mapped to owner | Reuse the provider-scoped payment reference for purchases. Redirects and client amounts cannot mint credits. |
| Service cost | Server-controlled policy | Validate the charge in the app's exact credit unit; the client cannot select it. An accepted operation keeps its agreed cost across retries. |
| Operation identity/outcome | Existing payment/job/operation record | Recover the same identity across retries; bind owner, action and amount, reject conflicting reuse, and retain whether the change applied. |

**Choose one availability authority.** An owner balance plus existing operation outcomes is often sufficient. If the host already uses a ledger, derive availability from it or maintain its balance atomically. Add credit history only for a concrete traceability or balance-reconstruction need that existing records cannot supply. Use native transactions/conditional writes to keep availability nonnegative and couple each change with its applied outcome. Reading a history sum before a separate debit does not prevent concurrent overspending.

## Workflow and recovery contract

- **Grant/top-up:** resolve trusted amount and owner; atomically add once and retain the applied outcome. Different notifications for one purchase resolve to the same grant identity.
- **Consumption:** check native permission and owner; resolve an existing operation before treating the request as a new charge. For new work, atomically check server cost against availability, debit once and retain the operation. A retry resumes/returns that operation even when the remaining balance cannot fund another one. A new key per retry defeats protection. For work entirely in one database, commit its result in the same transaction.
- **External work:** for charge-on-acceptance, commit debit and accepted operation before dispatch through the existing job/worker. Reuse provider-supported idempotency and retain provider correlation. A database transaction cannot make a remote effect atomic; never place paid calls inside retryable database transactions.
- **Interrupted result:** inspect the operation/provider outcome. Repeat only with safe provider idempotency or confirmed non-execution. Otherwise surface pending state for bounded operator recovery; never blindly repeat an uncertain paid effect or charge again.

Recheck ownership at the mutation/worker boundary, including after remote work. Credits never authorize another owner's resources. Known failures follow the agreed charge policy; any credit restoration is also a trusted operation applied once.

## Small worked mapping

A personal app has `users`, owner-scoped `jobs`, and verified `payments`. Signup is free; an accepted processing job costs 3 credits. Map availability to the user, grant identity to payment, and consumption identity/outcome to job. Add only missing availability/applied-outcome information.

With 5 credits, two concurrent jobs costing 3 cannot both be accepted. The accepted job leaves 2; request/worker replay cannot debit again. Repeated top-up notifications cannot grant twice. A remote timeout follows the recovery rule above. This is illustrative, not execution evidence.

## Decisions and essential checks

Resolve owner, trusted grant sources, cost, charge timing and known-failure policy. Make charging on acceptance explicit; do not silently substitute it for a successful-delivery promise.

Check free signup without subscriptions, cross-owner denial, client amount manipulation, duplicate grants/consumption, concurrent overspending and interrupted external work. Use the selected provider's official payment/idempotency mechanisms. This spec supplies no runtime or credit execution evidence.
