# Literature Review Chapter Outline
## Dissertation: Increasing Efficiency, Efficacy, and Extensibility in Heterogeneous Agent Reinforcement Learning

**Document Purpose:** Comprehensive outline for writing the Literature Review chapter
**Target Length:** ~12,000-15,000 words (30-40 pages)
**Last Updated:** January 29, 2026

---

## Executive Summary

This literature review positions the dissertation's three contributions within the broader MARL landscape:

| Contribution | Core Problem | Lit Review Connection |
|-------------|--------------|----------------------|
| **C1**: Curriculum Learning | Team scaling efficiency | §2.5 (Curriculum Learning) + §2.3 (Scalability) |
| **C2**: Implicit Indication | Heterogeneous parameter sharing | §2.4 (Heterogeneity) + §2.6 (Permutation Invariance) |
| **C3**: Arch vs. Rep | Paradigm comparison for HARL | §2.6 (Permutation) + §2.4 (Heterogeneity) |

---

## Chapter Structure

### 2.1 Foundations of Reinforcement Learning
**Suggested Length:** 1,500-2,000 words (~4-5 pages)
**Purpose:** Establish notation and fundamental concepts

#### 2.1.1 Single-Agent Reinforcement Learning (800 words)
- Markov Decision Processes (MDPs)
- Value functions and optimality
- Policy gradient methods

**Key References:**
- `sutton2018` - *Reinforcement Learning: An Introduction* (foundational text)
- `kaelbling1996` - *Reinforcement Learning: A Survey*
- `puterman2005` - *Markov Decision Processes*
- `williams1992` - REINFORCE algorithm
- `watkins1992` - Q-Learning

#### 2.1.2 Deep Reinforcement Learning (700 words)
- Function approximation with neural networks
- DQN and the deep RL revolution
- Actor-critic architectures

**Key References:**
- `mnih2013`, `mnih2015` - DQN papers
- `mnih2016` - A3C
- `lillicrap2019` - DDPG
- `schulman2017` - TRPO

#### 2.1.3 Proximal Policy Optimization (500 words)
- Clipped surrogate objective
- Importance for MARL adoption
- *Connection to C1/C2/C3: All contributions use PPO*

**Key References:**
- ⭐ `schulman2017a` - PPO (main citation)
- `kakade2002` - Approximately optimal approximate RL

---

### 2.2 Multi-Agent Reinforcement Learning Fundamentals
**Suggested Length:** 2,500-3,000 words (~7-8 pages)
**Purpose:** Introduce MARL formalism and core paradigms

#### 2.2.1 Problem Formalization (800 words)
- Dec-POMDPs and POSGs
- Joint action spaces and reward structures
- Cooperative vs. competitive vs. mixed settings

**Key References:**
- `littman1994` - Markov games framework
- `busoniu2008` - Comprehensive MARL survey
- `shoham2007` - *If MARL is the answer, what is the question?*

#### 2.2.2 Centralized Training with Decentralized Execution (CTDE) (700 words)
- The paradigm explained
- Benefits for coordination learning
- Critic architectures and centralized information
- *Connection to C1/C2/C3: All contributions operate within CTDE*

**Key References:**
- `lowe2020` - MADDPG
- `foerster2018` - COMA (Counterfactual Multi-Agent Policy Gradients)
- `rashid2018` - QMIX
- `zhou2023` - *Is Centralized Training with Decentralized Execution All You Need?*

#### 2.2.3 Independent Learning vs. Centralized Methods (600 words)
- IPPO and its surprising effectiveness
- Value decomposition approaches
- Communication learning

**Key References:**
- ⭐ `yu2022` - *Surprising Effectiveness of MAPPO* (main citation for C3)
- `witt2020` - *Is Independent Learning All You Need?*
- `sukhbaatar2016` - Learning multiagent communication

#### 2.2.4 Multi-Agent PPO Variants (700 words)
- MAPPO, IPPO, HAPPO
- Trust region methods in multi-agent settings
- *Direct connection to C2/C3 methods*

**Key References:**
- ⭐ `zhong2024` - HAPPO (main citation for C2/C3)
- `li2023c` - Multi-Agent Trust Region Policy Optimization
- `wen2021` - DTDE

---

### 2.3 Scalability Challenges in MARL
**Suggested Length:** 2,000-2,500 words (~5-6 pages)
**Purpose:** Frame the scalability problem that motivates all three contributions

#### 2.3.1 Computational Complexity and Team Size (800 words)
- Exponential growth of joint action/observation spaces
- Training time vs. number of agents
- Sample efficiency concerns
- *Connection to C1: Directly motivates curriculum approach*

**Key References:**
- `gronauer2022` - Multi-Agent DRL Survey
- `zhang2021` - MARL: A Selective Overview
- `hernandez-leal2019` - Survey on multi-agent learning
- `liu2024a` - *Scaling Up MARL*

