# Introduction Chapter Outline

**Dissertation:** Increasing Efficiency, Efficacy, and Extensibility in Heterogeneous Agent Reinforcement Learning
**Author:** Brandon Hosley
**Document Purpose:** Comprehensive outline for writing the Introduction chapter
**Target Length:** ~8,000-10,000 words (20-25 pages)
**Last Updated:** January 30, 2026

---

## Executive Summary

The introduction chapter serves three functions: (1) establish the real-world motivation and urgency of the research problem, (2) frame the technical challenges that span all three contributions, and (3) articulate the unifying thesis that **representation design is as important as algorithmic architecture** for enabling efficient, extensible heterogeneous multi-agent reinforcement learning.

### Unifying Thesis Statement

> Training efficiency, heterogeneity handling, and deployment flexibility in HARL are fundamentally representational problems before they are architectural ones. Task structure and heterogeneity type determine optimal method selection, and good representational design yields robustness as a natural consequence.

---

## Chapter Structure and Logical Flow

### 1.1 Opening: The Promise and Challenge of Autonomous Multi-Agent Systems
**Suggested Length:** 1,200-1,500 words (~3-4 pages)
**Purpose:** Hook the reader with real-world motivation; establish urgency and relevance

#### 1.1.1 The Rise of Autonomous Swarms (500 words)
- Open with concrete applications: disaster response, search and rescue, ISR operations
- DARPA OFFSET program as proof of technical feasibility
- Replicator Initiative (2023) as policy signal of strategic importance
- Gap between demonstrations and deployment: cost, complexity, training inefficiency

**Key References:**
- `mohddaud2022` - Drone applications in disaster management
- `robertson2023` - Pentagon Replicator Initiative announcement
- `zotero-2656` - Hicks discusses Replicator Initiative
- `zotero-2835` - OFFSET Swarm Systems demonstrations
- `hambling2021` - Why militaries want drone swarms
- `rogers2022` - The Third Drone Age
- `kallenborn2024` - Swarm warfare implications
- `gerstein2024` - Emerging technology and autonomy (Rand study)

#### 1.1.2 The Training Bottleneck (400 words)
- Computational cost as the primary barrier to real-world deployment
- Sample complexity scales with team size and task difficulty
- The gap between controlled benchmarks and operational environments
- Transition to: why this is fundamentally a learning problem

**Key References:**
- `jin2025` - Comprehensive survey on deployment barriers
- `canese2021` - MARL overview highlighting computational costs
- `krouka2022` - Communication-efficient training
- `gronauer2022` - Multi-agent DRL survey

#### 1.1.3 Heterogeneity as the Core Challenge (400 words)
- Real swarms are not homogeneous: varying sensors, capabilities, roles
- Examples: mixed drone fleets, robotic warehouses, agricultural robots
- Preview that heterogeneity is both a requirement and a complicating factor
- Transition to technical framing

**Key References:**
- `rizk2019` - Cooperative heterogeneous multi-robot systems
- `calvo2018` - Heterogeneous multi-agent DRL
- `hoang2023` - Drone swarms
- `cao2012` - Overview of multi-robot coordination
- `amarasinghe2019` - Agricultural drone swarms
- `carbone2018` - Swarm robotics

---

### 1.2 Multi-Agent Reinforcement Learning: Foundations and Paradigms
**Suggested Length:** 1,500-1,800 words (~4-5 pages)
**Purpose:** Establish the technical framework; introduce key paradigms readers need

#### 1.2.1 From Single-Agent to Multi-Agent RL (500 words)
- Brief RL foundations: MDPs, policies, value functions
- Multi-agent formalization: Dec-POMDPs, POSGs
- The non-stationarity problem from single-agent perspective
- Game-theoretic foundations: Nash equilibrium, cooperative vs. competitive

**Key References:**
- `sutton2018` - Reinforcement Learning: An Introduction
- `littman1994` - Markov games framework
- `busoniu2008` - Comprehensive MARL survey
- `shoham2007` - If MARL is the answer, what is the question?
- `kaelbling1996` - RL: A Survey

#### 1.2.2 Centralized Training with Decentralized Execution (CTDE) (600 words)
- The paradigm: centralized information during training, local execution
- Benefits for coordination learning
- Actor-critic architectures within CTDE
- Why this work operates within CTDE (practical deployability)

