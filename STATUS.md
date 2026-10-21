# Scope and evidence

Draft 0.2, 21 October 2026. A specification kit with zero product runtime code or package dependencies. Isolated implementation-trial code is separate from this package.

## Available

- Six contracts: identity/session recovery, personal/shared ownership, customer-owned connections/reconnection, background processing/business progress, subscriptions/access and management-screen mapping.
- Logical relationship diagrams, workflow-local field guidance and conditional recovery information.
- A short bridge-plan template with observed/proposed/unresolved mappings and requirement-to-operation checks; examples for both a global personal mailbox app and an already-structured notes app.
- A self-contained instruction-only skill with one documented project-local loading path. Contributor instructions are separate from consumer guidance.
- Standing agent instructions preserving native architecture and limiting additions to demonstrated gaps.
- MIT license and the supplied AppLift logo.

The docs are intended to save host-mapping decisions rather than replace provider SDK instructions. No mandatory schema, Store interface, role system, ORM or code generator is supplied.

## Evidence and limits

Author review checked field authority, relationship/workflow consistency, optional storage and recovery paths. Relative documentation links and image references were checked locally. The worked example is hypothetical and was not executed. Mermaid source is supplied; a successful rendering test is not claimed.

One fresh-context implementation attempt passed for a representative global personal Node/SQLite backend with local provider simulators: [evidence and reproducible fixture](evidence/private-customer-trial.md). Seven implementer checks and nine held-out evaluator scenarios passed without maintainer engineering correction. The test used the explicitly supplied public kit; it does not demonstrate organic discovery, implicit skill activation, reduced effort, broad compatibility or production readiness. Live provider acceptance remains separate.

Skill frontmatter/name and relative-reference checks passed, and its installed project-local copy was unchanged during the attempt. The bundled skill validator could not run because its Python environment lacked PyYAML; no validator pass is claimed. Explicit path loading was exercised, not automatic discovery.

## Stopping rule

The planned bounded implementation attempt has completed. Its business choices and local provider interfaces were supplied in the host README; no additional business clarification or author engineering rescue was reported. A plan-only result would have supported mapping quality only. This result executes actual SQLite migration, service guards, imports, queue recovery and search in one fixture, while keeping external-provider behavior simulated.

The submitted implementation preserved old IDs, data and user-managed progress and passed the affected private-access/background checks on first evaluation. Stop here unless another concrete host or observed failure justifies more work. Do not turn one success into a generalized compatibility claim or restart broad benchmarks/provider certification.

## Conditional scope

Connections and background ownership are now included because the personal-email-app transition requires them. Uploads, marketplaces, enterprise access systems, general workflow engines and additional provider wrappers remain outside the supported slice. The deeper trial budget does not justify extra abstractions or commercial services.
