# Scope and evidence

Draft 0.2, 21 October 2026. A specification kit with zero product runtime code or package dependencies. Isolated implementation-trial code is separate from this package.

## Available

- Six contracts: identity/session recovery, personal/shared ownership, customer-owned connections/reconnection, background processing/business progress, subscriptions/access and management-screen mapping.
- Optional [user-choice contract](specs/user-choices.md), added October 22, 2026: email suppression across imports/queued sends, privacy-choice enforcement and conditional terms acceptance. Reviewed against linked official US guidance; no host implementation trial or legal-compliance validation is claimed for this addition.
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

A subsequent [existing-host subscription pilot](evidence/scout-subscription-pilot.md) reached an assisted candidate with two maintainer corrections. Clean frozen installations, normal backend/frontend builds, focused checks and four actual Firestore emulator checks passed. It observed filesystem discovery/use of the installed kit, not native implicit activation. Browser, production database and real-provider acceptance remain unverified. The transaction-boundary omission was clarified in the subscription spec; consumer/contributor instructions now require a concrete reason before overriding native/provider defaults. No reduced-effort or causal-benefit claim is supported.

## Stopping rule

The planned bounded implementation attempt has completed. Its business choices and local provider interfaces were supplied in the host README; no additional business clarification or author engineering rescue was reported. A plan-only result would have supported mapping quality only. This result executes actual SQLite migration, service guards, imports, queue recovery and search in one fixture, while keeping external-provider behavior simulated.

The submitted implementation preserved old IDs, data and user-managed progress and passed the affected private-access/background checks on first evaluation. Stop here unless another concrete host or observed failure justifies more work. Do not turn one success into a generalized compatibility claim or restart broad benchmarks/provider certification.

## Conditional scope

Connections and background ownership are now included because the personal-email-app transition requires them. Uploads, marketplaces, enterprise access systems, general workflow engines and additional provider wrappers remain outside the supported slice. The deeper trial budget does not justify extra abstractions or commercial services.
