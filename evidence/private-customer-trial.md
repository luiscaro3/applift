# One independent implementation attempt

21 October 2026. **Passed for one representative Node/SQLite backend with simulated providers.** This demonstrates a bounded implemented case, not live OAuth acceptance or measured effort savings.

## Starting condition and task

The author-created personal campaign fixture had global data, one mailbox, an existing queue and search projection, fulfilled requisitions and manual notes. It had no users or access guards. Its original single-user behavior passed before the attempt.

A fresh agent (6.1 sol low, no inherited author conversation) received an ordinary request to let other customers use it privately with their own mailboxes while preserving completed work. It received the frozen host, business choices and public AppLift revision [`c6154de`](https://github.com/luiscaro3/applift/tree/c6154de4fc901ac4d4f173c8f368923221a53ddb). The skill was explicitly supplied at a project-local path; organic discovery and implicit activation were not tested.

## Observed outcome

The agent implemented the backend transition and its tests. It retained existing IDs and tables, derived record ownership through a customer-owned connection, delegated session verification to the fixed simulator, and preserved business progress during import upserts. It added users/connections, consent correlation and the required queue context without an AppLift runtime, team system or role engine.

Seven implementer tests and nine separately authored evaluator scenarios passed. The evaluator's behavior criteria were fixed before dispatch and withheld. Concrete API calls were adapted after submission to the implemented service interface. No engineering correction was supplied by the maintainer; the first submitted implementation passed these checks. No additional business clarification was requested beyond the supplied business choices.

| Checked behavior | Observed result |
| --- | --- |
| Convert an actual database created by the frozen baseline | Existing IDs, source links, fulfillment, notes and completion times retained; unrelated first signup starts empty. |
| Private list/detail/search/count/update | Verified actor required; another customer's IDs or forged context do not expose/change their records. |
| Same message ID in two mailboxes | Separate correctly owned requisitions and scoped search results. |
| Duplicate import and changed source facts | Same business ID; imported subject/body refresh while fulfillment/manual progress remains. |
| Database commit followed by lost acknowledgement | Replay neither duplicates the record nor undoes progress changed by the user between attempts. |
| Disconnect/reconnect while an old fetch returns | Old result cannot commit; newly authorized same-account work can proceed. |
| New external account and queued old work | Old history keeps its original association; another customer cannot claim the connection. |
| Revoked grant / temporary failure | Reconnection state is local to the affected connection; temporary retries are bounded and can later resume. |
| Reopen persistence and frozen boundary | Actor mappings/progress persist; provider simulator and supplied kit were not modified. |

## Inspect or reproduce

The optional [fixture archive](private-customer-trial.zip) contains baseline/candidate source, tests, protocol, predeclared criteria, execution output and reproduction instructions. It is test evidence, not code consumers must install or conform to. See its REPRODUCE.md; Node v24.19.0 is the tested runtime and no dependency install is needed.

## Limits and stopping rule

This was one representative fixture created by AppLift's author, not a naturally evolved production application. Fixed local simulators supplied verified sessions, account/grant claims and mailbox replies. Live Google/mailbox consent, provider token refresh/revocation, protected credential storage and production approval were not validated. No browser/HTTP UI, billing transition, distributed-worker guarantee or multi-provider compatibility was tested. The engineer-owned migration setup assumed a proven founder identity supplied in the brief.

The result establishes that this explicitly supplied kit could support this agent completing this service-boundary transition without maintainer engineering rescue. It does not establish causation, reduced effort, organic discovery or a universal selection advantage. The bounded check passed; further scope should follow an observed need rather than expanding the test program automatically.
