# Existing-host subscription pilot: assisted candidate evidence

Updated 22 October 2026. An independently developed Scout source export was used in an isolated copy. The coordinator selected a workspace-subscription scenario; this was not an external adopter or demonstrated commercial demand.

A fresh agent received an ordinary business request without naming AppLift. It found the installed public kit through project-file discovery and read the skill, subscriptions, ownership and bridge-plan documents. This is observed resource selection; native implicit activation and internet discovery were not established. Supplied kit revision: `c68b75e22555ab78685ff82a0deabc163bb31fd9`.

The candidate reused existing Account membership, IDs and Firestore references. It prepared paid Ideas mutations, unpaid reads, provider reconciliation and small Profile controls without an AppLift runtime or new identity/role/database framework. Seven existing source/manifest files changed and one billing file was added. No original working application, credentials or deployment was changed.

Backend and changed-frontend typechecks reported zero diagnostics; 13 focused synthetic scenario groups and retained client/command checks passed on Node 22.21.1. Tests exercised actual host functions/router/transport with an in-memory database, provider stubs and SDK-generated test signatures. No real provider delivery is implied.

**Two maintainer engineering corrections were needed:** remote Stripe reads initially occurred inside a retryable database callback; review also removed an unnecessary Checkout expiry override in favor of the provider default. Relevant checks passed afterward. The first finding exposed a missing explicit boundary in the subscription guidance; the maintained spec now states that provider reads stay outside retryable transactions and local commits recheck native context/version. The installed trial snapshot remained unchanged.

After separate explicit approval, four checks passed against the actual Firestore 1.22.0 emulator in an isolated Linux container on Node 22.21.1: paid-write/unpaid-read and workspace/member boundaries; projection-conflict reread outside retryable callbacks; stale-edit rejection; membership revocation before commit. Stripe replies remained synthetic. External networking was disabled, no ports or credentials were supplied, and the container was removed. The earlier Windows emulator loopback failure was not retried or bypassed. No further integration-code correction was needed for this run.

The backend dependency lock was updated for Stripe. Clean frozen installations and normal backend (`tsc`) and frontend (portable `vinext`) builds passed on Node 22.21.1 / pnpm 11.25.0. The frontend lock stayed unchanged; its build emitted a large-chunk warning. Original build inputs omitted by initial source filtering were restored from the frozen archive for these checks; seed scripts were compiled, not executed. This repairs trial preparation, rather than adding another integration-code correction.

The second correction also informs a general consumer/contributor rule: preserve native/provider defaults unless a concrete requirement justifies an override, and state the reason for each custom setting. Both lessons should guide the next ordinary adoption attempt; no artificial repeat trial is required merely to improve the report.

Browser rendering, production Firestore and live Stripe acceptance remain unverified. Earlier Stripe sandbox results belong to their original host and are not transferred to this implementation. Private host code and raw local logs are not published with this summary.

This is a maintainer-assisted local result, not successful unaided integration or a completed real-provider pilot. Token cost/savings were not measured. No broad compatibility, production readiness or causal benefit is claimed. Further work should follow a concrete adopter need and approved setup, not expand the test program to remove every qualification.
