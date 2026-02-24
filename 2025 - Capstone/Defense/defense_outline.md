# DIE-HARL Defense Presentation Outline
**Durable, Implicit, and Extensible Heterogeneous Agent Reinforcement Learning**
Capt Brandon Hosley, USAF — Ph.D. Defense, AFIT-ENS-DS-26-M-094

---

## Slide Count & Timing Strategy

| Section | Slides | Est. Time |
|---|---|---|
| Opening & Roadmap | 3 | ~3 min |
| Motivation & Context | 4 | ~5 min |
| Technical Foundations | 5 | ~6 min |
| Contribution 1 | 8 | ~10 min |
| Contribution 2 | 8 | ~10 min |
| Contribution 3 | 7 | ~9 min |
| Synthesis & Contributions Status | 4 | ~5 min |
| Limitations & Future Work | 2 | ~3 min |
| Closing | 2 | ~3 min |
| **TOTAL** | **43** | **~54 min** |

---

## SECTION 1: Opening & Roadmap (3 slides)

### Slide 1 — Title Slide
- Dissertation title
- Author, committee, department, date
- AFIT crest / distribution statement

### Slide 2 — Dissertation Roadmap
- Visual showing three contributions in relation to one another
- Emphasize the logical chain: _cost_ → _capability_ → _comparison_
- Brief bullets: C1 addresses training efficiency; C2 addresses heterogeneity handling; C3 validates the approach
- Label: "Three questions, one unified answer"

### Slide 3 — Contributions Status *(requested feature)*
A table with status indicators for each contribution and its sub-claims:

| Contribution | Central Question | Environment(s) | Status |
|---|---|---|---|
| **C1: Policy Upsampling** | Can pretraining smaller teams reduce cost without sacrificing performance? | Waterworld, Multiwalker, LBF | ✓ Complete |
| **C2: Implicit Indication** | Can a shared policy handle structural heterogeneity without explicit identifiers? | HyperGrid | ✓ Complete |
| **C3: Paradigm Comparison** | Does representational or architectural invariance perform better? | HyperGrid | ✓ Complete |

---

## SECTION 2: Motivation & Context (4 slides)

### Slide 4 — The Autonomous Systems Imperative
- DoD Replicator Initiative (Dep. Sec. Hicks, 2023) — hundreds of autonomous systems, months not years
- DARPA OFFSET — 100+ agent swarm demonstrations
- **Bold emphasis:** The capability exists. The bottleneck is *training*.
- Visual: drone swarm / fleet illustration (use `drone-mid.pdf` asset)

### Slide 5 — Why Heterogeneous Agents?
- Operational reality: mixed fleets are the norm, not the exception
- Examples: aerial surveillance + ground vehicles, varying sensor loadouts, skill tiers
- **Bold emphasis:** *Homogeneous assumptions don't hold in deployment.*
- Taxonomy visual distinguishing behavioral vs. intrinsic heterogeneity

### Slide 6 — The Three Training Challenges
Lay out the three research gaps clearly as the narrative throughline:
1. **Efficiency** — Training large teams is expensive. Can curricula help? → _C1_
2. **Flexibility** — Heterogeneous agents break parameter sharing. Can representation fix it? → _C2_
3. **Design Choice** — When we solve heterogeneity, which paradigm wins? → _C3_

### Slide 7 — Thesis Statement
Single-slide framing of the unifying thesis:
> *"Training efficiency, heterogeneity handling, and deployment flexibility in HARL are fundamentally **representational** problems before they are **architectural** ones."*

Brief sub-bullets previewing the evidence

---

## SECTION 3: Technical Foundations (5 slides)

### Slide 8 — MARL Primer
- Single-agent RL → Multi-agent extension
- Dec-POMDP framing
- **Bold:** *Non-stationarity* as the core challenge
- Keep brief — committee knows this material

### Slide 9 — CTDE and PPO Family
- Centralized Training, Decentralized Execution diagram (use `ctde_actor-critic.tex`)
- MAPPO → IPPO → HAPPO lineage
- **Bold:** *HAPPO* as the primary baseline for C2/C3

### Slide 10 — The Heterogeneity Landscape
- Behavioral vs. Intrinsic heterogeneity defined
- Current solutions: one-hot identifiers, per-type policies, attention, GNNs
- Each has costs — motivates the C2 approach

