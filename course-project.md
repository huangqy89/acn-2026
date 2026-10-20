---
layout: page
title: Course Project
permalink: /course-project/
---

Build on one of the eight recommended papers below and develop your own **algorithm, design, or observation**. Your project must go beyond summarizing or reproducing the original paper: explain what is new and provide **experimental results or data** that support your contribution.

At the end of the semester, prepare a **5-minute presentation** on your improvement or extension to the original paper and an **8-page, single-column report**.

[Project requirements](#project-requirements) · [Final deliverables](#final-deliverables) · [Recommended papers](#recommended-papers)

## Project Requirements

1. **Identify a research question.** Explain the original paper's approach and identify a limitation, an untested assumption, or a new setting worth investigating.
2. **Make a contribution.** Propose a new or improved algorithm, extend a system design, or establish a new observation through measurements and analysis. Clearly distinguish your work from the original paper and its released code.
3. **Validate your contribution.** Use experiments or data to show why your design is reasonable or your observation is supported. Compare with the original method or an appropriate baseline under comparable conditions. A reproduction can establish the baseline, but it must lead to a new contribution.

## Final Deliverables

### 5-Minute Presentation

Focus on **your improvement or extension to the original paper** and the evidence supporting it. Briefly introduce the original work, then explain your research question, contribution, key experimental results, and main conclusion.

A suggested allocation is 1 minute for the background and problem, 2 minutes for your algorithm/design/observation, 1.5 minutes for experimental evidence, and 0.5 minutes for conclusions and limitations.

### 8-Page Report (Single Column)

Prepare an **8-page report in single-column format**. Clearly separate the original paper's contributions from your own work and cite the papers, code, and datasets used.

Suggested report structure:

- **Introduction and motivation:** the research question and why it matters.
- **Background and original paper:** the relevant approach, assumptions, and limitation being addressed.
- **Your contribution:** the new algorithm, design, or observation, with sufficient detail to understand the work.
- **Experimental methodology:** implementation, environment, datasets/workloads, baselines, metrics, and settings needed to reproduce the evaluation.
- **Results and analysis:** quantitative comparisons, explanations, and additional experiments that test the central claim.
- **Discussion and conclusion:** limitations, applicability, and the main takeaway.

## Recommended Papers

Choose one paper as your starting point and develop a well-motivated extension. Check the repository's setup and data requirements before choosing the experimental scope.

### 1. ServeGen — LLM Serving

**ServeGen: Workload Characterization and Generation of Large Language Model Serving in Production** · NSDI 2026  
[Paper](https://www.usenix.org/system/files/nsdi26-xiang-servegen.pdf) · [Code and data](https://github.com/alibaba/ServeGen)

### 2. SimAI — Networking for AI

**SimAI: Unifying Architecture Design and Performance Tuning for Large-Scale Large Language Model Training with Scalability and Precision** · NSDI 2025  
[Paper](https://www.usenix.org/conference/nsdi25/presentation/wang-xizheng-simai) · [Code](https://github.com/aliyun/SimAI)

### 3. Agua — AI for Networking

**Agua: A Concept-Based Explainer for Learning-Enabled Systems** · SIGCOMM 2025  
[Paper](https://doi.org/10.1145/3718958.3754341) · [Code and artifacts](https://github.com/NetSAIL-UCI/agua)

### 4. StarCDN — Satellite Communication

**StarCDN: Moving Content Delivery Networks to Space** · SIGCOMM 2025  
[Paper](https://doi.org/10.1145/3718958.3754345) · [Simulator](https://github.com/ConnectedSystemsLab/StarCDN-Simulator) · [SpaceGEN trace generator](https://github.com/ConnectedSystemsLab/SpaceGEN)

### 5. CellReplay — 5G/6G and Mobile Networks

**CellReplay: Towards accurate record-and-replay for cellular networks** · NSDI 2025  
[Paper](https://www.usenix.org/conference/nsdi25/presentation/sentosa) · [Code and traces](https://github.com/williamsentosa95/cellreplay)

### 6. 5G Mid-Band Landscape — 5G/6G and Mobile Networks

**Unveiling the 5G Mid-Band Landscape: From Network Deployment to Performance and Application QoE** · SIGCOMM 2024  
[Paper](https://doi.org/10.1145/3651890.3672269) · [Data and analysis artifacts](https://github.com/SIGCOMM24-5GinMidBands/artifacts)

### 7. CoActo — Edge Computing

**CoActo: CoActive Neural Network Inference Offloading with Fine-grained and Concurrent Execution** · MobiSys 2024  
[Paper](https://doi.org/10.1145/3643832.3661885) · [Code](https://github.com/Kmbin93/CoActo)

### 8. Pantheon — Edge Computing

**Pantheon: Preemptible Multi-DNN Inference on Mobile Edge GPUs** · MobiSys 2024  
[Paper](https://doi.org/10.1145/3643832.3661878) · [Code](https://github.com/PantheonInfer/Pantheon)
