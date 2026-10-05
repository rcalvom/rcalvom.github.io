---
title: "AutoSOUP: Safety-Oriented Unit Proof Generation for Component-level Memory-Safety Verification"
slug: "autosoup"
category: "refereed-conference-publications"
date: 2026-05-11
venue: "the 33rd ACM Conference on Computer and Communications Security (CCS '26)"
authors:
  - "Paschal C. Amusuo"
  - "Ricardo Calvo"
  - "Dharun Anandayuvaraj"
  - "Taylor Le Lievre"
  - "Kevin Kolyakov"
  - "Elijah Jorgensen"
  - "Aravind Machiry"
  - "James C. Davis"
status: "forthcoming"
pages: "13"
doi: "10.48550/arXiv.2605.10712"
preprintUrl: "https://arxiv.org/pdf/2605.10712"
---

Memory-safety errors remain a persistent source of zero-day vulnerabilities in low-level software. The problem is especially acute in embedded systems, where hardware protections are often limited and dynamic analysis is difficult to apply effectively. Memory-safety verification can provide stronger assurance by proving the absence of such errors or exposing violations when they exist. However, current verification workflows remain largely manual and require substantial specialized expertise, limiting their adoption in practice. We present AutoSOUP, a system for automating component-level memory-safety verification through Safety-Oriented Unit Proofs. We formalize these unit proofs as artifacts that encode verification choices, including scope, loop bounds, and environment models, for verifying safety properties, and introduce three techniques for deriving them automatically. To overcome the limitations of existing automation approaches, we further introduce LLM-As-Function-Call, a hybrid architecture that combines deterministic program synthesis with LLMs to automate these techniques and produce justifiable unit proofs. We evaluate AutoSOUP by assessing its ability to automate memory-safety verification and expose vulnerabilities in verified components, and we characterize the assumptions and guarantees of the resulting proofs.