#### 2.3.2 Parameter Sharing for Efficiency (1,000 words)
- Full parameter sharing: benefits and limitations
- Selective parameter sharing approaches
- Trade-offs: efficiency vs. specialization
- *Connection to C2: Extends parameter sharing to heterogeneous settings*

**Key References:**
- ⭐ `terry2020` - *Parameter Sharing for Heterogeneous Agents* (main citation for C2)
- ⭐ `christianos2021` - *Selective Parameter Sharing* (main citation for C2)
- `hao2022` - Boosting MARL via agent grouping

#### 2.3.3 Benchmark Environments and Evaluation (700 words)
- Evolution of MARL benchmarks
- Waterworld, Multiwalker, LBF characterization
- Evaluation metrics (agent-steps)
- *Connection to C1: Justifies environment selection*

**Key References:**
- ⭐ `gupta2017` - Waterworld, Multiwalker (main citation for C1)
- ⭐ `papoudakis2021` - LBF, MARL benchmarking (main citation for C1)
- `terry2021` - PettingZoo
- `samvelyan2019` - SMAC
- `ellis2023` - SMACv2
- `kurach2020` - Google Research Football
- `rutherford2023` - JaxMARL

---

### 2.4 Heterogeneous Multi-Agent Reinforcement Learning
**Suggested Length:** 2,500-3,000 words (~7-8 pages)
**Purpose:** Establish the heterogeneity problem central to C2 and C3

#### 2.4.1 Taxonomy of Heterogeneity (800 words)
- **Behavioral heterogeneity**: Same structure, different learned behaviors
- **Intrinsic heterogeneity**: Different sensors, actuators, capabilities
- Observation-space vs. action-space heterogeneity
- *Connection to C2/C3: Defines the problem space*

**Key References:**
- ⭐ `zhong2024` - HARL framework
- `guo2024` - Heterogeneous MARL: A Survey
- `calvo2018` - Heterogeneous Multi-Agent DRL
- `wakilpoor2020` - Heterogeneous MARL approaches

#### 2.4.2 Agent Indication Methods (800 words)
- One-hot encoding approaches
- Learned embeddings and agent IDs
- Limitations for structural heterogeneity
- *Connection to C2: Motivates implicit indication*

**Key References:**
- ⭐ `terry2020` - Agent indication methods
- `iqbal2019` - Actor-Attention-Critic
- `iqbal2021` - REFIL (Randomized Entity-wise Factorization)

#### 2.4.3 Separate Policies vs. Shared Policies (700 words)
- Independent policies per agent type
- Computational costs of maintaining multiple networks
- Generalization limitations
- *Connection to C2/C3: Storage footprint motivation*

**Key References:**
- ⭐ `zhong2024` - HAPPO (separate policies baseline)
- `li2023d` - F2A2 (flexible agent assignment)

#### 2.4.4 Real-World Applications: Heterogeneous Swarms (700 words)
- Drone swarm heterogeneity requirements
- Military and civilian applications
- Sensor diversity in practical deployments
- *Connection to dissertation motivation*

**Key References:**
- `rizk2019` - Cooperative Heterogeneous Multi-Robot Systems
- `brambilla2013` - Swarm Robotics
- `hoang2023` - Drone Swarms
- `kallenborn2024` - Swarm warfare
- `gerstein2024` - Emerging technology and autonomy
- `amarasinghe2019` - Agricultural drone swarms

---

### 2.5 Curriculum Learning and Transfer in MARL
**Suggested Length:** 2,000-2,500 words (~5-6 pages)
**Purpose:** Ground C1 in the curriculum learning literature

#### 2.5.1 Curriculum Learning Foundations (700 words)
- From easy to hard: progressive complexity
- Automatic curriculum generation
- Task sequencing strategies

**Key References:**
- ⭐ `narvekar2020` - *Curriculum Learning for RL* (main citation for C1)
- `baker2019` - Emergent tool use from multi-agent autocurricula
- `balduzzi2019` - Open-ended learning

#### 2.5.2 Team Size Curriculum Approaches (800 words)
- Training with fewer agents first
- Policy upsampling and duplication
- Agent-steps as normalized metric
- *Direct connection to C1 methodology*

**Key References:**
- ⭐ `smit2023` - GRF team scaling (main citation for C1)
- `liu2024a` - Scaling up MARL
- `berner2019` - Dota 2 (large-scale training)
- `vinyals2019` - StarCraft II (AlphaStar)

#### 2.5.3 Transfer Learning in Multi-Agent Settings (700 words)
- Policy transfer across team configurations
- Observation schema adaptation
- Challenges with varying input dimensions
- *Connection to C1: Truncated/ally-ignorant schemas*

