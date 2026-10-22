# Communication preferences, privacy choices and terms

Use only when a requested workflow sends customer email, adds tracking/data use, or needs terms acceptance. Save the mapping between a person's choice and the operations it controls. Reuse the host and provider mechanisms; no consent platform, new tables or universal legal documents are required by this contract.

## Minimum mapping

**An existing recipient or actor makes a choice for a defined sender and purpose; the affected operation consults its current authority.** A provider's suppression record, existing preference or browser choice may already supply everything needed. An email address can identify a delivery destination without proving account ownership.

| Needed meaning | Simplest authority |
| --- | --- |
| Who and what the choice covers | Existing recipient/actor plus the relevant sender, purpose and account relationship. Do not invent a preference per workspace unless that is the actual boundary. |
| Current permission or suppression | Existing delivery provider, consent mechanism or host record. Identify which source wins if they disagree; a stale cache cannot override a later restriction. |
| Terms accepted, if acceptance is needed | Existing actor and identifiable terms version. Retain time/evidence only as needed for the applicable workflow; showing a notice is not proof of acceptance. |

Collect only missing information needed to enforce or evidence the selected workflow. Marketing choice, tracking choice, service authorization and contract acceptance have different meanings; do not collapse them into one `consent` flag.

## Workflow boundaries

| Trigger | Effect and recovery |
| --- | --- |
| Recipient unsubscribes from marketing | Use the provider's supported opt-out/suppression path. It must work without app login. Repeating the request leaves the same suppression in effect. Do not cancel billing, delete an account or disconnect a mailbox. |
| A queued marketing send or retry runs | Apply the current suppression at the actual dispatch boundary, preferably provider-enforced. Reimporting a contact, reconnecting or renewing a subscription cannot silently opt them back in. If preference state is unavailable, defer affected marketing rather than assume permission. |
| Customer requests another message category | Distinguish necessary service/security messages from promotions by actual content and purpose. Do not relabel marketing as transactional to bypass an opt-out. |
| Visitor changes a tracking/privacy choice | Map the choice to the actual scripts, SDKs and server-side destinations it governs. Reuse the existing mechanism; stop affected future activity when required, including after reload. Where applicable, honor recognized browser opt-out signals. A banner alone does not enforce a choice. |
| Terms are presented or accepted | Link the appropriate product terms/EULA and privacy notice. Capture acceptance only when the workflow needs it, bound to the right actor/version. Agreement to service terms does not itself authorize unrelated marketing or tracking. |

Example: an import discovers an unsubscribed contact again. Refreshing their source facts must preserve the provider's suppression; an already queued campaign must still consult that suppression before dispatch. This is the same preservation boundary used for [background work](background-work.md), applied to recipient choices.

Account access/export/deletion requests are separate authorized operations, not email preferences. If in scope, map the existing ownership and retention rules to the affected data/providers and prevent stale imports from recreating removed data contrary to that policy. Do not promise immediate deletion of everything or invent a retention schedule.

## Applicability and checks

Business and legal requirements depend on audience, jurisdictions, message purpose, tracking and data practices. Identify those facts and unresolved legal decisions; obtain appropriate legal input where needed. Do not impose a cookie banner or EULA on every app, draft universal legal terms, or describe AppLift as compliance certification.

Choose checks for the affected path: unsubscribe twice; replay an import and a queued send after opt-out; confirm the right sender/recipient boundary and unrelated service behavior remain intact; change tracking choices and reload; verify any required acceptance refers to the correct actor/version. These are proposed host checks, not executed AppLift acceptance evidence.

Official US starting points, reviewed October 22, 2026:

- [FTC CAN-SPAM guidance](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business): commercial email includes B2B; provide an accessible opt-out, keep it working for at least 30 days after sending and honor requests within 10 business days. Sender identity, content and postal-address duties also apply. Prefer prompt provider suppression; the deadline is not a reason to delay it.
- [California CCPA guidance](https://oag.ca.gov/privacy/ccpa) and [Global Privacy Control](https://oag.ca.gov/privacy/ccpa/gpc): covered businesses have notice and applicable data-rights/opt-out obligations. Applicability is not determined merely by whether a site uses cookies. Check current rules for the actual audience; these links are not a complete US or international compliance checklist.
