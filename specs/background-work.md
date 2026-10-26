# Customer-owned background work and preserved business progress

Use when importing, processing, indexing or retrying continues without a logged-in user, or when a save should return before derived work finishes. Reuse existing schedules, workers, transactions and services. A background worker needs resolvable authority; a browser session is not its durable ownership context.

## Minimum logical model and information

An existing **connection or parent resource identifies the owner** of the imported source record. Existing work refers to that context; the resulting business record and search/index entries remain within the same boundary. A job or owner field at every step is not mandatory. See [models](../MODELS.md#connections-and-background-work).

| Information | Authority / simplest source | Needed behavior |
| --- | --- | --- |
| Owner context | Trusted connection/parent association | Resolve the correct customer during ingestion, processing, writes, retries, search and export; never infer it from the worker process's default account. |
| Stable source identity | Provider source reference within its account/connection namespace | Recognize the same import on replay. A message ID without its account namespace may collide across customers. |
| Business-record relationship | Existing link from source/import identity to requisition/job | Find and update the same business record while preserving app IDs. A native unique key/upsert can replace a new dedup table. |
| Imported facts versus user-managed state | Provider owns source facts; app user owns lifecycle fields | Decide what replay may update. Explicitly distinguish imported subject/body/source timestamps from fulfillment status, manual notes, assignments and completion dates. |
| Operation identity and outcome | Existing queue/task/store when work can be interrupted | Retry or inspect the same intended operation; retain enough status to avoid lost work. No new queue or event log by default. |

**Invariant: reprocessing a source must not reset business progress.** Replaying a fulfilled requisition cannot turn it back into new. Update only imported fields that are actually authoritative and current; preserve user-managed fields unless an explicit authorized business action changes them. If a user can edit a normally imported field, establish its override/conflict rule instead of overwriting it on the next sync.

**Source content is data, not authority.** Emails, messages and documents may contain indirect prompt injection. Keep their text separate from agent/worker instructions; extracting facts or summarizing it does not authorize embedded commands. The same boundary applies to derived summaries and search results. Resolve owners, credentials, permitted actions and export destinations from trusted host bindings and the authorized workflow, never source instructions. Validate extracted values before native operations; a prompt warning alone is not an access control.

## Workflow contract

| Operation | Required connection | Ordinary failure / repeat behavior |
| --- | --- | --- |
| Enqueue or schedule | Derive connection/parent context from an authorized action or trusted existing schedule. | A forged job payload cannot select another owner's resource or credentials. Preserve stable correlation across retries. |
| Fetch and process | Resolve current ownership, account and usable authority; obtain this connection's source data. | Temporary errors may retry within a bound; invalid grant stops affected work and exposes reconnection. Other customers continue normally. |
| Commit result | Recheck relevant authority and target identity at the native mutation boundary. | Disconnect/reassignment while fetching cannot authorize a stale result. Use existing transaction/conditional mechanisms; avoid holding a database transaction across a remote call. |
| Replay import | Match namespaced source identity; create missing business record or update allowed imported facts. | Converge on the same result without duplicate requisitions, lost manual notes or lifecycle rollback. Use native uniqueness/atomicity where competing workers can race. |
| Index / list / search / count / export | Resolve the result's actual owner, including through its parent; scope the enforcing operation. | Indexes and browser filtering alone do not authorize results. Carry ownership through separate indexing services or enforce it at retrieval. Recover stale indexes from authoritative records. |
| Resume interrupted work | Inspect the existing operation/result and current connection authority. | A failure between database commit and acknowledgement must be safe to replay. External irreversible effects need provider-supported idempotency or a retained effect result; do not promise exactly-once execution. |

For an external account change, do not relabel existing imported data as belonging to the new account. Keep stable source identity/history and apply an explicit replacement/import policy. Resolve new authorization independently of old queued work.

For chargeable work, recheck eligibility at execution before side effects. Follow the [lifecycle defaults](lifecycle.md) when access or credits recover: publishing-like backlogs require explicit resume by default; harmless retries may follow the host's agreed automatic policy.

## Persist first, then enrich the entity

Concrete transition: a person saves authored content and receives confirmation while assessment, classification or indexing finishes separately. This contract separates persistence from derived work without adding an AppLift runtime, event log or general job model. Apply only the affected stages; explicit assessment can remain a separate action if automatic processing is not promised.

**A plain save validates, authorizes, commits and returns.** Keep input checks, current ownership/account/plan guards and optimistic concurrency at the native mutation boundary. Commit user content without waiting for AI, optional enrichment, publication or notification. Keep the transaction's reads/writes limited to the changed invariant; no unrelated collection scan for an ordinary text edit. Return the committed entity/version and applicable follow-up state in the same mutation response. A correctness-required readback is acceptable; a complete workspace reload must not gate save confirmation. Replaying a timed-out creation uses the same owner-scoped command/entity identity; the same command with different input must not silently become a second write.

Keep the acknowledgements truthful:

| State | Evidence required |
| --- | --- |
| Local saved | Content retained on the device under the host's local durability policy; server persistence may still be pending. |
| Server persisted | Backend content commit succeeded. A lost response leaves the client's outcome uncertain until retry/read resolves it. |
| Enriched | Derived output matches the current entity and relevant input revision. Old scores/rationales are stale; missing results are pending/unknown, never fabricated success. |
| Published / sent | An external effect receipt establishes the outcome under the host/provider contract. Acceptance of a command alone is insufficient. |

**Accept follow-up durably.** If automatic work is promised, persist content and recoverable work intent atomically before acknowledging the save. Existing entity pending state and an existing worker/scheduled scan can suffice. A transactional delivery mechanism or existing outbox can also suffice; choose from the host. If queue dispatch happens after commit, a durable pending marker plus recovery scan must close the crash gap. If a notification arrives before commit, the worker must verify committed intent before processing. Unawaited promises, timers and process memory cannot be the only work record. Identify the actual wake-up and recovery path; a scheduler that never discovers this pending state is insufficient.

Resolve only information the host needs: target and owner through existing parents; input revision through existing versions or a fingerprint; and recoverable outcome/claim through existing work or entity state. Add storage only for a demonstrated missing fact. An entity revision alone may be too broad if derived writes change it: identify the authored content/media and relevant prompt/config versions that actually determine the result, including entity incarnation if IDs can be reused after deletion.

| Stage | Guarantee and ordinary recovery |
| --- | --- |
| Select work | Coalesce to the latest desired revision per entity when intermediate results are unnecessary. An edit marks affected derived output stale and leaves new work discoverable; it does not reset unrelated manual progress. |
| Claim | Atomically claim the entity/revision/stage with a bounded lease and fencing token or equivalent conditional authority. An expired claim can be reclaimed; its old worker cannot later commit success, failure or status over its replacement. |
| Execute | Resolve current owner, target, connection and chargeable eligibility. Run remote work outside retryable database transactions. Order only actual dependencies: classification and assessment can be independent; an explanation consuming ratings waits for that exact assessment. Generation/polish loops retain their real dependencies and bounds. |
| Commit | Recheck current authority, input revision and claim using native conditional writes/transactions. Apply only the intended derived fields; automatic enrichment cannot silently rewrite authored content or manufacture approval. Superseded output is discarded without marking newer work complete/failed. Preserve the host's content-edit approval rules. |
| Retry / stop | Duplicate delivery converges on the same intended result. Retry transient failures with bounded backoff and attempt/time limits; reuse valid completed stages. Invalid input, lost eligibility or invalid connection stops/pauses affected work with a safe reason and an authorized retry/reconnect action. Retried stages must still match their inputs. |

Expose pending, running, completed, failed or paused meaning through existing entity/operation status as applicable; these are outcomes to distinguish, not mandatory new columns or a state-machine framework. A worker crash and terminal failure must not leave an invisible permanent spinner. Keep accepted content intact when enrichment fails. Result idempotency does not prevent duplicate remote computation/charges after a crash; use supported provider idempotency where available and bound retries. Do not promise exactly-once execution.

Long work must not monopolize the only request slot or owner-wide lock needed for plain saves. Reuse the host's delivery/capacity controls, bound work per turn and avoid starvation across entities/owners. Inspect actual contention before changing concurrency; preserve deletion safety and justify custom settings rather than prescribing an instance count.

### Publication and other external effects

Keep publication separate from persistence/enrichment. Bind its durable intended effect/claim to the approved content and destination version. Recheck current approval, owner/account/deletion state, connection, eligibility and pause/resume policy before sending; enqueue-time permission is insufficient. Preserve existing provider validation and receipt mechanisms. A version change before sending invalidates the old intent according to the host's approval rules.

Reuse the same intended effect identity with provider-supported idempotency. After a timeout that may have sent, inspect/reconcile the receipt before repeating. If no safe provider recovery exists, expose an uncertain outcome for authorized review rather than blindly send again. Revocation cannot retract a call already issued; stop subsequent effects and apply the host's receipt/recovery policy. Do not report Published while merely queued, or automatically publish a missed backlog when access recovers; see [lifecycle defaults](lifecycle.md).

### Measure the save boundary

A latency goal belongs to the host and chosen conditions. For example, a requested **200 ms server-processing goal** is a target to measure, not an AppLift guarantee or a replacement for server persistence with a local acknowledgement. Name the boundary and percentile before claiming it is met. Measure authenticated command entry through durable content/intent commit and response serialization, including authorization/projection reads, required readback and DB retries. Separately measure any authentication before that boundary, platform queue/startup, external entitlement refresh, network/preflight and client confirmation; also report total request and click-to-confirm time where available. Excluded phases must remain visible.

Report sample count and distribution for warm instances with fresh entitlement, stale-entitlement/refresh paths, cold starts, and saves concurrent with long work. A warm average or a few historic access-log durations cannot establish a maximum/p95. Instrument only the phases needed to find the actual delay; no observability platform is required. See [subscription enforcement](subscriptions.md#enforce-access-without-repeated-provider-reconciliation) for keeping access checks bounded without bypassing policy.

### Checks for a save/follow-up change

- Hold AI/publication/notification calls unresolved: plain save still commits and responds with the entity/version. With valid fresh entitlement, ordinary save performs no billing-provider reconciliation. Required validation, access checks and concurrency conflicts still apply.
- Crash after content/intent commit before dispatch and after result commit before acknowledgement: work is recovered and duplicate delivery converges. Retry a creation after losing its response: no duplicate entity or changed-payload replay.
- Race an edit/config change, duplicate worker, expired lease and slow old worker against both success and failure: no stale result/status overwrites newer input/work. Current work remains discoverable.
- Exercise two owners with colliding external/work IDs, forged target context, deletion and authority/eligibility revocation during work: no cross-owner access, stale commit or later unauthorized effect. Stop only affected work.
- Fail assessment, exhaust retries and restore eligibility/connection: saved content survives; status and safe recovery are observable. Publication uncertainty cannot duplicate a send or silently resume a paused backlog.
- Measure the declared save boundary under warm, cold, refresh and long-work contention conditions. Record actual results and unrun cases; documentation alone validates no latency or runtime behavior.

## Handoff and essential checks

Identify actual importer, worker, business writes, index/search query and any direct/export path. Record which fields the source may update and which business progress must survive. Test the existing lifecycle with duplicate input, a post-commit retry, two customers with the same external source ID, and revocation during processing. Check only the paths affected by the requested transition; retain working unrelated behavior.

Include one adversarial source alongside ordinary input: extraction/summarization still succeeds, while embedded instructions cannot switch credentials, cross ownership, trigger unauthorized effects or change an export destination. Check the affected tool/backend boundary, including replay; see the [mailbox example](../examples/personal-mailbox-app.md#consequential-requirements-and-observable-results).

If the host has no identities/ownership yet, mark the new associations as proposed and obtain the original-owner decision before exposing existing data. Use [connections](connections.md) for account consent/reconnection and [ownership](ownership.md) for private/shared access. No AppLift worker runtime is required.