### Slide 11 — The Observation-Space Coupling Problem
- Key blocker identified in C1: team size is coupled to observation dimension in many benchmarks
- Diagram showing how agent-count changes break policy transfer
- **Bold:** *This is the precise barrier* that policy upsampling and truncated schemas address

### Slide 12 — Environments Overview
- Brief visual tour of all four environments used (one panel each)
- Waterworld, Multiwalker, LBF (C1) — HyperGrid (C2/C3)
- Characterize: continuous vs. discrete, coordination tightness, heterogeneity type
- Use existing environment PNGs

---

## SECTION 4: Contribution 1 — Curriculum-Based Team Scaling (8 slides)

### Slide 13 — C1 Central Question
- "Can pretraining smaller teams and scaling via policy duplication reduce training cost without sacrificing final performance?"
- **Bold:** *Policy upsampling* as the novel mechanism
- Diagram of the two-phase training schema (`training_1.png`, `training_2.png`)

### Slide 14 — The Agent-Steps Metric
- Motivate why existing metrics obscure cost comparisons
- Define agent-steps: `agents × training steps`
- **Bold/Italic:** This enables *normalized cost comparison* across team sizes
- Quick visual example illustrating the math

### Slide 15 — Observation Schema Solutions
- Truncated observation schema (fixed-width, pads with zeros for missing allies)
- Ally-ignorant variant
- **Bold:** These solve the *dimensionality coupling problem*
- Side-by-side schema diagram

### Slide 16 — C1 Results: Waterworld
- Show training curves for 3-8 agent configurations
- Highlight: pretraining accelerates convergence; benefit scales with size ratio
- AUC comparison bar chart (`Waterworld-AUCs.png`)
- **Callout:** Clear win — environment well-suited to curriculum

### Slide 17 — C1 Results: Multiwalker
- Show training curves
- Highlight: pretraining as *stabilization* — without it, large teams frequently fail entirely
- **Bold:** Even when final performance is matched, the *path* matters
- AUC comparison (`Multiwalker-AUCs.png`)

### Slide 18 — C1 Results: LBF
- Show training curves; note limited/inconsistent improvements
- Explain: dynamic intrinsic heterogeneity (variable skill levels) creates steep scaling challenges
- **Bold:** *Task structure moderates* curriculum effectiveness
- AUC comparison (`LBF-AUCs.png`)

### Slide 19 — C1 Synthesis
- Summary table: Waterworld (strong benefit) | Multiwalker (stabilization benefit) | LBF (mixed)
- Takeaway: curriculum through team size is *environment-dependent*
- The bottleneck is representational — poorly designed obs spaces block transfer
- Bridge forward: "This motivates designing obs spaces that *support* sharing from the start → C2"

### Slide 20 — C1 (Backup/Optional): Iteration Cost Analysis
- `iter_cost.png` showing cost per agent-step
- Useful if committee asks about practical training budgets
- Mark as backup slide

---

## SECTION 5: Contribution 2 — Implicit Indication (8 slides)

### Slide 21 — C2 Central Question
- "Can a shared policy work across structurally heterogeneous agents without explicit agent identifiers?"
- **Bold:** The key insight: *implicit conditioning* via observation structure
- Contrast with one-hot vectors and per-type policies

### Slide 22 — The Implicit Indication Framework
- Define homogenized observation space Õ
- Each agent accesses only its relevant elements; remainder masked/zeroed
- **Bold:** Policy infers *agent identity from the pattern of populated elements*
- No explicit identifiers needed
- Clean conceptual diagram (draw or adapt `rgb.tex` visualization)

### Slide 23 — Key Requirement: Semantic Decomposability
- Define: observation elements must have consistent meaning across agent types
- Counterexample of when it fails vs. when it succeeds
- **Italic:** *Semantic decomposability* is the precondition
- Formal result: any collection of functions over heterogeneous spaces can be represented by a single function over the homogenized domain (Deep Sets foundation)

### Slide 24 — HyperGrid Environment
- MiniGrid-based n-dimensional gridworld
- Configurable sensor channels as source of heterogeneity
- Four training configurations: complete, intersecting-span, disjoint-span, incomplete
- Show `marl-minigrid.png`

### Slide 25 — C2 Training Results
- Training performance across four sensor configurations
- Implicit Indication matches HAPPO performance during training
- **Bold:** *Same performance, 1/|I| storage footprint*
- Show training curves with configuration labels

