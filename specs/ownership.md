# Private data or shared workspaces

Use when a personal app becomes usable by multiple people. First decide whether they need **separate private data**, **shared team data**, or deliberately public data. Multiple users alone do not imply teams.

## Minimum logical model

Private: **User -> Existing resource**, one owner per protected resource. Shared: **User -> Membership <- Workspace -> Existing resource**. Each membership binds one user to one workspace; one pair has at most one current membership. Each protected resource belongs to one selected workspace, directly or through its parent. A workspace must be an existing team/account/project boundary where possible. See [diagrams](../MODELS.md#ownership).

Membership carries only permissions the actual operations need. Reuse host roles; do not install fixed AppLift roles. If the app offers owner-controlled administration, define how the last administrator is preserved or how an intentional closure works. Public/shared links are explicit separate grants, not missing-owner records.

## Map to the host

### Minimum information

| Information / meaning | Authority and simplest source | Needed when / workflow it enables |
| --- | --- | --- |
| `resource_id`: stable existing record key | Existing host record | Addresses the same record before and after the transition; retain links and references. |
| Owner reference: user or workspace allowed to control the resource | Trusted existing relationship, document path or parent; otherwise a host-assigned reference | Private reads/writes/aggregates need a resolvable boundary. Choose personal or shared ownership; no generic `owner_type` system is required. |
| `user_id` + `workspace_id`: membership pair | Existing host sharing model | Only shared work needs membership lookup. Reuse existing team/account IDs; the pair itself may identify the membership. |
| Role or permission information | Existing permission rules plus current membership where applicable | Only operations with differing permissions need a distinction. A uniform member policy can be code/configuration; do not add a role column or new role engine automatically. |
| Version/revision | Existing database or host concurrency mechanism | Only writes that must reject stale edits need it. Reuse native revisions/conditional writes; do not add a generic version field to every record. |

An owner inherited from a trusted parent needs no duplicate owner column on every child. If old data lacks a provable owner, identify the assignment decision before exposing it; guessing ownership is not a schema shortcut.

| Choice | Relational mapping | Document mapping |
| --- | --- | --- |
| Personal | Existing resource owner foreign key to existing user | Owner reference on existing document, or authorized user-owned path |
| Shared | Existing workspace foreign key; membership pair uniqueness | Workspace-owned path/reference; native membership lookup |
| Child resource | Follow trusted parent ownership; don't duplicate it without need | Authorize through parent/path; validate parent assignment |

Choose the actual enforcing layer: row policies, document rules or authorized backend operations. Firestore server/Admin SDK paths bypass client Security Rules and need their own access checks. Never accept a caller's arbitrary owner ID as authority.

## Workflow contract

| Trigger / actor | Authority and commit | Repeat or failure / user outcome |
| --- | --- | --- |
| Existing data becomes private/shared | Map existing records to the proven current owner/workspace; retain IDs and relations. Preview assignment before migration. | Ambiguous ownership blocks that record's exposure until resolved. Preserve a reversible mapping/change record appropriate to the migration. |
| Actor lists, reads, creates or changes data | Verify actor and current permission; scope query including counts/search; validate parent/child owner consistency. Derive creation owner from authorized context. | A different owner's ID is denied. Never fetch broadly and rely on browser filtering. |
| Actor makes a sensitive write | Couple permission and target-state checks to the write using the native transaction/conditional-write boundary where races matter. | Revocation/conflict before commit must not permit a now-unauthorized write. Don't invent a separate transaction framework. |
| User switches workspace | Verify membership and reset/reload private caches, selections and pending requests for that context. | Late responses cannot populate the new workspace screen. |
| Authorized manager changes membership | Recheck manager permission and affected membership; enforce any last-admin rule within the native mutation boundary. | Repeat removal is harmless; removed users lose future authorized operations. Clear access UI on denial. |

## Handoff and essential checks

Name the ownership choice, old-data assignment, actual guard and affected list/detail/write/aggregate operations. Check two users cannot read or alter each other's private data, invalid parent references fail, and old IDs still resolve for their rightful owner. Add a revocation/conflict check only for the sensitive writes this integration promises. Preserve existing public behavior explicitly rather than converting all records to private by assumption.

Official boundary references: [row-level security](https://supabase.com/docs/guides/database/postgres/row-level-security), [Firestore rule conditions and server-client boundary](https://firebase.google.com/docs/firestore/security/rules-conditions).
