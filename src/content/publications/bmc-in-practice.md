---
title: "Small Harnesses, Default Checks, Limited Coverage: Bounded Model Checking in Practice"
slug: "bmc-in-practice"
category: "other-works"
date: 2026-11-14
venue: "arXiv preprint arXiv:2611.19267"
authors:
  - "Kevin Kolyakov"
  - "Ricardo Calvo"
  - "James C. Davis"
  - "Paschal C. Amusuo"
status: "preprint"
pages: "13"
doi: "10.48550/arXiv.2611.19267"
preprintUrl: "https://arxiv.org/pdf/2611.19267"
---

The growing use of AI to generate software and verification artifacts has increased the need for automated systems that provide reliable software assurance. Bounded model checking (BMC) offers a practical foundation for such systems by automatically checking correctness and security properties directly on software. However, effective verification requires choices about properties, input assumptions, function models, and execution bounds that influence the guarantees obtained. Little systematic evidence exists on how practitioners make these choices, limiting the empirical foundation for developing automated verification systems.

We present an empirical study of BMC practices in open-source C and Rust projects using CBMC and Kani. Through LLM-assisted open coding, static analysis, and artifact execution, we characterize verification properties, artifact complexity, and verification outcomes. Our findings reveal diverse verification objectives and generally small harnesses, but also property-specification errors and extensive use of execution bounds and environment models. Most artifacts complete verification quickly and achieve high coverage within their scope, while repository-level coverage decreases with project size. Our findings and annotated dataset provide empirical baselines for verification automation and motivate improved techniques for property validation, harness generation, and scaling verification breadth.
