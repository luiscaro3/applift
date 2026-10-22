# AppLift standing instructions

Read this before any work on AppLift. These instructions travel with the directory; future agents must receive them. Current user instructions take precedence.

## Purpose and scope ceiling

Help an LLM connect a requested capability to an existing app's entities, ownership and workflows with less design invention. Specs and logical data models are the product. Runtime code is optional and currently absent.

Before adding anything, name the concrete user transition and design decision it saves. If reading and adapting it costs more than using the provider's own instructions, simplify or omit it. Partial useful adoption is enough. Stop when the narrow outcome is clear; do not pursue exhaustive coverage or unmeasured perfection.

Describe needed relationships, authority and workflow guarantees; leave physical implementation and any necessary host repair to the consuming agent. Do not turn the kit into a general architecture repair manual or mandatory redesign process. One-contract adoption and the host's existing working notes are sufficient when they cover the requested boundary.

## Design rules

- Preserve native entities, IDs, data and guards. Each logical box must say whether it is reused, provider-owned, derived or genuinely missing. A box does not mandate a table.
- Treat field names as semantic examples. For each needed value, identify its authority and resolve it from existing data, provider state or derivation first. Add storage only for a demonstrated missing relationship or needed retained fact. Conditional recovery fields stay conditional; no default columns, mirrored provider records or separate field catalog merely for completeness.
- Choose private per-user ownership or shared ownership from the actual use case. Do not add teams, workspaces, roles or polymorphic owner systems by default.
- Pair relationships with ordinary workflows and recovery: trigger, authority, effect, repeat behavior and next action after failure.
- Reuse maintained auth, billing and delivery services. Explain their connection to host behavior. Do not build provider wrappers, a Store interface, ORM, generator, universal inference engine, custom DSL or new identity/payment infrastructure.
- Keep actual authorization at the host's enforcing boundary. UI visibility and successful payment redirects are not authorization.
- Use official documentation for provider mechanics. Do not duplicate rapidly changing API details in generic specs.
- Preserve native/provider defaults unless a concrete requirement justifies an override. State the reason for each custom setting; omit unnecessary configuration.
- Keep the entry point short. Read only the needed spec; historical roadmaps are evidence, not a backlog.

## Work and evidence

Separate maintaining this kit from using it in another app. These contributor instructions govern changes to AppLift; they do not replace the consuming host's instructions. The skill and selected specs supply consumer guidance. When implementation is requested, continue from the short mapping through implementation and relevant checks within that authorization; do not create an artificial plan-only stopping point.

Evaluate actual supported behavior. A plan-only trial demonstrates mapping quality; a successful implementation attempt demonstrates only its tested case. Keep simulated-provider evidence distinct from live provider acceptance. Record business clarification separately from maintainer engineering rescue. Do not claim measured savings, universal compatibility or production readiness without corresponding evidence.

Retire irrelevant code from the recommended path. Preserve historical evidence; no broad deletion or host cleanup is implied. Customer-owned connections and background processing are supported contracts because the personal-email-app transition needs them. Use the least engineering and tokens needed for the current outcome; reuse applicable partial work and evidence. A prior deeper trial budget is not standing permission for extra abstractions or speculative scope. Stop after the bounded attempt passes the relevant checks, preserving existing behavior without maintainer engineering rescue. Record any correction if that goal was not met. Fix observed failures before expanding.

## Protected boundaries

Preserve working host applications and use an authorized isolated snapshot for trials. Provider tests, credentials, endpoint exposure and deployment are separate activities. No spending or paid APIs/build/deploy without explicit budget approval. Credential creation/configuration and persistent access require exact security confirmation. Never write secrets to chat/files or reuse exposed credentials. Publication/push requires the user's authorization; a request to edit documentation alone does not supply it.

If work moves elsewhere, install these instructions at that workspace's applicable agent entry point; do not claim global enforcement. Do not spawn agents without authorization. Report actual changes, relevant checks and unresolved limits.