**Key References:**
- `lowe2020` - MADDPG
- `foerster2018` - COMA
- `rashid2018` - QMIX
- `zhou2023` - Is CTDE all you need?

#### 1.2.3 Policy Optimization for Multi-Agent Systems (500 words)
- PPO as the workhorse algorithm: stability, sample efficiency
- MAPPO, IPPO, HAPPO variants
- Why PPO is the foundation for all three contributions
- Brief note on trust region methods

**Key References:**
- ⭐ `schulman2017a` - PPO (critical for all contributions)
- `yu2022` - Surprising effectiveness of MAPPO
- ⭐ `zhong2024` - HAPPO
- `li2023c` - Multi-agent trust region policy optimization

---

### 1.3 The Heterogeneity Challenge in MARL
**Suggested Length:** 1,800-2,200 words (~5-6 pages)
**Purpose:** Define the core problem space; introduce the behavioral/intrinsic taxonomy

#### 1.3.1 Taxonomy of Heterogeneity (700 words)
- **Behavioral heterogeneity:** Agents structurally identical but develop different behaviors through independent learning
- **Intrinsic heterogeneity:** Agents differ in sensors, effectors, or internal structure
- Observation-space vs. action-space heterogeneity
- Why this taxonomy matters for method selection

**Key References:**
- ⭐ `zhong2024` - HARL framework
- `guo2024` - Heterogeneous MARL survey
- `wakilpoor2020` - Heterogeneous MARL approaches
- `terry2020` - Parameter sharing for heterogeneous agents

#### 1.3.2 Parameter Sharing: Benefits and Limitations (500 words)
- Full parameter sharing: sample efficiency, coordination promotion
- The interchangeability assumption and when it breaks
- Selective parameter sharing attempts
- The storage/computation vs. flexibility trade-off

**Key References:**
- ⭐ `christianos2021` - Selective parameter sharing
- ⭐ `terry2020` - Agent indication methods
- `gupta2017` - Cooperative multi-agent control
- `hao2022` - Boosting MARL via agent grouping

#### 1.3.3 Current Approaches to Heterogeneity (600 words)
- Explicit agent indication: one-hot vectors, embeddings
- Separate policies per agent type (computational cost)
- Architectural solutions: attention, GNNs
- Representational solutions: observation encoding
- Gap: no systematic framework for choosing approaches

**Key References:**
- `iqbal2019` - Actor-Attention-Critic
- `iqbal2021` - REFIL
- ⭐ `liu2020b` - PIC (Permutation Invariant Critic)
- ⭐ `yang2021a` - IHG-MA (graph-based MARL)
- `hao2023` - GAT-MF

#### 1.3.4 The Observation Space Dimensionality Problem (400 words)
- Many benchmarks couple team size with observation dimensionality
- This blocks policy transfer, curriculum learning, zero-shot generalization
- Examples: LBF, SMAC, GRF
- Transition to: this is a representational problem

**Key References:**
- `papoudakis2021` - LBF, MARL benchmarking
- `samvelyan2019` - SMAC
- `kurach2020` - Google Research Football
- `terry2021` - PettingZoo

---

### 1.4 Research Gaps and Dissertation Positioning
**Suggested Length:** 1,200-1,500 words (~3-4 pages)
**Purpose:** Articulate the specific gaps each contribution addresses

#### 1.4.1 Gap 1: Curriculum Learning for Team Scaling (400 words)
- Existing curriculum work focuses on task complexity, not team size
- Smit et al. (2023) showed mixed results in GRF—why?
- The role of task structure and heterogeneity form unexplored
- **C1 addresses:** Can smaller-team pretraining reduce training cost?

**Key References:**
- ⭐ `smit2023` - GRF team scaling (key motivation)
- ⭐ `narvekar2020` - Curriculum learning for RL
- `baker2019` - Emergent tool use from autocurricula
- `shukla2022` - ACuTE

#### 1.4.2 Gap 2: Parameter Sharing Across Structural Heterogeneity (400 words)
- Current explicit indication doesn't resolve structural mismatches
- Separate policies scale poorly (1/|I| storage problem)
- No unified framework for arbitrary heterogeneity
- **C2 addresses:** Can homogenized representations enable shared policies?

