---
title: "Lessons from Mitigating False Positives in Google's OSS-Fuzz-Gen"
slug: "lessons-oss-fuzz-gen"
category: "refereed-conference-publications"
date: 2026-07-05
venue: "Proceedings of the 34th ACM International Conference on the Foundations of Software Engineering"
citation: "Paschal Amusuo, Dongge Liu, Ricardo Andres Calvo Mendez, Jonathan Metzman, Oliver Chang, James C Davis"
paperUrl: "https://dl.acm.org/doi/pdf/10.1145/3803437.3805205"
---

Fuzz testing is widely used in industry and open-source ecosystems, but its effectiveness depends on the quality of fuzz drivers that translate raw fuzzer input into valid function arguments. Automated fuzz driver generation reduces manual effort, but in practice often produces false positive crashes, especially for complex functions. We introduce OSS-Fuzz-Gen, an experimental system for agent-based fuzz driver generation. This paper reports our experience mitigating its false positives using two complementary strategies: constraint-based fuzz driver generation and context-aware crash validation against realistic program entry points. In our evaluation on 1,500 benchmark functions from OSS-Fuzz, these strategies filtered out more than half of crashes initially classified as program errors, at modest additional cost. We distill lessons for deploying LLM-based agents in large-scale fuzzing pipelines.
