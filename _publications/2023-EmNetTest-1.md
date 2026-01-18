---
title: "Systematically detecting packet validation vulnerabilities in embedded network stacks"
collection: publications
category: manuscripts
permalink: /publication/EmNetTest
#excerpt: ''
date: 2023-9-11
venue: '2023 38th IEEE/ACM International Conference on Automated Software Engineering (ASE)'
#slidesurl: 'https://academicpages.github.io/files/slides1.pdf'
paperurl: 'https://arxiv.org/pdf/2308.10965f'
#bibtexurl: 'https://academicpages.github.io/files/bibtex1.bib'
citation: 'Paschal C Amusuo, Ricardo Andrés Calvo Méndez, Zhongwei Xu, Aravind Machiry, James C Davis'
---
Embedded Network Stacks (ENS) enable low-resource devices to communicate with the outside world, facilitating the development of Internet of Things and Cyber-Physical Systems. Some defects in ENS are thus high-severity cybersecurity vulnerabilities: they are remotely triggerable and can impact the physical world. While prior research has shed light on the characteristics of defects in many classes of software systems, no study has described the properties of ENS defects nor identified a systematic technique to expose them. The most common automated approach to detecting ENS defects is feedback-driven randomized dynamic analysis (“fuzzing”), a costly and unpredictable technique. This paper provides the first systematic characterization of cybersecurity vulnerabilities in ENS. We analyzed 61 vulnerabilities across 6 open-source ENS. Most of these ENS defects are concentrated in the transport and network layers of the network stack, require reaching different states in the network protocol, and can be triggered by only 1–2 modifications to a single packet. We therefore propose a novel systematic testing framework that focuses on the transport and network layers, uses seeds that cover a network protocol's states, and systematically modifies packet fields. We evaluate this framework on 4 ENS and replicated 12 of the 14 reported IP/TCP/UDP vulnerabilities. On recent versions of these ENSs, it discovered 7 novel defects (6 assigned CVES) during a bounded systematic test that covered all protocol states and made up to 3 modifications per packet. We found defects in 3 of the 4 ENS we tested that had not been found by prior fuzzing research. Our results suggest that fuzzing should be deferred until after systematic testing is employed.