**Key References:**
- `shi2023` - Lateral Transfer Learning
- `shukla2022` - ACuTE (curriculum transfer)
- `chen2016` - Net2Net (network morphism)
- `gupta2017a` - Learning invariant feature spaces

#### 2.5.4 Limitations of Curriculum Approaches (500 words)
- Task structure dependencies
- Role specialization barriers
- When curriculum helps vs. hinders
- *Connection to C1 findings: LBF challenges*

**Key References:**
- `ye2020` - Full MOBA games (complexity limits)
- `sun2023` - Asymmetrical multiplayer games

---

### 2.6 Permutation Invariance and Architectural Approaches
**Suggested Length:** 2,500-3,000 words (~7-8 pages)
**Purpose:** Frame the architectural vs. representational debate for C2/C3

#### 2.6.1 The Permutation Problem in MARL (700 words)
- Agent ordering sensitivity
- Set-based representations
- Why permutation matters for generalization
- *Connection to C2/C3: Core theoretical motivation*

**Key References:**
- ⭐ `zaheer2017` - Deep Sets (main citation for C2)
- `diaconis1980` - Finite exchangeable sequences
- `kimura2024` - On Permutation-Invariant Neural Networks

#### 2.6.2 Architectural Solutions: Graph Neural Networks (900 words)
- GNNs for agent interactions
- Message passing and attention mechanisms
- Permutation equivariance through architecture
- *Connection to C3: PIC comparison*

**Key References:**
- ⭐ `liu2020b` - PIC (Permutation Invariant Critic) (main citation for C2/C3)
- ⭐ `yang2021a` - IHG-MA (graph-based MARL) (main citation for C3)
- `zambaldi2018` - Relational deep RL
- `hao2023` - GAT-MF
- `lee2019` - Set Transformer
- `vaswani2017` - Attention is All You Need

#### 2.6.3 Representational Solutions: Input Encoding (800 words)
- Feature-level permutation handling
- Masking and padding approaches
- Semantic decomposability assumption
- *Connection to C2: Homogenization approach*

**Key References:**
- `hartford2018` - Deep Models of Interactions
- `murphy2019` - Janossy Pooling
- `tang2021` - Sensory Neuron as Transformer
- `li2021b` - Permutation Invariant Policy Optimization
- `hazra2024` - Addressing Permutation Challenges

#### 2.6.4 Comparing Paradigms: When to Use What (600 words)
- Architectural vs. representational trade-offs
- Domain characteristics that favor each approach
- Explicit vs. implicit inductive biases
- *Direct motivation for C3 research question*

**Key References:**
- `noppakun2022` - Permutation Invariant Agent-Specific Centralized Critic
- `sonar2021` - Invariant Policy Optimization

---

### 2.7 Research Gaps and Dissertation Positioning
**Suggested Length:** 1,000-1,500 words (~3-4 pages)
**Purpose:** Synthesize gaps and position contributions

#### 2.7.1 Gap 1: Curriculum Learning for Heterogeneous Teams (400 words)
- Existing work focuses on homogeneous scaling
- Role specialization challenges unexplored
- *C1 addresses this gap*
- Connection to prospectus research questions:
    - RQ1: Can smaller-team pretraining + duplication + retraining improve training efficiency without sacrificing final performance?
    - RQ2: How does effectiveness vary across environments with different heterogeneity forms?

#### 2.7.2 Gap 2: Parameter Sharing Without Explicit Indication (400 words)
- Current methods require architectural changes or explicit IDs
- No unified framework for arbitrary heterogeneity
- *C2 addresses this gap with homogenization*
- Connection to prospectus research questions:
    - RQ1: How do input-invariant structures affect learning efficiency and team robustness with partially overlapping observations?
    - RQ2: Do input-invariant architectures stabilize performance under team-size changes and partial observation loss?
    - RQ3: What are the computational/implementation costs relative to benefits (mean-field / invariant modules)?

#### 2.7.3 Gap 3: Systematic Comparison of Invariance Paradigms (400 words)
- Architectural and representational approaches compared informally
- No controlled empirical comparison in HARL context
- *C3 addresses this gap*
- Connection to prospectus research questions:
    - RQ1: To what extent do graph-based policies improve learning efficiency in heterogeneous-agent environments vs. alternatives?
    - RQ2: How robust are graph-based policies to changes in partial observability and team composition?
    - RQ3: What are the computational/implementation costs relative to performance benefits?

#### 2.7.4 Contribution Summary Table (300 words)
- Synthesis of how each contribution addresses identified gaps
- Relationship between contributions
- Preview of methodology chapters

---

## Reference Mapping Summary

### By Section

