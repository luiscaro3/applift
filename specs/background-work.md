# Customer-owned background work and preserved business progress

Use when importing, processing, indexing or retrying continues without a logged-in user. Reuse existing schedules, workers, transactions and services. A background worker needs resolvable authority; a browser session is not its durable ownership context.

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

## Handoff and essential checks

Identify actual importer, worker, business writes, index/search query and any direct/export path. Record which fields the source may update and which business progress must survive. Test the existing lifecycle with duplicate input, a post-commit retry, two customers with the same external source ID, and revocation during processing. Check only the paths affected by the requested transition; retain working unrelated behavior.

If the host has no identities/ownership yet, mark the new associations as proposed and obtain the original-owner decision before exposing existing data. Use [connections](connections.md) for account consent/reconnection and [ownership](ownership.md) for private/shared access. No AppLift worker runtime is required.
