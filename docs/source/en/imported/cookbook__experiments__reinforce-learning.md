# TCRL vs Tinker Training Performance Comparison

This document presents comparative experiments between TCRL (Tinker Cookbook RL) and Tinker across two benchmarks — **MATH** and **GSM8K** — using the same base model Qwen3-4B-Instruct-2507. The results demonstrate that TCRL and Tinker are essentially equivalent in training performance, validating TCRL as an effective open-source alternative.

## Experiment 1: MATH Dataset[​](\#experiment-1-math-dataset)

### Configuration[​](\#configuration)

- **Model**
  
  : Qwen-Qwen3-4B-Instruct-2507
- **Task**
  
  : Reinforcement learning training on the MATH dataset
- **LoRA Config**
  
  : 32 rank, 2e-05 learning rate
- **Training Config**
  
  : 16 group size, 64 batch size, importance sampling
- **Random Seed**
  
  : 0
- **Training Steps**
  
  : 188 steps

### Key Findings[​](\#key-findings)

TCRL and Tinker achieve nearly identical final performance on the MATH task:

1. **Comparable Final Performance**
  
  : The final rewards on the test set differ by only 0.0036, which is negligible.
2. **Similar Training Dynamics**
  
  : Both exhibit highly consistent trends in training reward growth curves, format accuracy, and correctness metrics.
3. **Consistent KL Divergence**
  
  : Both maintain the same level of KL divergence during training, indicating that TCRL correctly implements importance sampling and policy update logic.

### Detailed Metrics[​](\#detailed-metrics)

#### Final Metrics (Step 187)[​](\#final-metrics-step-187)

| Metric | TCRL | Tinker | Diff (Tinker - TCRL) | Notes |
| --- | --- | --- | --- | --- |
| Train Reward | 0.7738 | 0.7477 | -0.0262 | TCRL slightly higher, diff < 4% |
| Test Reward | 0.7534 | 0.7570 | +0.0036 | Nearly identical, diff < 0.5% |
| Train Correct | 0.7832 | 0.7617 | -0.0215 | TCRL slightly higher |
| Test Correct | 0.7620 | 0.7720 | +0.0100 | Nearly identical |
| Train Format Accuracy | 0.9062 | 0.8594 | -0.0469 | TCRL achieves higher format accuracy |
| Policy Entropy | 0.1104 | 0.0869 | -0.0235 | TCRL explores more thoroughly |
| KL Divergence v1 (kl_v1) | 0.0005 | 0.0005 | +0.0001 | Fully consistent |
| Time per Step (time/total) | 56.47s | 56.30s | -0.17s | Consistent timing at final step |

#### Training Process Statistics[​](\#training-process-statistics)

| Metric | TCRL | Tinker | Notes |
| --- | --- | --- | --- |
| Average Train Reward | 0.6810 | 0.6528 | TCRL's overall training reward is slightly higher |
| Reward Growth | +0.4119 | +0.3817 | Both achieved stable reward improvement |
| Average Time per Step | 121.3s | 63.0s | TCRL takes longer per step; potential for optimization exists |

### Training Dynamics[​](\#training-dynamics)

#### Reward Curves[​](\#reward-curves)

- **Train Rewards**
  
  : Both TCRL and Tinker's train rewards increased from ~0.36 to ~0.76, with gains of +0.41 and +0.38 respectively.
- **Test Rewards**
  
  : Final performance on the test set is nearly identical (0.7534 vs 0.7570), indicating that TCRL does not exhibit significant overfitting.

#### Format & Correctness[​](\#format--correctness)

- **Format Accuracy**
  
  : TCRL's final format accuracy is 90.6%, higher than Tinker's 85.9%, demonstrating that TCRL performs better in generating properly formatted output.
- **Correctness**
  
  : Test set correctness rates are 76.2% and 77.2% respectively — a negligible difference.

#### KL Divergence[​](\#kl-divergence)

- **KL(sampler ‖ trainer)**
  
  : Both maintain a KL divergence of approximately 0.0005, confirming that TCRL correctly implements KL control logic consistent with Tinker, avoiding distribution shift during policy updates.

#### Policy Entropy[​](\#policy-entropy)

- TCRL's policy entropy (0.1104) is slightly higher than Tinker's (0.0869), suggesting that TCRL maintains better exploratory behavior during training, which may help avoid premature convergence to suboptimal policies.

### Training Efficiency[​](\#training-efficiency)

- **Per-step Time (final step):**
  
  Essentially identical between both (~56s)
- **Average Per-step Time:**
  
  TCRL averages 121.3s per step, significantly higher than Tinker's 63.0s (speedup ratio: 1.92x)

**Analysis:** The primary reasons for TCRL's higher average time may be:

1. Longer sampling time in early training steps (TCRL uses remote API sampling, while Tinker may employ more optimized sampling strategies).
2. Lack of certain performance optimizations (such as asynchronous sampling, batching optimizations, etc.).

### Visualization[​](\#visualization)

The figure below shows a comparison of training curves between TCRL and Tinker across 9 key metrics:

*Figure 1: TCRL vs Tinker Training Metrics Comparison on MATH (3×3 panel)*

Panel descriptions:

1. **Train/Test Reward**
  
  : Reward curves on training and test sets
2. **Format & Correct (train/test)**
  
  : Format accuracy and answer correctness rates
3. **Group Composition**
  
  : Proportions of all-correct / mixed / all-incorrect groups within each training batch
4. **Policy Entropy**
  
  : Policy entropy, measuring exploration extent
5. **Gradient Norm**
  
  : Gradient norm (logarithmic scale)
6. **KL Divergence**
  
  : KL divergence, measuring the difference between sampling and training policies
7. **Per-step Time**
  
  : Per-step time breakdown (sampling/training/checkpoint saving)
8. **Tokens per Turn**
  
  : Token counts per turn (actions/observations)

## Experiment 2: GSM8K Dataset[​](\#experiment-2-gsm8k-dataset)

### Configuration[​](\#configuration-1)

- **Model**
  
  : Qwen/Qwen3-4B-Instruct-2507
- **Training Steps**
  
  : 50
- **Date**
  
  : 2026-05-19

### Final Results[​](\#final-results)

| Metric | Tinker | TCRL |
| --- | --- | --- |
| Baseline Accuracy | 0.9100 (91/100) | 0.9300 (93/100) |
| Post-training Accuracy | 0.9300 (93/100) | 0.9200 (92/100) |
| Improvement | +0.0200 | -0.0100 |

### Training Process Comparison[​](\#training-process-comparison)

| Metric | Tinker | TCRL |
| --- | --- | --- |
| Average Reward | ~0.956 | ~0.949 |
| Reward Range | 0.820~1.000 | 0.820~1.000 |
| Degenerate Ratio | 81%~100% | 75%~100% |
| Avg Time per Step | ~12.3s | ~20.0s |
| Total Training Time | ~10min 35s | ~16min 47s |

### Analysis[​](\#analysis)

1. **Baseline Variance**: The baselines differ slightly (91% vs 93%), which falls within normal sampling fluctuation — the difference is only 2 samples.
2. **Minimal Improvement**: Tinker gained +2%, while TCRL dropped -1%. Both changes are within baseline fluctuation range and lack statistical significance.
3. **Training Speed**: Tinker processes each step in ~12.3s vs TCRL's ~20.0s, making Tinker approximately 38% faster. However, this difference may be influenced by runtime load, network conditions, and other environmental factors.
4. **High Degenerate Ratio**: Both exhibit degenerate ratios of 75%~100%, meaning the vast majority of rollouts within each group are identical, resulting in very few effective training datums. This is typical when the model is already very strong on the task — the room for RL improvement is limited.
5. **Late-Training Reward Fluctuation**: Both show reward dips around Steps 36~49, indicating similar stability characteristics.

### Visualization[​](\#visualization-1)

The figure below shows a comparison of training curves between TCRL and Tinker on the GSM8K dataset:

*Figure 2: TCRL vs Tinker Training Metrics Comparison on GSM8K*

### Conclusion[​](\#conclusion)

**There is no significant difference between the two on GSM8K.** The improvements are marginal (+2% vs -1%) and fall within baseline sampling noise, lacking statistical significance. The root cause is that GSM8K is already a high-accuracy task for Qwen3-4B-Instruct-2507 (baseline 91%~93%), leaving the model with almost no rollout diversity (extremely high degenerate ratio) and thus limited marginal benefit from RL training. The two perform comparably.

## Overall Conclusions & Future Work[​](\#overall-conclusions--future-work)

### Conclusions[​](\#conclusions)

1. **TCRL Validated Across Tasks**: On both MATH and GSM8K, TCRL achieves performance essentially equivalent to Tinker — on MATH with near-identical test rewards (diff < 0.5%), and on GSM8K with differences within baseline fluctuation. This validates TCRL as a correct and usable open-source RL training framework.
2. **Highly Consistent Training Dynamics**: Key metrics such as reward growth, format accuracy, KL divergence, and degenerate ratio show highly similar trends between the two, confirming that TCRL correctly implements Tinker's core algorithmic logic.
3. **Room for Optimization**: TCRL's training efficiency can still be improved — it is approximately 1.9× slower on MATH and 1.6× slower on GSM8K compared to Tinker. Further hardware-aware optimization is needed to close this gap.
4. **Task Ceiling Effect**: On high-accuracy tasks like GSM8K where the model already performs well, RL training yields diminishing returns due to high degenerate ratios. This is an inherent characteristic of the task-model combination, not a framework limitation.

### Next Steps[​](\#next-steps)

1. **Performance Optimization**
  
  : Optimize TCRL's sampling and training pipeline with hardware-aware optimizations to improve training efficiency.
2. **Broader Validation**
  
  : Validate TCRL on additional tasks (especially lower-accuracy tasks where RL has more room for improvement) and models.
3. **Feature Enhancement**
  
  : Support more loss functions and training strategies to expand TCRL's applicability.