### Slide 26 — C2 Robustness Evaluation (8 Conditions)
- List the 8 eval conditions (sensor loss, degradation, improvement, coverage changes, shuffled assignments, zero-shot)
- Show aggregate robustness profile — implicit indication handles novel configurations gracefully
- **Bold:** *Robustness emerges as a natural consequence* of representational design — not from explicit robustness training

### Slide 27 — C2 Synthesis
- Key result: parameter-shared policy across structurally different agents, no IDs needed
- **Bold:** 1/|I| storage, zero-shot generalization, tolerance to sensor changes
- Bridge forward: "But there are architectural alternatives — how does this representational approach compare? → C3"

### Slide 28 — C2 (Backup): Disjoint-Span Finding
- Disjoint-span training showed strongest relative improvements
- Hypothesis: non-overlapping observations reduce gradient interference
- Design implication: prefer clean separation in observation structure when possible

---

## SECTION 6: Contribution 3 — Paradigm Comparison (7 slides)

### Slide 29 — C3 Central Question
- "Which paradigm is more effective — architectural invariance (GNNs) or representational invariance (homogenization)?"
- **Bold:** The *surprising* hypothesis going in: GNNs should win — richer expressiveness
- **Bold:** The *finding*: they don't

### Slide 30 — Two Paradigms, Side by Side
| | Representational (Implicit Indication) | Architectural (PIC / GNN) |
|---|---|---|
| Mechanism | Homogenized obs + masking | Graph convolutional layers + symmetric pooling |
| Agent info | Inferred from obs pattern | Explicit type attributes on nodes |
| Network type | Standard feed-forward MLP | Graph Neural Network |
| Complexity | Lower | Higher |

- **Bold:** PIC = *Permutation Invariant Critic*

### Slide 31 — C3 Experimental Design
- Same HyperGrid environment as C2
- Matched network capacities and hyperparameters
- Four sensor configurations × eight evaluation conditions
- Clean controlled comparison

### Slide 32 — C3 Main Result: Performance Comparison
Headline table:

| Config | Implicit Indication | PIC | Advantage |
|---|---|---|---|
| Complete Visibility | 9.10 | 3.89 | **2.34×** |
| Intersecting-Span | 5.04 | 1.61 | **3.13×** |
| Disjoint-Span | 5.80 | 1.84 | **3.15×** |
| Incomplete Coverage | 4.63 | 1.05 | **4.41×** |

- **Bold:** Implicit Indication wins *consistently* and *substantially* across all configurations
- Visual: `eval_scale.png` or equivalent performance comparison plot

### Slide 33 — C3 Robustness Comparison
- Eval heatmaps (`eval_heatmaps.png`) or box plots (`eval_boxes.png`) showing robustness profiles
- Implicit Indication also outperforms both PIC *and* HAPPO under perturbed conditions
- **Bold:** The representational approach is *more robust and more efficient*

### Slide 34 — C3 Interpretation
- Why does the simpler approach win?
- PIC's GNN may be better suited to environments with rich *relational* structure
- In structurally-heterogeneous discrete domains with semantically decomposable obs, explicit masking provides cleaner gradient signals
- **Bold:** *Architectural sophistication is not a substitute for representational clarity*
- Design principle emerges naturally

### Slide 35 — C3 Synthesis
- Empirical vindication of the representational paradigm
- Not saying GNNs are never useful — task structure determines what works
- **Bold:** For this problem class: *representation first, architecture second*
- Bridge to synthesis: "These three contributions together support a unified design philosophy"

---

## SECTION 7: Synthesis & Contributions Status (4 slides)

### Slide 36 — Cross-Cutting Insights
Five insights labeled clearly:
1. **Representation Over Architecture** — obs schemas matter more than algorithmic sophistication
2. **Task Structure as Critical Moderator** — no universal method; environment determines effectiveness
3. **Unified Sharing Without Interchangeability** — semantic decomposability enables shared learning across structurally distinct agents
4. **Match Methods to Heterogeneity Type** — behavioral → curriculum; structural → homogenization
5. **Emergent Robustness** — deployment flexibility emerges "for free" from representational design

