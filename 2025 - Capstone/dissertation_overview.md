# Dissertation Overview

**Working Title:** Increasing Efficiency, Efficacy, and Extensibility in Heterogeneous Agent Reinforcement Learning

**Author:** Brandon Hosley (Captain, USAF)
**Degree:** Doctor of Philosophy in Operations Research
**Department:** ENS
**Expected Graduation:** March 2026
**Document Designator:** AFIT-ENS-DS-26-M-094

**Committee:**
- Bruce Cox, Ph.D. (Chair)
- Matthew Robbins, Ph.D. (Member)
- Maj Nicholas Yielding, Ph.D. (Member)

---

## Dissertation Structure

This is a **k-paper formatted dissertation** consisting of three main contributions (C1, C2, C3), each representing a standalone research paper unified by the theme of improving training efficiency and scalability in Multi-Agent Reinforcement Learning (MARL), particularly in heterogeneous settings (HARL).

### Core Research Theme

The dissertation addresses barriers to real-world deployment of autonomous multi-agent systems (e.g., drone swarms) by developing methods that reduce computational costs of training robust multi-agent policies at scale while maintaining or improving performance.

---

## Chapter Summaries

### Contribution 1 (C1): Policy Upsampling / Curriculum Learning for Team Scaling

**File:** `Chapters/C1/contribution_1.tex`

**Central Question:** Can pretraining smaller teams of agents and then scaling to target team sizes via policy duplication reduce training cost without sacrificing final performance?

**Focus:** Evaluates a curriculum-based training strategy where policies are first trained with fewer agents, then "upsampled" (duplicated) to create larger teams for continued training.

**Key Arguments:**
1. Training complexity scales with team size; smaller-team pretraining may reduce total computational cost
2. The effectiveness of this strategy depends heavily on task structure and the degree of role specialization required
3. Uses "agent-steps" (agents × training steps) as a normalized metric for comparing training efficiency

**Methodology:**
- Uses PPO (Proximal Policy Optimization) within the CTDE (Centralized Training with Decentralized Execution) paradigm
- Evaluates across three benchmark environments with different coordination demands:
  - **Waterworld**: Homogeneous agents, low coordination requirements
  - **Multiwalker**: Agents with fixed spatial roles, tight coordination needed
  - **Level-Based Foraging (LBF)**: Dynamic intrinsic heterogeneity via skill levels

**Key Findings:**
- **Waterworld**: Pretraining accelerated convergence without compromising final performance; larger ratios between pretraining and target team sizes yield greater benefits
- **Multiwalker**: Pretraining serves as a stabilizing mechanism for larger teams prone to early training failure due to sparse rewards
- **LBF**: Limited and inconsistent improvements; dynamic role complexity creates steep coordination challenges at scale

**Observation Schema Modifications:** Implemented "truncated" and "ally-ignorant" observation schemas to maintain fixed policy architectures across varying team sizes.

**Main Citations:**
- Smit et al. (2023) - Prior work on curriculum learning in GRF
- Gupta et al. (2017) - Waterworld, Multiwalker environments
- Papoudakis et al. (2021) - Level-Based Foraging
- Schulman et al. (2017) - PPO algorithm
- Narvekar et al. (2020) - Total reward ratio evaluation

---

### Contribution 2 (C2): Implicit Indication via Homogenization

**File:** `Chapters/C2/contribution_2.tex`

**Central Question:** Can shared policy parameters work across heterogeneous agents without explicit agent identifiers by using homogenized observation/action spaces?

**Focus:** Proposes "implicit indication" as a representational framework where agent identity is inferred from the pattern of populated observation elements rather than explicit identifiers.

**Key Arguments:**
1. Standard parameter sharing assumes agent interchangeability; this breaks down with structural heterogeneity
2. Explicit agent indication (one-hot vectors, embeddings) doesn't resolve structural mismatches in observation/action spaces
3. Homogenized spaces that span all agent-specific subspaces enable a single policy to operate across heterogeneous agents

