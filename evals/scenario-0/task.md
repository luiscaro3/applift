# Add private access to an existing notes app

Write PLAN.md for adding managed-provider sign-in to this existing app. This is a planning task: do not deploy, call providers, install dependencies or implement an app. Include concrete affected operations, unresolved product choices and acceptance checks. Preserve the app's IDs, data and behavior. Customers work individually.

The inspected host currently has:

```text
users(id TEXT PRIMARY KEY, display_name TEXT)
projects(id TEXT PRIMARY KEY, owner_id TEXT REFERENCES users(id))
notes(id TEXT PRIMARY KEY, project_id TEXT REFERENCES projects(id), body TEXT)
```

The founder is existing user `u-founder`; all existing projects belong to that user. Other user IDs already appear in audit records, so replacing user IDs would break those references. The selected managed auth provider supplies verified `(issuer, subject)` and contact email through its SDK; its IDs differ from local IDs. Signup is open to new individual customers. The SDK owns sessions and recovery. There is no account-linking feature.

Routes `listProjects(actor)`, `getNote(actor, noteId)` and `editNote(actor, noteId, body)` currently trust a development actor selector. `requireOwnedProject(actor, projectId)` already exists and checks `projects.owner_id`. `searchNotes(actor, query)` currently searches every note. The browser stores cached note results and supports logout/account switching. Signup is free; billing is not requested.

Show how returning sign-in resolves the same local actor, existing records stay assigned correctly, and private note reads/edits/search remain private. Explain what happens on an expired/revoked session and account switching. Give checks an implementer can execute, and state which have actually run.
