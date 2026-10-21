# Why this kit exists

AppLift helps an agent bridge existing app architecture and new service-backed workflows. Its useful output is a small host-specific plan: what to reuse, which relationship is missing, where authority is enforced, and how ordinary failure recovers. It is a product hypothesis, not a measured productivity claim.

The project began with runtime and adapter experiments. Those are retired from the recommended path: this repository has no runtime dependency and does not require their APIs, roles, test harnesses or provider setup. Earlier guided integrations informed the contracts but do not demonstrate independent agent adoption. Historical audits, original roadmaps and private host evidence are retained separately by the maintainer; they are not this repository's backlog or requirements.

## Evidence informing scope

- [Lovable's Build Economy summary](https://lovable.dev/blog/a-first-look-at-the-build-economy) describes a substantial nontechnical audience and monetization intent on its platform. It is not a representative census of all MVPs.
- [Stack Overflow's 2025 AI survey](https://survey.stackoverflow.co/2025/ai) identifies nearly-correct output and debugging as common respondent frustrations. It does not measure AppLift's benefit.
- [RevenueCat's subscription report](https://www.revenuecat.com/state-of-subscription-apps) demonstrates the importance of subscription lifecycle and payment recovery in its app population; it does not rank web-app feature demand.

These signals motivate the initial scope. Official mechanism references live beside the relevant workflow in each spec. Neither the research nor the previous implementation experiments prove a universal feature ranking, provider compatibility or an LLM preference for this kit.

See [current scope and evidence](STATUS.md) for what is delivered and what remains unvalidated.