**Core Concept - Homogenization:**
- Construct a unified observation space Õ as the union of all observation elements available to any agent
- Each agent's capabilities correspond to a distinct subset; unused elements are masked/empty
- Policies learn to condition implicitly on which elements are populated
- Requires "semantic decomposability": observation elements must have consistent meaning across agents

**Methodology:**
- Custom HyperGrid environment (MiniGrid-based) with configurable observation heterogeneity
- Compares Implicit Indication against HAPPO (separate policies per agent type)
- Four training configurations: Full visibility, Intersecting span, Disjoint span, Incomplete coverage
- Eight evaluation conditions testing robustness to sensor loss/gain, team changes, novel compositions

**Key Findings:**
- Implicit indication matches HAPPO performance during training with 1/|I| storage footprint
- Disjoint-span training showed strongest relative improvements (reduced gradient interference)
- Method provides inherent robustness to sensor dropout and team-size changes
- Novel agent compositions supported without architectural changes

**Theoretical Contribution:** Formalizes conditions under which disjoint injective embeddings preserve representability—any collection of functions over heterogeneous input spaces can be represented by a single function over the shared domain.

**Main Citations:**
- Terry et al. (2020) - Agent indication methods
- Christianos et al. (2021) - Selective parameter sharing
- Zaheer et al. (2017) - Deep Sets, permutation invariance
- Liu et al. (2020b) - Permutation Invariant Critic (PIC)
- Zhong et al. (2024) - HAPPO

---

### Contribution 3 (C3): Architectural vs. Representational Approaches to Heterogeneity

**File:** `Chapters/C3/contribution_3.tex`

**Central Question:** Which paradigm is more effective for heterogeneous MARL—architectural invariance (graph neural networks) or representational invariance (homogenized observation spaces)?

**Focus:** Direct empirical comparison between the Permutation Invariant Critic (PIC) and Implicit Indication under controlled experimental conditions.

**Key Arguments:**
1. Two paradigms exist for handling heterogeneity: architectural (specialized network layers) vs. representational (unified input encoding)
2. Explicit masking in representational approaches may provide more direct learning signals than learned graph-based aggregation
3. Domain characteristics (observation-based vs. behavioral heterogeneity) should guide paradigm selection

**Methodology:**
- Controlled comparison using matched network capacities and hyperparameters
- Same HyperGrid environment as C2
- PIC uses GNN-based critic with explicit agent type attributes
- Implicit Indication uses homogenized observations with standard networks

**Key Findings:**
- **Training**: Similar convergence behavior between methods
- **Evaluation**: Implicit Indication substantially outperforms PIC across all configurations
  - Complete visibility: 9.10 vs 3.89 mean return
  - Intersecting span: 5.04 vs 1.61
  - Disjoint span: 5.80 vs 1.84
  - Incomplete: 4.63 vs 1.05
- Implicit Indication also outperforms HAPPO baseline despite using single shared policy
- Superior robustness to sensor changes, team composition modifications, and zero-shot generalization

**Discussion Points:**
- PIC's graph-based architecture may be better suited to environments with richer relational structure
- Discrete gridworld domain may not leverage GNN inductive biases effectively
- Representational solutions can be highly effective when heterogeneity is structural and semantically decomposable

**Main Citations:**
- Liu et al. (2020b) - PIC
- Yu et al. (2022) - MAPPO
- Zhong et al. (2024) - HAPPO
- Yang et al. (2021a) - Graph-based MARL

---

## Key Terminology and Definitions

### Abbreviations

| Abbreviation | Full Term |
|-------------|-----------|
| MARL | Multi-Agent Reinforcement Learning |
| HARL | Heterogeneous-Agent Reinforcement Learning |
| PPO | Proximal Policy Optimization |
| HAPPO | Heterogeneous-Agent PPO |
| MAPPO | Multi-Agent PPO |
| IPPO | Independent PPO |
| CTDE | Centralized Training with Decentralized Execution |
| PIC | Permutation-Invariant Critic |
| GNN | Graph Neural Network |
| MLP | Multi-Layer Perceptron |
| DNN | Deep Neural Network |
| LBF | Level-Based Foraging |
| Dec-POMDP | Decentralized Partially Observable MDP |
| POSG | Partially Observable Stochastic Game |
| GAE | Generalized Advantage Estimator |
| HPN | Hyper Policy Network |

