# Sign-in, sessions and recovery

Use when an existing app gains sign-in or lacks a coherent return-to-app flow. Skip solved parts. External-service API consent is a separate connection, not the app session.

## Minimum logical model

**User** is the existing local actor. **Identity** is the provider's stable verified subject, namespaced by issuer/project as appropriate. Each accepted identity maps to exactly one user; a user may have multiple identities only if linking is supported. **Session** authenticates one user; the auth service may own all session storage. See [diagrams](../MODELS.md#identity).

Reuse the managed auth user ID as the local key when it already fits. An extra identity mapping exists only when the host ID differs or supported linking requires it. Email is contact information, not a safe automatic cross-provider account-linking key. Do not create an AppLift session store or token format.

## Map to the host

### Minimum information

Names below describe meanings, not required columns. Availability is required for the selected workflow; new storage is not.

| Information / meaning | Authority and simplest source | Needed when / workflow it enables |
| --- | --- | --- |
| `user_id`: stable local actor | Existing host user key, or managed auth user key already used by the host | Every authenticated operation needs a consistent actor; preserve existing IDs. |
| `issuer` + `subject`: namespaced provider identity, associated with `user_id` | Verified auth result plus trusted host mapping; a fixed issuer/project may come from configuration | Resolves repeat sign-in to the same user. Add a mapping only if the provider identity cannot already resolve the host user. |
| Authenticated actor and session validity/expiry | Supported auth verifier/session service; expiry alone does not establish validity | Protected requests and session restoration need the verifier's result. Reuse SDK refresh/rejection behavior rather than adding local token or session columns. |

Email/name are optional contact/display values, not identity keys. Add them only for a selected screen, communication or explicit signup policy; use the provider's verification information if that policy depends on verified email. Tokens, credentials and provider recovery records do not belong in this field mapping.

- Relational example: existing `users.id`; optional `identities(issuer, subject, user_id)` with unique `(issuer, subject)`. Sessions stay with the auth service unless the app already owns them.
- Document example: existing user document keyed by provider UID, or one deterministic identity mapping to the existing user document. Concurrent callbacks must resolve to the same user through the native uniqueness/transaction mechanism.
- Inspect login callback, session middleware, protected operations and browser restoration. Authentication establishes the actor; [ownership](ownership.md) supplies data permission.

## Workflow contract

| Trigger / actor | Authority and effect | Repeat or failure / user outcome |
| --- | --- | --- |
| User starts login | Supported provider SDK owns redirect, state/nonce and code verification appropriate to the flow. | Cancel returns to login without creating partial access. Preserve safe return location. |
| Verified callback arrives | Resolve stable identity. Reuse user; create only if signup policy allows it. Commit mapping and any required local user creation together. | Repeat resolves the same user. Existing-only signup rejects unknown identities. Linking requires authenticated proof under an explicit policy. |
| App opens / session expires | SDK restores or refreshes session. Backend verifies it and derives user ID; request body cannot select another actor. | Transient service failure offers bounded retry. Invalid/revoked session clears private context and requests sign-in; avoid redirect loops. |
| User signs out | Invoke provider-supported session invalidation/logout and clear local private caches. | Repeated logout is harmless. State whether logout affects this device or all sessions using provider capabilities. |
| User loses provider account | Provider owns account recovery. | Explain provider recovery route. App-owner recovery, if offered, requires a separate explicit proof process; never relink solely by matching email. |

Before redirecting after expiry, preserve unsent work only if safe; do not leak private drafts into shared browser storage or restore them to a different user. Sign-in recovery does not recreate revoked team membership.

## Handoff and essential checks

Name signup policy, chosen auth service, current user key, session validation boundary and private-cache reset points. Operator owns approved OAuth app/redirect configuration and consent. Verify repeat login keeps one user, altered/invalid session cannot access a protected operation, and expiry leads to refresh or usable sign-in recovery. These are implementation checks, not claims that this spec ran them.

Official mechanisms: [OIDC subject stability](https://openid.net/specs/openid-connect-core-1_0.html#ClaimStability), [Google OAuth web flow](https://developers.google.com/identity/protocols/oauth2/web-server), [managed session example](https://supabase.com/docs/guides/auth/sessions). Use the chosen service's current documentation.
