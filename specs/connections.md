# Customer-owned connections and reconnection

Use when each customer connects an external mailbox, calendar or similar service. App sign-in identifies the actor; service consent authorizes an external account. One does not substitute for the other. Reuse the host connector and maintained provider SDK.

## Minimum logical model and information

An existing **user or workspace owns a connection**. The connection identifies the external account and the approved grant used to access it. Existing imported records can inherit ownership through that connection. These are meanings, not required new tables; see [models](../MODELS.md#connections-and-background-work).

| Information | Authority / simplest source | Needed behavior |
| --- | --- | --- |
| Connection reference and owner | Trusted host association to the existing user/workspace | Resolve who may connect, use, disconnect and see imported results. Reuse an existing integration record if present. |
| Provider namespace and stable account identity | Verified provider response, scoped to its service/environment | Distinguish accounts; email/display name alone cannot justify reassignment. |
| Granted capabilities/scopes | Provider grant or connector's existing verified state | Know whether the requested operation is authorized; request only what that operation needs. |
| Credential reference | Existing protected secret/connector store | Select this connection's authorized grant. Never expose credential values in models, browser responses, job payloads or logs. |
| Usability / reconnection state | Current provider result plus deliberate host disconnect state | Distinguish usable, temporary failure, reconnection required and disconnected. Avoid duplicating the provider's entire state machine. |

An expiry value is needed only if the chosen SDK requires the host to manage refresh timing. A connection/grant revision is needed only if the host needs it to reject stale callbacks/results. Native transactions or conditional updates may already provide the needed guarantee.

## Workflow contract

| Trigger | Authority and effect | Repeat, interruption and recovery |
| --- | --- | --- |
| Logged-in customer connects | Server binds supported consent/callback correlation to the authorized actor. Verify the returned account and grant before associating them. | Cancelled/expired callback grants nothing. Repeated callback resolves the same intended connection. Never attach an arbitrary callback account to a browser-supplied owner. |
| Host or worker uses connection | Resolve owner and the current usable grant from trusted host state; select credentials by that connection. | No fallback to the founder's global credential. An absent/ambiguous owner stops the affected work. |
| Access expires | Let the existing provider SDK refresh when supported and authorized. | Temporary failures get bounded retry. Revoked/invalid grant requires reconnection; repeated refresh cannot recreate consent. |
| Customer disconnects | Verify ownership, disable future use, revoke remotely where supported and appropriate; prevent pending/in-flight work from committing under the removed authority. | Local disconnect must remain effective if remote revocation is temporarily unavailable. Retrying cleanup must not reconnect it. |
| Customer reconnects | Verify current actor and the external account. Restore a same-account connection only under its ownership policy. | A different external account is an explicit new/replacement connection; never silently move another customer's records or reuse old-account results. Stale callbacks cannot undo a later disconnect. |

Define whether an external account may be connected by more than one app owner. Do not silently merge records by external account or message ID. For the common private-account slice, reject attempts to take another customer's existing connection. Only an explicit supported sharing model changes that rule.

## Existing personal setup and checks

Before admitting new users, inventory the global credential, polling schedule and already imported records. Assign them to the proven original owner using an explicit authenticated bootstrap/operator decision. Preserve source IDs, app IDs, links and business progress. Do not infer the founder from whichever stranger logs in first. New customers begin with no inherited private data or connection unless the product explicitly says otherwise.

Map [background work](background-work.md) and all reads/searches to that ownership. Check two customers' connections remain separate, failed refresh produces a usable reconnection path, disconnect affects only its owner, and delayed work cannot publish results after authority is removed. These checks validate the host slice; real consent and provider production setup require separate evidence.

Official mechanics: [Google server OAuth and refresh](https://developers.google.com/identity/protocols/oauth2/web-server). Use the chosen provider's current account, scope, revocation and production requirements; AppLift supplies no credential service or connector wrapper.
