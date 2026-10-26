# Scope and evidence

Draft 0.3, updated 26 October 2026. A specification kit with zero product runtime code or package dependencies. Isolated implementation-trial code is separate from this package.

## Available

- Six contracts: identity/session recovery, personal/shared ownership, customer-owned connections/reconnection, background processing/business progress, subscriptions/access and management-screen mapping.
- Optional [user-choice contract](specs/user-choices.md), added October 22, 2026: email suppression across imports/queued sends, privacy-choice enforcement and conditional terms acceptance. Reviewed against linked official US guidance; no host implementation trial or legal-compliance validation is claimed for this addition.
- Optional [credit contract](specs/credits.md): trusted grants, service consumption and retry-safe atomic credit changes on existing accounts/operations. No subscription requirement or mandatory ledger. Subscription guidance retains provider subscription/customer identifiers in the existing canonical mapping. The credit contract has no executed integration or production evidence; subscription evidence below does not validate credit consumption.
- A short [lifecycle decision guide and checklist](specs/lifecycle.md): recommended cancellation/expiry, credit eligibility, queued-work resumption and separate account-deletion policies. Configurable defaults, not a new framework or provider guarantee. No host execution evidence is claimed for this addition.
- Explicit [untrusted imported-content boundary](specs/background-work.md) in the consumer skill, connection guidance and mailbox example. Embedded instructions cannot supply authority; legitimate extraction remains supported. Documentation review and a proposed adversarial check are not proof of runtime prompt-injection resistance or a cleared third-party audit.
- Logical relationship diagrams, workflow-local field guidance and conditional recovery information.
- A short bridge-plan template with observed/proposed/unresolved mappings and requirement-to-operation checks; examples for both a global personal mailbox app and an already-structured notes app.
- A self-contained instruction-only skill with one documented project-local loading path. Contributor instructions are separate from consumer guidance.
- Standing agent instructions preserving native architecture and limiting additions to demonstrated gaps.
- MIT license and the supplied AppLift logo.

The docs are intended to save host-mapping decisions rather than replace provider SDK instructions. No mandatory schema, Store interface, role system, ORM or code generator is supplied.

The intended lifecycle is MVP to an early operating startup. This kit is not a complete SaaS operating model or enterprise-readiness checklist. Comprehensive observability, disaster-recovery programs and enterprise governance are outside default scope; their absence does not invalidate a selected integration contract. Basic authorization, customer isolation, data preservation and ordinary recovery remain part of the relevant contracts. Additional operational needs belong to the actual host and use case. This scope choice is not a claim that early startups never need monitoring, backups or stronger controls, nor that adopting AppLift makes a whole product ready to sell.

## Evidence and limits

Author review checked field authority, relationship/workflow consistency, optional storage and recovery paths. Relative documentation links and image references were checked locally. The worked example is hypothetical and was not executed. Mermaid source is supplied; a successful rendering test is not claimed.

One fresh-context implementation attempt passed for a representative global personal Node/SQLite backend with local provider simulators: [evidence and reproducible fixture](evidence/private-customer-trial.md). Seven implementer checks and nine held-out evaluator scenarios passed without maintainer engineering correction. The test used the explicitly supplied public kit; it does not demonstrate organic discovery, implicit skill activation, reduced effort, broad compatibility or production readiness. Live provider acceptance remains separate.

Skill frontmatter/name and relative-reference checks passed, and its installed project-local copy was unchanged during the attempt. The bundled skill validator could not run because its Python environment lacked PyYAML; no validator pass is claimed. Explicit path loading was exercised, not automatic discovery.

A subsequent [existing-host subscription pilot](evidence/scout-subscription-pilot.md) reached an assisted candidate with two maintainer corrections. Clean frozen installations, normal backend/frontend builds, focused checks and four actual Firestore emulator checks passed. It observed filesystem discovery/use of the installed kit, not native implicit activation. That isolated pilot did not validate the browser, production database or actual provider delivery. The transaction-boundary omission was clarified in the subscription spec; consumer/contributor instructions now require a concrete reason before overriding native/provider defaults. No reduced-effort or causal-benefit claim is supported.

A separate [deployed Scout subscription check](evidence/scout-subscription-pilot.md#deployed-scout-with-actual-stripe-sandbox), reported 23 October 2026, used actual Stripe sandbox Checkout and signed webhook synchronization against the deployed application. Card-free $0/month signup created a customer/subscription and paid $0 invoice. The canonical workspace mapping matched provider customer/subscription/price IDs and merchant/test context. Four webhook deliveries returned HTTP 200; activation allowed workspace access and immediate provider cancellation through the Stripe Dashboard persisted canceled state and revoked access in a fresh view. The release image passed 28/28 checks. This is deployed-host sandbox evidence, not live-mode billing, paid-customer adoption, unaided adoption or credit execution evidence.

## Stopping rule

The planned bounded implementation attempt has completed. Its business choices and local provider interfaces were supplied in the host README; no additional business clarification or author engineering rescue was reported. A plan-only result would have supported mapping quality only. This result executes actual SQLite migration, service guards, imports, queue recovery and search in one fixture, while keeping external-provider behavior simulated.

The submitted implementation preserved old IDs, data and user-managed progress and passed the affected private-access/background checks on first evaluation. Stop here unless another concrete host or observed failure justifies more work. Do not turn one success into a generalized compatibility claim or restart broad benchmarks/provider certification.

## Conditional scope

Connections and background ownership are now included because the personal-email-app transition requires them. Uploads, marketplaces, enterprise access systems, general workflow engines and additional provider wrappers remain outside the supported slice. The deeper trial budget does not justify extra abstractions or commercial services.