### Mathematical Notation

| Symbol | Description |
|--------|-------------|
| I | Set of agents i |
| t, T | Time step, set of time steps |
| s, S | State, state space |
| O, Oᵢ | Observation space, marginal observation space of agent i |
| o, oᵢ | Joint observation, observation of agent i |
| A, Aᵢ | Action space, marginal action space of agent i |
| a, aᵢ | Joint action, action of agent i |
| r, rᵢ | Reward, reward for agent i |
| π, πᵢ | Policy, policy of agent i |
| C | Set of observation element indices (channels) |
| Cᵢ | Observation element subset for agent i |
| Õ | Homogenized observation space |
| P(C) | Power set of C |
| γ | Discount factor |
| E[·] | Expected value |
| V(s) | State value function |
| Q(s,a) | Action-value function |
| Â | Advantage estimate |

### Key Concepts

**Behavioral Heterogeneity:** Agents are structurally identical but develop different behaviors through independent policy updates during training.

**Intrinsic Heterogeneity:** Agents differ in sensors, effectors, or internal structure, leading to varying observation or action spaces.

**Semantic Decomposability:** The assumption that observation/action spaces can be factorized into elements with consistent meaning across agents.

**Agent-Steps:** Normalized training cost metric defined as (number of agents) × (training steps).

**Implicit Indication:** Agent identity inferred from the pattern of populated observation elements rather than explicit identifiers.

**Homogenized Space:** A unified representation spanning all agent-specific subspaces, enabling shared policy training.

---

## Environments Used

### Waterworld (PettingZoo/SISL)
- Continuous control, homogeneous agents
- Navigate 2D arena to collect food, avoid poison
- Supports emergent behavioral heterogeneity
- Low coordination requirements

### Multiwalker (PettingZoo/SISL)
- Physically coupled bipedal agents transporting payload
- Fixed spatial positions create observation asymmetries
- Tight temporal coordination required
- Sparse rewards, sensitive to coordination failures

### Level-Based Foraging (LBF)
- Discrete grid-world with skill-leveled agents and food
- Dynamic intrinsic heterogeneity through variable skill levels
- Coordination depends on matching agent abilities to task demands
- Observation space scales with team size (problematic for transfer)

### HyperGrid (Custom - C2/C3)
- MiniGrid-based, n-dimensional discrete grid
- Configurable observation heterogeneity via sensor channels
- Shared action space, cooperative objectives
- Designed to isolate observation heterogeneity effects

---

## Cross-Chapter Connections

1. **C1 → C2:** C1 identifies observation space dimensionality as a barrier to policy transfer; C2 addresses this via homogenization
2. **C1 → C3:** Both investigate training efficiency; C1 through curriculum learning, C3 through representation choice
3. **C2 → C3:** C3 directly compares the homogenization approach from C2 against architectural alternatives
4. **Unifying Theme:** All contributions seek to improve MARL/HARL training efficiency while maintaining flexibility for heterogeneous deployments

---

## Status and TODOs

### Completed
- [x] Contribution 1 - Complete
- [x] Contribution 2 - Complete
- [x] Contribution 3 - Complete

### Pending (from dissertation.tex)
- [ ] Introduction chapter (placeholder)
- [ ] Abstract (placeholder)
- [ ] Literature Review - content exists but may need integration
- [ ] Results/Discussion chapter (commented out)
- [ ] Conclusion chapter (commented out)
- [ ] Keywords selection
- [ ] SF 298 form completion
- [ ] Glossary organization improvements

---

*Last Updated: January 2026*
*Document created for cross-session reference by Claude*
