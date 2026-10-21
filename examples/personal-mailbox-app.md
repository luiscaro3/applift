# From a global personal mailbox app to private customers

This is a proposed bridge for the harder starting condition, not a tested migration or a required schema. The app has global requisitions, one configured mailbox, a poller, processing jobs and a search index. It has no user model or access guard. Ordinary request: "Let other customers use this privately, without seeing my information. Keep our completed work."

## Business choices

Ask whether customers share work; assume separate private accounts for this example. The proven founder retains existing records and mailbox; new customers begin empty and connect their own mailbox. Reconnecting the same account retains its records; replacing the mailbox is an explicit choice. Fulfillment and manual notes survive imports. Billing is a separate requested feature, not an automatic addition to this transition.

Do not ask the founder how to propagate ownership, scope credentials or make retries safe. Inspect and design those connections using the selected contracts. Original-owner proof is an explicit bootstrap/operator step, never "first login wins."

## Inspect and map

| Mapping | Evidence status before inspecting a host | Change only if missing |
| --- | --- | --- |
| Sign-in -> existing/new local actor | Unresolved | Use managed identity directly or add the needed stable identity association. |
| Founder -> existing global data/credential | Proposed; requires proven original-owner decision | Retain IDs/lifecycle; establish one trusted association. Preview old-data assignment. |
| Customer -> mailbox connection -> imported message | Proposed | Reuse existing connector/import records; otherwise add the smallest recoverable relationship. Credentials stay in the existing protected service. |
| Imported message -> requisition -> search result | Unresolved until source paths are inspected | Follow existing source/business links where available; scope retrieval rather than add ownership columns everywhere. |
| Queued work -> current authorized connection | Unresolved | Preserve context through the existing job record; check current authority before writing delayed results. |

Once inspected, replace these placeholders with real paths and observed facts. Do not mistake this example for knowledge of the host.

## Consequential requirements and observable results

| Requirement | Host operations to identify | Result to check |
| --- | --- | --- |
| Other customers cannot see my data | List/detail/search/count/export and updates | A second user cannot retrieve or alter the founder's records through any affected operation. |
| Existing work survives conversion | Bootstrap/migration and existing fulfillment command | Existing IDs, links, manual notes and completion state are retained. |
| Each customer uses their mailbox | Connect callback, credential lookup, poller and worker | Two accounts, even with the same provider message ID, produce separate correctly owned results. |
| Revocation stays effective | Disconnect, pending tasks and commit boundary | One customer's disconnect blocks their delayed work without stopping another customer. Reconnection verifies account identity; stale results cannot cross an account replacement. |
| Re-import does not undo fulfillment | Import upsert and search refresh | Subject/body changes can refresh imported facts while fulfilled status, completion time and manual notes remain intact. Duplicate delivery produces no new requisition. |

Use native transactions/conditional writes for local effects and supported provider refresh/idempotency for remote mechanics. Existing job/index services remain in place. If no protected connection store or trustworthy original-owner assignment exists, record that concrete gap instead of inventing credentials or exposing data.

## What counts as evidence

A plan-only exercise can validate this mapping. An implementation attempt must run the affected operations and report observed outcomes. Local provider simulators can test the host boundary and recovery branches, but cannot prove real OAuth consent/refresh or production provider approval. A single successful isolated attempt demonstrates that case only; record business answers and maintainer engineering rescue separately.
