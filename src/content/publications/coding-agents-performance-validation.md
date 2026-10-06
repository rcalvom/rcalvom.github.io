---
title: "How Do Coding Agents Optimize Software and Report Performance Validation? A Large-Scale Empirical Study of Open-Source Pull Requests"
slug: "coding-agents-performance-validation"
category: "other-works"
date: 2026-10-02
venue: "arXiv preprint arXiv:2610.03969"
authors:
  - "Huiyun Peng"
  - "Ricardo Calvo"
  - "Kelechi G. Kalu"
  - "James C. Davis"
status: "preprint"
doi: "10.48550/arXiv.2610.03969"
preprintUrl: "https://arxiv.org/pdf/2610.03969"
---

Software performance optimization requires identifying bottlenecks and improvement opportunities, and empirically evaluating the effects and trade-offs across performance objectives. Autonomous AI coding agents submit performance-oriented pull requests (PRs) to open-source projects, yet it remains unclear whether these changes reflect established optimization practices and adequately substantiate their claimed value. Extending our MSR 2026 Mining Challenge pilot study of 407 performance PRs, we analyze a sample of 1,130 agentic and 1,130 human-authored performance PRs collected through June 2026. We compare adoption outcomes and patch characteristics between the two groups, and examine their optimization practices and validation behaviors. The results show that agentic PRs are merged less often than human-authored PRs (54.4% vs. 73.3%), but the two groups use similar optimization strategies and report validation at comparable rates. Agentic PRs rely more on static reasoning and less on benchmarks (46.1% vs. 57.2%), although benchmark use converges by the end of the study period. Agentic PRs also report validation for code-smell refactorings as often as for resource-targeting changes, whereas human-authored PRs do so less often. Across both groups, about half of validated PRs report no quantitative performance metric, and relevant trade-offs are rarely quantified. Agentic optimization practice has become increasingly similar to human practice, but the supporting evidence remains incomplete. Establishing whether agent-proposed optimizations are supported by rigorous, quantitative, and multidimensional evidence remains an important challenge. These findings motivate evaluation infrastructure and review criteria that measure intended effects and relevant costs rather than treating the presence of validation alone as sufficient.