| Section | References | Main Citations |
|---------|------------|----------------|
| 2.1 Foundations | 12 | schulman2017a |
| 2.2 MARL Fundamentals | 14 | yu2022, zhong2024 |
| 2.3 Scalability | 13 | terry2020, christianos2021, gupta2017, papoudakis2021 |
| 2.4 Heterogeneity | 14 | zhong2024, terry2020 |
| 2.5 Curriculum | 12 | narvekar2020, smit2023 |
| 2.6 Permutation | 15 | zaheer2017, liu2020b, yang2021a |
| 2.7 Gaps | 6 | (synthesis) |

**Total unique references used:** ~70-80 of 153 available

---

## Identified Reference Gaps

### Critical Gaps (High Priority - Seek Additional References)

1. **Graph Neural Networks for MARL**
   - Current catalog: Only 1 reference (`yang2021a`)
   - **Needed:** 3-5 additional GNN-MARL papers
   - **Suggested searches:**
     - Wang et al. "Multi-Agent Graph Attention Communication"
     - Jiang et al. "Graph Convolutional RL"
     - Agarwal et al. "Graph Networks for Multi-Agent"

2. **Observation Space Design**
   - Current catalog: Limited explicit coverage
   - **Needed:** Papers on observation engineering for MARL
   - **Suggested searches:**
     - "State representation learning MARL"
     - "Feature engineering multi-agent"

3. **Semantic Decomposability / Compositional Observations**
   - Current catalog: No direct references
   - **Needed:** Papers on compositional/factored representations
   - **Suggested searches:**
     - Factored MDPs literature
     - Compositional generalization in RL

### Moderate Gaps (Medium Priority)

4. **Zero-Shot Generalization in MARL**
   - Current catalog: Indirect coverage only
   - **Needed:** 2-3 papers on zero-shot/few-shot MARL
   - References like `stone2010` (ad hoc teams) partially cover this

5. **Robustness to Agent Changes**
   - Current catalog: Limited
   - **Needed:** Papers on agent dropout, sensor failure robustness
   - Relevant to C2's robustness claims

6. **Network Capacity and Expressiveness**
   - Current catalog: Minimal
   - **Needed:** Papers comparing network architectures in MARL
   - `hachmo` (intrinsic dimensionality) is relevant but incomplete

### Minor Gaps (Low Priority)

7. **Military/DoD MARL Applications**
   - Current catalog: Good coverage (22 drone/swarm references)
   - Could add 1-2 recent AFIT/DoD technical reports

8. **Hyperparameter Sensitivity**
   - Current catalog: `akiba2019` (Optuna), `liaw2018` (Tune)
   - Adequate for methodology; additional not critical

---

## Suggested Writing Order

1. **First:** §2.1 (Foundations) - establishes notation
2. **Second:** §2.2 (MARL Fundamentals) - core paradigms
3. **Third:** §2.3 (Scalability) - frames the problem
4. **Fourth:** §2.4 (Heterogeneity) - central to C2/C3
5. **Fifth:** §2.5 (Curriculum) - C1 grounding
6. **Sixth:** §2.6 (Permutation) - C2/C3 technical basis
7. **Last:** §2.7 (Gaps) - synthesis and positioning

---

## Cross-References to Contributions

### Contribution 1 (Curriculum Learning)
- Primary sections: §2.3, §2.5
- Supporting sections: §2.2.4, §2.4.1
- Key references: smit2023, gupta2017, papoudakis2021, narvekar2020

### Contribution 2 (Implicit Indication)
- Primary sections: §2.4, §2.6
- Supporting sections: §2.3.2, §2.2.4
- Key references: terry2020, christianos2021, zaheer2017, liu2020b, zhong2024

### Contribution 3 (Arch vs. Rep)
- Primary sections: §2.6
- Supporting sections: §2.4, §2.3
- Key references: liu2020b, yu2022, zhong2024, yang2021a

---

## Length Budget Summary

| Section | Pages | Words | % of Chapter |
|---------|-------|-------|--------------|
| 2.1 Foundations | 4-5 | 1,500-2,000 | 13% |
| 2.2 MARL Fundamentals | 7-8 | 2,500-3,000 | 20% |
| 2.3 Scalability | 5-6 | 2,000-2,500 | 17% |
| 2.4 Heterogeneity | 7-8 | 2,500-3,000 | 20% |
| 2.5 Curriculum | 5-6 | 2,000-2,500 | 17% |
| 2.6 Permutation | 7-8 | 2,500-3,000 | 20% |
| 2.7 Gaps/Positioning | 3-4 | 1,000-1,500 | 10% |
| **Total** | **38-45** | **14,000-17,500** | **100%** |

---

## Next Steps

1. [ ] Address critical reference gaps (GNN-MARL, semantic decomposability)
2. [ ] Draft §2.1 to establish notation consistency
3. [ ] Write §2.7 early to clarify positioning arguments
4. [ ] Develop transition paragraphs between sections
5. [ ] Create figure/table list for visual elements

---

*Outline generated: January 29, 2026*
*For use in subsequent writing sessions*