### Slide 37 — HARL Design Principles
Practical takeaways for practitioners:
- Prefer representation-level solutions before adding architectural complexity
- Design obs spaces with *semantic decomposability* in mind from the start
- Use masking/homogenization for flexible team compositions
- Be aware of gradient interference when agents share observation overlap
- Consider task coordination structure before choosing curriculum strategies

### Slide 38 — Contributions Summary (Redux Status Table)
Return to the contributions table from Slide 3, now enriched with key findings:

| Contribution | Central Claim | Key Finding | Implication |
|---|---|---|---|
| **C1: Policy Upsampling** | Pretraining smaller teams can reduce cost | Environment-dependent; strong for Waterworld/Multiwalker, limited for LBF | Task structure governs curriculum benefit |
| **C2: Implicit Indication** | Shared policy without explicit IDs | Matches HAPPO; 1/\|I\| storage; zero-shot robust | Representational design yields emergent robustness |
| **C3: Paradigm Comparison** | Representational > Architectural | 2.3–4.4× advantage over GNN-based PIC | Simple masking beats complex graph aggregation |

### Slide 39 — The Unifying Answer
Return to the thesis statement and show how each contribution supports it:
- C1: even scalability is constrained by *representational choices* (obs coupling)
- C2: heterogeneity is *representable* without explicit structure if obs space is well-designed
- C3: architectural complexity cannot compensate for poor representational design
- **Bold:** DIE-HARL: *Durable* (C3), *Implicit* (C2), *Extensible* (C1)

---

## SECTION 8: Limitations & Future Work (2 slides)

### Slide 40 — Limitations
- Single algorithm family (PPO-based) — results may not generalize to off-policy methods
- Controlled/simulated environments — real-world complexity not yet tested
- Limited team sizes (max 8 agents) — scaling properties under study
- *Semantic decomposability assumption* — not all operational systems will satisfy this
- Discrete action spaces predominantly

### Slide 41 — Future Directions
- Action-space heterogeneity (structural differences in *what agents can do*, not just observe)
- Scaling to larger and dynamically-changing teams
- Hybrid representational + architectural approaches
- Real-world validation (physical platforms, noisy sensors)
- Formal convergence guarantees for implicit indication

---

## SECTION 9: Closing (2 slides)

### Slide 42 — Conclusion
- Restate the dissertation's contribution to HARL
- Single clean graphic: the three-contribution map converging on the unifying thesis
- **Bold:** The path forward for robust, efficient heterogeneous multi-agent systems runs through *representation design*

### Slide 43 — Questions
- Standard "Questions?" slide
- Include contact information / distribution statement
- AFIT crest

---

## BACKUP SLIDES (to prepare but not present unless asked)

| # | Topic | Trigger Question |
|---|---|---|
| B1 | Iteration cost analysis (`iter_cost.png`) | "How much training cost does C1 actually save?" |
| B2 | Formal proof sketch (Deep Sets foundation for C2) | "What's the theoretical basis for implicit indication?" |
| B3 | HAPPO vs. Implicit Indication detail | "How does C2 compare to HAPPO specifically?" |
| B4 | HyperGrid environment detail | "Tell me more about HyperGrid design choices" |
| B5 | Eval heatmaps / box plots (C3) | "Can you break down the robustness conditions?" |
| B6 | Disjoint-span gradient interference hypothesis | "Why does disjoint-span training perform best?" |
| B7 | Smit (2023) comparison | "How does this compare to prior curriculum work?" |
| B8 | Future: action-space heterogeneity detail | "Where are you going with this after graduation?" |

---

## OPEN QUESTIONS FOR BRANDON

1. **Distribution statement**: Should slides be marked UNCLASSIFIED//DISTRIBUTION A, or other?
2. **Committee preferences**: Any known stylistic preferences from Dr. Cox, Dr. Robbins, or Maj Yielding?
3. **Opening hook**: Use the Replicator Initiative quote directly, or a visual-first opening (drone swarm)?
4. **C1 emphasis**: Are there specific sub-findings in C1 you want highlighted or downplayed?
5. **Demo / video**: Is there any live demo or video clip to include (e.g., HyperGrid agents running)?
6. **Acknowledgments slide**: Include before or after title? Separate slide or part of closing?
7. **Color theme**: The defense class supports blue/purple/green for unclassified — preference?
8. **Figures**: Any results figures you'd like regenerated at higher quality or in a different format?