**Key References:**
- ⭐ `zaheer2017` - Deep Sets (theoretical foundation)
- `diaconis1980` - Finite exchangeable sequences
- `hartford2018` - Deep models of interactions
- `tang2021` - Sensory neuron as transformer

#### 1.4.3 Gap 3: Systematic Comparison of Invariance Paradigms (400 words)
- Architectural (GNN) vs. representational (homogenization) approaches
- No controlled empirical comparison in HARL context
- When is architectural complexity justified?
- **C3 addresses:** Which paradigm is more effective?

**Key References:**
- `liu2020b` - PIC as architectural exemplar
- `kimura2024` - On permutation-invariant neural networks
- `noppakun2022` - Permutation invariant agent-specific centralized critic

---

### 1.5 Contributions and Thesis Overview
**Suggested Length:** 1,500-1,800 words (~4-5 pages)
**Purpose:** Present the three contributions as a coherent research program

#### 1.5.1 Contribution 1: Curriculum-Based Team Scaling (500 words)
- **Central question:** Can pretraining smaller teams and scaling via policy duplication reduce training cost?
- **Approach:** Agent-steps metric for normalized comparison; three benchmark environments
- **Key insight:** Task structure critically moderates curriculum effectiveness
- Environments: Waterworld (behavioral), Multiwalker (mild intrinsic), LBF (dynamic intrinsic)

**Key References:**
- `gupta2017` - Waterworld, Multiwalker
- `papoudakis2021` - LBF
- `smit2023` - Prior curriculum work

#### 1.5.2 Contribution 2: Implicit Indication via Homogenization (500 words)
- **Central question:** Can shared policy parameters work across structurally heterogeneous agents without explicit identifiers?
- **Approach:** Construct homogenized observation spaces; agent identity inferred from populated elements
- **Key insight:** Disjoint observation coverage can *improve* learning by reducing gradient interference
- Theoretical contribution: disjoint injective embeddings preserve representability

**Key References:**
- `zaheer2017` - Deep Sets
- `zhong2024` - HAPPO (baseline comparison)
- `christianos2021` - Selective parameter sharing

#### 1.5.3 Contribution 3: Architectural vs. Representational Approaches (500 words)
- **Central question:** Which paradigm is more effective—GNNs or homogenized representations?
- **Approach:** Controlled comparison between PIC and Implicit Indication
- **Key insight:** Representational solutions substantially outperform architectural solutions in this domain
- Implications for HARL system design

**Key References:**
- `liu2020b` - PIC
- `yu2022` - MAPPO
- `yang2021a` - IHG-MA

#### 1.5.4 The Unifying Thesis (300 words)
- Representation design matters as much as algorithmic architecture
- Task structure and heterogeneity type determine method selection
- Robustness emerges from good representational design
- Implications for practitioners and future research

---

### 1.6 Dissertation Structure
**Suggested Length:** 500-700 words (~1-2 pages)
**Purpose:** Guide the reader through the document

#### 1.6.1 Chapter Overview (400 words)
- **Chapter 2 (Literature Review):** Technical foundations across RL, MARL, HARL, curriculum learning, permutation invariance
- **Chapter 3 (C1):** Policy upsampling experiments
- **Chapter 4 (C2):** Implicit indication framework and experiments
- **Chapter 5 (C3):** Comparative evaluation of paradigms
- **Chapter 6 (Results/Conclusion):** Cross-cutting insights, design principles, future directions

#### 1.6.2 Cross-Chapter Connections (200 words)
- C1 → C2: C1 identifies observation dimensionality as barrier; C2 addresses via homogenization
- C1 → C3: Both investigate training efficiency through different lenses
- C2 → C3: C3 directly compares C2's homogenization against architectural alternatives
- All → Thesis: Representation over architecture

---

## Reference Mapping Summary

### By Section (Estimated Citation Counts)

| Section | Primary References | Supporting References | Total |
|---------|-------------------|----------------------|-------|
| 1.1 Opening | 8 | 4 | 12 |
| 1.2 MARL Foundations | 10 | 5 | 15 |
| 1.3 Heterogeneity | 14 | 6 | 20 |
| 1.4 Research Gaps | 10 | 4 | 14 |
| 1.5 Contributions | 9 | 6 | 15 |
| 1.6 Structure | 0 | 0 | 0 |
| **Total unique** | ~40-50 | | |

