# Recurring subscriptions and app access

Use when the **app owner sells recurring access** to a user or workspace. Begin with one recurring plan per access owner; model multiple products only if requested. An app whose users sell to their own customers has an additional merchant boundary and requires a separate payment-platform mapping. This spec does not supply marketplace settlement.

## Minimum logical model

**Access owner** means the existing user OR workspace receiving access; choose one for this product. It is a label, not a new table or a required polymorphic owner framework. **Subscription** is the provider-owned recurring agreement associated with that owner. **Plan** maps the offering to allowed app capabilities; it may be static configuration. The provider's customer/payer reference is stored or resolved with the subscription mapping; the payer may differ from the recipient of access. The app owner is the merchant, usually configuration rather than another database entity.

One access owner has zero or more historical subscriptions, but at most one current grant under this simple offering. Each subscription has one access owner and one selected plan in this slice. Provider subscription ID is scoped to provider account and test/live environment. Customer ID and email alone cannot establish an authorized app owner. **Access/entitlement is derived** from verified provider facts plus explicit app policy; it need not be a new entity. See [diagram](../MODELS.md#subscriptions).

## Map to the host

### Minimum information

These are values the selected workflow must resolve, not a list of billing columns to create.

| Information / meaning | Authority and simplest source | Needed when / workflow it enables |
| --- | --- | --- |
| `subscription_id` with provider/account/environment context | Provider reference; fixed account/environment can remain configuration | Locates the right recurring agreement for activation, renewal and reconciliation without mixing accounts or test/live data. |
| Access-owner reference | Server-authorized association to the existing user or workspace | Connects verified subscription facts to the recipient of app access. This relationship must be recoverable; never infer it from email or an untrusted browser field. |
| Customer/payer reference | Provider subscription/customer record, or existing host payer mapping | Checkout, portal and payment recovery need the correct payer. Resolve from provider state when available; it need not be duplicated locally or equal the access owner. |
| Plan/price reference and allowed capability mapping | Provider offering reference plus app-owned configuration or existing plan model | Translates a purchased offering into app behavior. No separate catalog or entitlement table is required. |
| Verified subscription/payment facts needed by the chosen policy | Authenticated provider event or authoritative read; retain only necessary facts if caching | Activation, failed-payment handling and renewal need trustworthy inputs. A provider status string alone is not an app permission. |
| Effective allowed capabilities and access cutoff, where time-bounded | Derived from verified facts and explicit app policy | Paid-operation checks need the effective decision. A billing-period end is not automatically an access cutoff; grace and cancellation policy can change the result. |

### Conditional recovery information

| Information | Authority and simplest source | Include only when |
| --- | --- | --- |
| `last_verified_at`: when the facts were authoritatively checked | Host records successful verification of the retained facts, not merely an event's arrival time | Local access facts are cached and a freshness policy needs it. Freshness does not solve out-of-order events; reconcile or use the provider's ordering mechanism. |
| Cancellation effective time | Provider-confirmed schedule interpreted under app policy | Cancellation ends access later. Read or derive it from existing provider facts rather than duplicating it by default. |
| Grace deadline | App policy plus a reliable failure/coverage anchor | The product offers a grace period. Repeated events must not restart grace; derive or retain a stable deadline only as needed. |
| Operation/idempotency reference | Host's stable identity for the intended purchase, reused with supported provider mechanisms | An interrupted remote creation could otherwise produce another purchase. Retain or recover the reference across retries; a new key per retry defeats it. |

Missing a business policy is a decision to resolve, not a reason to add another field. Unknown or absent access facts must not silently mean unlimited paid access. Provider-owned payment details and secrets remain outside the model.

- Reuse existing user/workspace and paid-feature guard. Map a provider subscription reference to it through a server-authorized checkout operation. Do not trust browser-supplied owner/price/paid flags.
- Relational: existing owner plus subscription mapping/projection keyed by provider account/environment/subscription ID. Document: equivalent owner reference or owner-scoped record. Enforce the same relationship with native mechanisms.
- Store only facts the app needs locally. A small access projection may include capability, effective access end and last verification; it is a cache/decision, not a second billing ledger. Choose acceptable freshness and outage behavior for the actual paid action.
- A free user has no paid subscription. Keep ordinary ownership authorization independent from paid access. Payment never grants another workspace's membership.

## Workflow contract

| Trigger / actor | Authority and local effect | Repeat or recovery / user outcome |
| --- | --- | --- |
| Authorized payer starts checkout | Verify payer's permission to buy for selected owner; select an allowed plan server-side; use official hosted checkout and a stable operation correlation. | If creation times out, reuse supported idempotency key or inspect result before creating again. Prevent a second purchase for the same intended current grant. |
| Browser returns from checkout | Show pending until backend verifies authoritative provider facts and owner mapping. | A successful redirect alone grants nothing. Refresh/recheck pending status safely. |
| Verified activation or renewal | Authenticate provider event or perform authorized provider read; map subscription/account/environment to owner; update local projection atomically. | Repeated delivery has the same result. Out-of-order facts must not overwrite newer state; use provider-supported ordering/version or reconcile current state. |
| Payment fails | Provider handles configured payment retries and hosted payment-update flow. App applies explicit grace/access policy. | Show payment action to authorized payer. End access at the chosen boundary if unresolved; avoid a custom dunning engine. |
| Payment recovers | Verify current provider facts and recompute access. | Restore only the mapped owner's capabilities. Repeated recovery does not duplicate grants. |
| Payer cancels | Verify management permission and use provider portal/API. Distinguish immediate cancellation from scheduled period-end cancellation. | Scheduled cancellation retains access only to the specified effective end under policy; repeated request converges to current state. |
| App receives paid operation | Check actor's native permission AND owner's effective entitlement at the enforcing boundary. | Expired/unverified state follows explicit outage/freshness policy; it cannot silently become a permanent grant. |
| Event is missed or handler fails | Reconcile authoritative current subscription state for the affected owner/subscription; apply the same access policy. | Record visible failure/pending state and provide a bounded retry/operator action. No full provider event archive is required unless the implementation needs it. |

An event ID dedup record is optional if effects already converge; email/other irreversible effects need their own delivery idempotency. Use the provider's authenticated delivery and SDK verification mechanisms; never invent a signature protocol.

## Decisions and essential checks

Fill in: who can purchase/manage, access owner, plan-to-capability mapping, qualifying provider facts, free behavior, grace duration (including zero), cancel timing, access freshness and outage behavior. Trials and plan changes are additional branches only if the offering has them. Provider status names alone do not settle these business choices.

Operator owns product/price, portal, recovery and authenticated endpoint setup. Check verified activation grants the correct owner, browser spoofing/another owner is denied, and duplicate/reordered notification or reconciliation converges. Check failure -> policy-defined grace/end -> verified recovery with illustrative facts before any separately authorized provider run.

Official examples: [subscription lifecycle](https://docs.stripe.com/billing/subscriptions/overview), [events](https://docs.stripe.com/billing/subscriptions/webhooks), [delivery behavior](https://docs.stripe.com/webhooks), [provider-owned recovery](https://docs.stripe.com/billing/revenue-recovery), [Stripe agent skills](https://docs.stripe.com/skills). These illustrate mechanisms; no all-provider compatibility is claimed.
