---
title: "How Do Agents Perform Code Optimization? An Empirical Study"
slug: "code-optimization"
category: "refereed-conference-publications"
date: 2026-04-13
venue: "Proceedings of the 23rd International Conference on Mining Software Repositories (MSR '26)"
authors:
  - "Huiyun Peng"
  - "Antonio Zhong Qiu"
  - "Ricardo Calvo"
  - "Kelechi G. Kalu"
  - "James C. Davis"
pages: "732-736"
doi: "10.1145/3793302.3793564"
paperUrl: "https://dl.acm.org/doi/pdf/10.1145/3793302.3793564"
---

Performance optimization is a critical yet challenging aspect of software development, often requiring a deep understanding of system behavior, algorithmic tradeoffs, and careful code modifications. Although recent advances in AI coding agents have accelerated code generation and bug fixing, little is known about how these agents perform on real-world performance optimization tasks. We present the first empirical study comparing agent- and human-authored performance optimization commits, analyzing 324 agent-generated and 83 human-authored PRs from the AIDev dataset across adoption, maintainability, optimization patterns, and validation practices. We find that AI-authored performance PRs are less likely to include explicit performance validation than human-authored PRs (45.7% vs. 63.6%, p = 0.007). In addition, AI-authored PRs largely use the same optimization patterns as humans. We further discuss limitations and opportunities for advancing agentic code optimization.