### Critical References (Must Include)

1. `schulman2017a` - PPO (foundation for all contributions)
2. `zhong2024` - HAPPO, HARL framework
3. `smit2023` - GRF curriculum learning (C1 motivation)
4. `terry2020` - Agent indication methods
5. `christianos2021` - Selective parameter sharing
6. `zaheer2017` - Deep Sets (C2 theoretical basis)
7. `liu2020b` - PIC (C3 comparison)
8. `gupta2017` - Waterworld, Multiwalker environments
9. `papoudakis2021` - LBF, MARL benchmarking
10. `yu2022` - Surprising effectiveness of MAPPO
11. `narvekar2020` - Curriculum learning survey
12. `yang2021a` - IHG-MA graph-based MARL

---

## Length Budget Summary

| Section | Pages | Words | % of Chapter |
|---------|-------|-------|--------------|
| 1.1 Opening | 3-4 | 1,200-1,500 | 15% |
| 1.2 MARL Foundations | 4-5 | 1,500-1,800 | 18% |
| 1.3 Heterogeneity | 5-6 | 1,800-2,200 | 22% |
| 1.4 Research Gaps | 3-4 | 1,200-1,500 | 15% |
| 1.5 Contributions | 4-5 | 1,500-1,800 | 18% |
| 1.6 Structure | 1-2 | 500-700 | 7% |
| **Total** | **20-26** | **7,700-9,500** | **100%** |

---

## Suggested Writing Order

1. **First:** §1.5 (Contributions) - This is the core; write it first to ensure clarity on what you're introducing
2. **Second:** §1.4 (Research Gaps) - Frame the problems each contribution solves
3. **Third:** §1.3 (Heterogeneity Challenge) - Establish the technical problem space
4. **Fourth:** §1.2 (MARL Foundations) - Provide necessary background
5. **Fifth:** §1.1 (Opening) - Write the hook after you know exactly what you're motivating
6. **Last:** §1.6 (Structure) - Simple roadmap after everything else is solid

---

## Key Transitions to Plan

### §1.1 → §1.2
> "While the strategic importance of autonomous multi-agent systems is clear, realizing their potential requires solving fundamental learning challenges. We now turn to the technical framework..."

### §1.2 → §1.3
> "The paradigms established above assume a degree of agent homogeneity that rarely holds in practice. Real-world deployments require agents with varying capabilities..."

### §1.3 → §1.4
> "Despite significant progress, several critical gaps remain in our ability to efficiently train heterogeneous multi-agent systems. This dissertation addresses three interconnected challenges..."

### §1.4 → §1.5
> "To address these gaps, we present three contributions that collectively advance the efficiency, flexibility, and deployability of heterogeneous multi-agent systems..."

### §1.5 → §1.6
> "The remainder of this dissertation develops these contributions and synthesizes their implications for HARL system design..."

---

## Figures to Consider

1. **Motivational figure:** Illustration of heterogeneous drone swarm with varying sensors
2. **Taxonomy diagram:** Behavioral vs. intrinsic heterogeneity with examples
3. **Contribution relationship diagram:** How C1, C2, C3 connect
4. **Table:** Research questions mapped to contributions and chapters

---

## Connections to Other Chapters

### To Literature Review (Chapter 2)
- §1.2 provides abbreviated versions of §2.1-2.2
- §1.3 previews §2.4 (Heterogeneity) and §2.3 (Scalability)
- §1.4 sets up §2.7 (Research Gaps)

### To Contributions (Chapters 3-5)
- §1.5.1 → C1 introduction section
- §1.5.2 → C2 introduction section
- §1.5.3 → C3 introduction section

### To Results/Conclusion (Chapter 6)
- Thesis statement in §1.5.4 should be echoed in conclusion
- Cross-chapter insights preview the synthesis

---

## Writing Notes

1. **Tone:** Authoritative but accessible; avoid overly technical jargon in §1.1
2. **Balance:** Don't front-load all technical content; let it build
3. **Signposting:** Use explicit transitions and preview statements
4. **Avoid:** Excessive hedging; state claims confidently where evidence supports
5. **Include:** Brief acknowledgment of limitations in §1.5.4 (expanded in conclusion)

---

*Outline generated: January 30, 2026*
*For use in subsequent writing sessions*
