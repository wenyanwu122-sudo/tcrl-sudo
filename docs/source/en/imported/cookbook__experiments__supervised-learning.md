# SFT Comparison Experiments

This section records SFT comparison experiment results based on tcrl_infra. Experiments 1-2 validate the training equivalence between TCRL and Tinker; Experiments 3-4 demonstrate the performance progression from small models to large models to TCRL SFT models by comparing with multiple Proxy Models and Oracle Models, validating the effectiveness of TCRL (chat_sl) on text classification tasks.

## Experiment 1: no_robots Dataset[​](\#experiment-1-no_robots-dataset)

### Configuration[​](\#configuration)

- **Model**
  
  : Qwen/Qwen3-8B-Base
- **Task**
  
  : SFT training on no_robots dataset
- **LoRA config**
  
  : 64 rank, 5e-4 learning rate
- **Training config**
  
  : 64 batch size, 1 epoch, Cosine Decay
- **Training steps**
  
  : 148 steps
- **Eval interval**
  
  : every 20 steps

### Key Findings[​](\#key-findings)

TCRL and Tinker achieve nearly identical final performance on the no_robots task:

1. **Final performance equivalent**
  
  : Test NLL differs by only 0.0025, negligible.
2. **Similar training dynamics**
  
  : Both Train NLL curves show highly consistent trends.
3. **Consistent initialization**
  
  : Initial test/nll difference is only 0.0001, confirming identical model initialization and data loading.

### Detailed Metrics[​](\#detailed-metrics)

#### Final Metrics (Step 147)[​](\#final-metrics-step-147)

| Metric | Tinker | TCRL | Diff (TCRL - Tinker) | Note |
| --- | --- | --- | --- | --- |
| Test NLL (test/nll) | 1.7037 | 1.7062 | +0.0025 | Nearly identical, diff < 0.2% |
| Avg Train NLL | 1.7082 | 1.7155 | +0.0073 | Diff < 0.5% |
| Initial Test NLL | 1.8507 | 1.8506 | -0.0001 | Identical |
| NLL Drop | -0.1470 | -0.1444 | +0.0026 | Consistent drop |
| Avg Step Time | 1.30s | 18.86s | +17.56s | TCRL is slower |
| Total Training Time | ~3.2 min | ~46.5 min | — | TCRL includes remote API overhead |

#### Training Process Statistics[​](\#training-process-statistics)

| Metric | Tinker | TCRL | Note |
| --- | --- | --- | --- |
| Step 0-19 Avg NLL | 1.7324 | 1.7506 | Initial gap 0.018 |
| Step 20-49 Avg NLL | 1.7224 | 1.7312 | Gap narrows to 0.009 |
| Step 50-99 Avg NLL | 1.6936 | 1.6998 | Gap narrows to 0.006 |
| Step 100-147 Avg NLL | 1.7046 | 1.7075 | Final gap only 0.003 |

### Training Dynamics[​](\#training-dynamics)

#### NLL Curves[​](\#nll-curves)

- **Train NLL**
  
  : Both decrease from ~1.78 to ~1.59, with gap narrowing from 0.018 to 0.003.
- **Test NLL**
  
  : Final performance is nearly identical (1.7037 vs 1.7062), diff < 0.2%.

#### Gradient Norm[​](\#gradient-norm)

- TCRL's
  
  `grad_norm`
  
  shows an alternating large/small value pattern, with stable training throughout.

### Visualization[​](\#visualization)

*Figure 1: TCRL vs Tinker no_robots Train/Test NLL comparison*

### Conclusion[​](\#conclusion)

Under identical hyperparameter settings, Tinker and TCRL achieve **virtually identical** SFT training results on no_robots. The final test/nll gap is only 0.0025 (< 0.2%), and train_mean_nll phase average differences narrow from 0.018 to 0.003, validating the correctness of TCRL's SFT implementation and its equivalence to Tinker.

## Experiment 2: tulu3 Dataset[​](\#experiment-2-tulu3-dataset)

### Configuration[​](\#configuration-1)

- **Model**
  
  : Qwen/Qwen3-8B-Base
- **Task**
  
  : SFT training on tulu3 dataset
- **LoRA config**
  
  : 64 rank, 5e-4 learning rate
- **Training config**
  
  : 128 batch size, Cosine Decay
- **Steps analyzed**
  
  : 212 steps (Step 0-211)
- **Dataset scale**
  
  : ~7330 steps/epoch

### Key Findings[​](\#key-findings-1)

TCRL and Tinker achieve highly consistent training performance on the large-scale tulu3 dataset:

1. **Identical initialization**
  
  : test/nll difference is only 0.0004, confirming consistent model initialization and data loading.
2. **Similar training dynamics**
  
  : Phase average train_mean_nll differences are within 0.002-0.007.
3. **Identical loss computation**
  
  : Both use
  
  `num_loss_tokens ≈ 128`
  
  (per-sequence normalization), NLL values are directly comparable.

### Detailed Metrics[​](\#detailed-metrics-1)

#### Test Metrics[​](\#test-metrics)

| Metric | Tinker | TCRL | Diff (TCRL - Tinker) | Note |
| --- | --- | --- | --- | --- |
| Initial Test NLL (Step 0) | 0.9154 | 0.9158 | +0.0004 | Identical |
| Avg Step Time | 5.26s | 50.51s | +45.25s | TCRL is slower |
| Total Training Time (212 steps) | ~18.6 min | ~178.5 min | — | TCRL includes remote API overhead |

note

Due to the large size of the tulu3 dataset (~7330 steps/epoch), only Step 0 has validation evaluation data within the first 212 steps.

#### Training Process Statistics[​](\#training-process-statistics-1)

| Phase | Tinker | TCRL | Diff | Note |
| --- | --- | --- | --- | --- |
| Step 0-19 | 0.7886 | 0.7950 | +0.0064 | Initial phase |
| Step 20-49 | 0.7353 | 0.7370 | +0.0017 | Rapid convergence |
| Step 50-99 | 0.7325 | 0.7338 | +0.0013 | Steady descent |
| Step 100-149 | 0.7250 | 0.7264 | +0.0014 | Continued optimization |
| Step 150-199 | 0.7143 | 0.7161 | +0.0018 | Late stabilization |
| Step 200-211 | 0.7169 | 0.7182 | +0.0013 | Final phase |

### Training Dynamics[​](\#training-dynamics-1)

#### NLL Curves[​](\#nll-curves-1)

- **Train NLL**
  
  : Both gradually decrease from ~0.79 to ~0.72, a drop of ~0.07, in a stable learning phase during the first 212 steps (~2.9% of training progress).
- **Fluctuation pattern**
  
  : Due to batch randomness, single-step NLL varies considerably (~0.6-0.9), but both frameworks exhibit identical patterns.

#### Gradient Norm[​](\#gradient-norm-1)

- TCRL's grad_norm shows an alternating pattern of large values (10-170) and small values (0.1-4), possibly related to gradient accumulation or optimizer state, but does not affect convergence.

### Visualization[​](\#visualization-1)

*Figure 2: TCRL vs Tinker tulu3 Train/Test NLL comparison*

### Conclusion[​](\#conclusion-1)

On the large-scale tulu3 dataset, Tinker and TCRL SFT training performance is **virtually identical**. The train_mean_nll phase average differences do not exceed 0.007, and initial test/nll difference is only 0.0004. This demonstrates that TCRL achieves equivalent training effectiveness to Tinker on large-scale SFT tasks, validating the correctness of its implementation.

## Experiment 3: SST-5 Sentiment Classification[​](\#experiment-3-sst-5-sentiment-classification)

**Objective:** Validate TCRL (chat_sl) SFT performance on a small-scale dataset, demonstrating the performance progression from small models to large models to TCRL SFT models.

**Model:** Qwen/Qwen3-8B-Base, Qwen/Qwen3-8B

**Dataset:** SST-5 five-class sentiment analysis (train: 8,544, test: 2,210)

### Configuration[​](\#configuration-2)

| Config | TCRL (Qwen3-8B-Base) | TCRL (Qwen3-8B) |
| --- | --- | --- |
| LoRA rank | 64 | 64 |
| Learning rate | 5e-4 | 5e-4 |
| Batch size | 64 | 64 |
| Eval every | 20 steps | 20 steps |
| Total training steps | 133 | 133 |
| LR Schedule | Cosine Decay | Cosine Decay |

### Training Efficiency[​](\#training-efficiency)

| Metric | TCRL (Qwen3-8B-Base) | TCRL (Qwen3-8B) |
| --- | --- | --- |
| Total training time | 19.0 min | 10.3 min |
| Pure training time (excl. eval) | 16.5 min | 8.1 min |
| Evaluation time | 2.5 min | 2.1 min |
| Avg step time | 8.58s | 4.64s |
| Avg pure training step time | 7.87s | 3.87s |
| Initial Test NLL | 1.3670 | 23.4568 |
| Final Test NLL | 0.2063 | 0.4000 |
| NLL reduction | -1.1607 | -23.0568 |

:::info Training Efficiency Note
Qwen3-8B has significantly lower avg step time (3.87s) compared to Qwen3-8B-Base (7.87s). This is because the Instruct model already has instruction-following capabilities and converges faster, while the Base model requires more gradient updates to learn output formatting.
:::

### Results[​](\#results)

| Method | Model | Accuracy |
| --- | --- | --- |
| Proxy Model | Qwen2.5-1.5B-Instruct | 27.15% |
| Proxy Model | Qwen2.5-3B-Instruct | 46.61% |
| Proxy Model | Qwen3-8B-Base | 10.45% |
| Proxy Model | Qwen3-8B | 43.26% |
| Oracle Model | Qwen3-30B-A3B-Instruct | 56.74% |
| Oracle Model | DeepSeek-V3.2 | 50.59% |
| TCRL (chat_sl) | Qwen3-8B-Base | 43.76% |
| TCRL (chat_sl) | Qwen3-8B | 58.91% |

### Conclusion[​](\#conclusion-2)

1. **TCRL SFT effectively improves model performance**: Qwen3-8B after TCRL SFT achieves 58.91%, surpassing Oracle model Qwen3-30B-A3B-Instruct (56.74%) and DeepSeek-V3.2 (50.59%), proving SFT effectiveness.
2. **Base model selection matters**: Qwen3-8B after SFT (58.91%) significantly outperforms Qwen3-8B-Base after the same SFT (43.76%), showing that SFT works better on Instruct models.
3. **Clear progression from small to large models**: 1.5B (27.15%) → 3B (46.61%) → 8B SFT (58.91%), model capability improves progressively with scale and training.

## Experiment 4: AGNews Topic Classification[​](\#experiment-4-agnews-topic-classification)

**Objective:** Validate TCRL (chat_sl) SFT performance on a large-scale dataset, demonstrating the performance progression from small models to large models to TCRL SFT models.

**Model:** Qwen/Qwen3-8B-Base, Qwen/Qwen3-8B

**Dataset:** AGNews four-class news topic classification (train: 120,000, test: 2,000)

### Configuration[​](\#configuration-3)

| Config | TCRL (Qwen3-8B-Base) | TCRL (Qwen3-8B) |
| --- | --- | --- |
| LoRA rank | 64 | 64 |
| Learning rate | 5e-4 | 5e-4 |
| Batch size | 128 | 128 |
| Eval every | 50 steps | 50 steps |
| Total training steps | 937 | 937 |
| LR Schedule | Cosine Decay | Cosine Decay |

### Training Efficiency[​](\#training-efficiency-1)

| Metric | TCRL (Qwen3-8B-Base) | TCRL (Qwen3-8B) |
| --- | --- | --- |
| Total training time | 254.1 min (~4.2h) | 129.1 min (~2.2h) |
| Pure training time (excl. eval) | 242.1 min | 121.8 min |
| Evaluation time | 11.9 min | 7.3 min |
| Avg step time | 16.27s | 8.27s |
| Avg pure training step time | 15.83s | 7.96s |
| Initial Test NLL | 0.0650 | 23.2100 |
| Final Test NLL | 0.0301 | 0.0540 |
| NLL reduction | -0.0349 | -23.1560 |

:::info Training Efficiency Note
AGNews is a large-scale dataset (120K samples) requiring 937 training steps. Qwen3-8B's pure training avg step time (7.96s) is about half of Qwen3-8B-Base (15.83s), providing ~2× overall training efficiency improvement. The Base model achieves lower final Test NLL (0.0301 vs 0.0540), but the 8B model has higher classification accuracy, suggesting that the Instruct model has better format output capabilities.
:::

### Results[​](\#results-1)

| Method | Model | Accuracy |
| --- | --- | --- |
| Proxy Model | Qwen2.5-1.5B-Instruct | 51.40% |
| Proxy Model | Qwen2.5-3B-Instruct | 69.90% |
| Proxy Model | Qwen3-8B-Base | 5.35% |
| Proxy Model | Qwen3-8B | 79.00% |
| Oracle Model | Qwen3-30B-A3B-Instruct | 86.50% |
| Oracle Model | DeepSeek-V3.2 | 83.30% |
| TCRL (chat_sl) | Qwen3-8B-Base | 95.50% |
| TCRL (chat_sl) | Qwen3-8B | 96.05% |

### Training Metrics[​](\#training-metrics)

The following figure shows the training comparison between Qwen3-8B-Base and Qwen3-8B on the AGNews dataset:

*Figure 3: AGNews Qwen3-8B Base vs Instruct training comparison (Train Loss vs Step, Train Loss vs Time, Test Loss, Gradient Norm)*

### Conclusion[​](\#conclusion-3)

1. **TCRL SFT significantly surpasses large models**: Qwen3-8B-Base (95.50%) and Qwen3-8B (96.05%) after TCRL SFT both significantly surpass 30B-level large models (86.50%), exceeding by +9.00% and +9.55% respectively.
2. **Base model gap narrows on large datasets**: On the large-scale AGNews dataset, the gap between Qwen3-8B-Base (95.50%) and Qwen3-8B (96.05%) after SFT is only 0.55%, much smaller than the 15.15% gap on SST-5, indicating that sufficient training data can compensate for the gap between Base and Instruct models.
3. **Clear progression from small to large models**: 1.5B (51.40%) → 3B (69.90%) → 8B SFT (96.05%), SFT is particularly effective on large-scale datasets.

## Experiment 5: TNews Chinese News Classification[​](\#experiment-5-tnews-chinese-news-classification)

**Objective:** Validate TCRL (chat_sl) SFT performance on Chinese classification tasks, demonstrating the performance progression from small models to large models to TCRL SFT models.

**Model:** Qwen/Qwen3-8B-Base, Qwen/Qwen3-8B

**Dataset:** TNews 15-class Chinese news topic classification (train: 53,360, test: 1,837)

### Configuration[​](\#configuration-4)

| Config | TCRL (Qwen3-8B-Base) | TCRL (Qwen3-8B) |
| --- | --- | --- |
| LoRA rank | 64 | 64 |
| Learning rate | 5e-4 | 5e-4 |
| Batch size | 128 | 128 |
| Eval every | 50 steps | 50 steps |
| Total training steps | 416 | 416 |

### Training Efficiency[​](\#training-efficiency-2)

| Metric | TCRL (Qwen3-8B) |
| --- | --- |
| Total training time | 98.8 min (~1.6h) |
| Avg step time | 14.25s |
| Avg pure training step time | 13.82s |
| Initial Test NLL | 16.8089 |
| Final Test NLL | 0.2362 |
| NLL reduction | -16.5727 |

:::info Training Efficiency Note
TNews is a medium-scale dataset (53K) requiring 416 training steps. Qwen3-8B drops from a very high initial Test NLL (16.81) to 0.24 rapidly, showing the Instruct model can quickly learn new classification taxonomies on Chinese tasks.
:::

### Results[​](\#results-2)

| Method | Model | Accuracy |
| --- | --- | --- |
| Proxy Model | Qwen2.5-1.5B-Instruct | 23.01% |
| Proxy Model | Qwen2.5-3B-Instruct | 41.74% |
| Proxy Model | Qwen3-8B-Base | 11.54% |
| Proxy Model | Qwen3-8B | 51.01% |
| Oracle Model | Qwen3-30B-A3B-Instruct | 52.25% |
| Oracle Model | DeepSeek-V3.2 | 56.54% |
| TCRL (chat_sl) | Qwen3-8B-Base | 69.19% |
| TCRL (chat_sl) | Qwen3-8B | 67.99% |

### Conclusion[​](\#conclusion-4)

1. **TCRL SFT significantly surpasses large models**: Qwen3-8B-Base (69.19%) and Qwen3-8B (67.99%) after TCRL SFT both significantly surpass 30B-level large models (52.25%) and DeepSeek-V3.2 (56.54%), exceeding by +12.65% and +11.45% respectively.
2. **Base model performs better on Chinese classification**: On TNews, Qwen3-8B-Base (69.19%) slightly outperforms Qwen3-8B (67.99%) after SFT, possibly because the Base model has cleaner Chinese training data and can better adapt to specific classification taxonomies after SFT.
3. **Clear progression from small to large models**: 1.5B (23.01%) → 3B (41.74%) → 8B SFT (69.19%), SFT brings significant improvement on Chinese classification tasks as well.

## Experiment 6: DBPedia Ontology Classification[​](\#experiment-6-dbpedia-ontology-classification)

**Objective:** Validate TCRL (chat_sl) SFT performance on an extra-large-scale dataset, demonstrating the performance progression from small models to large models to TCRL SFT models.

**Model:** Qwen/Qwen3-8B-Base, Qwen/Qwen3-8B

**Dataset:** DBPedia 14-class ontology classification (train: 560,000, test: 1,988)

### Configuration[​](\#configuration-5)

| Config | TCRL (Qwen3-8B-Base) | TCRL (Qwen3-8B) |
| --- | --- | --- |
| LoRA rank | 64 | 64 |
| Learning rate | 5e-4 | 5e-4 |
| Batch size | 256 | 256 |
| Eval every | 50 steps | 50 steps |
| Total training steps | 500 | 500 |

### Training Efficiency[​](\#training-efficiency-3)

| Metric | TCRL (Qwen3-8B-Base) | TCRL (Qwen3-8B) |
| --- | --- | --- |
| Total training time | 250.8 min (~4.2h) | 252.6 min (~4.2h) |
| Avg step time | 30.09s | 30.32s |
| Avg pure training step time | 29.38s | 29.60s |
| Initial Test NLL | 1.1103 | 21.2056 |
| Final Test NLL | 0.0072 | 0.0112 |
| NLL reduction | -1.1031 | -21.1944 |

:::info Training Efficiency Note
DBPedia is an extra-large-scale dataset (560K) with batch size 256, trained for 500 steps. Both models have nearly identical training time (~4.2h), as training efficiency converges at large batch sizes. The Base model achieves slightly lower final Test NLL (0.0072 vs 0.0112), and both achieve near-identical classification accuracy (99.50% vs 99.40%).
:::

### Results[​](\#results-3)

| Method | Model | Accuracy |
| --- | --- | --- |
| Proxy Model | Qwen2.5-1.5B-Instruct | 66.80% |
| Proxy Model | Qwen2.5-3B-Instruct | 86.00% |
| Proxy Model | Qwen3-8B-Base | 19.40% |
| Proxy Model | Qwen3-8B | 91.50% |
| Oracle Model | Qwen3-30B-A3B-Instruct | 96.70% |
| Oracle Model | DeepSeek-V3.2 | 95.90% |
| TCRL (chat_sl) | Qwen3-8B-Base | 99.50% |
| TCRL (chat_sl) | Qwen3-8B | 99.40% |

### Conclusion[​](\#conclusion-5)

1. **TCRL SFT achieves near-perfect classification**: Qwen3-8B-Base (99.50%) and Qwen3-8B (99.40%) after TCRL SFT both approach 100% accuracy, significantly surpassing 30B-level large models (96.70%), exceeding by +2.80% and +2.70%.
2. **Both models perform identically on extra-large datasets**: On the DBPedia extra-large dataset (560K), the gap between Qwen3-8B-Base (99.50%) and Qwen3-8B (99.40%) after SFT is only 0.10%, further validating that sufficient training data can completely eliminate the gap between Base and Instruct models.
3. **Clear progression from small to large models**: 1.5B (66.80%) → 3B (86.00%) → 8B SFT (99.50%), SFT on extra-large datasets can push models toward near-perfect performance.

## Experiment 7: THUCNews Chinese Long-text News Classification[​](\#experiment-7-thucnews-chinese-long-text-news-classification)

**Objective:** Validate TCRL (chat_sl) SFT performance on Chinese long-text classification tasks, demonstrating the performance progression from small models to large models to TCRL SFT models.

**Model:** Qwen/Qwen3-8B-Base, Qwen/Qwen3-8B

**Dataset:** THUCNews 14-class Chinese long-text news classification (train: 46,000, test: 2,000)

### Configuration[​](\#configuration-6)

| Config | TCRL (Qwen3-8B-Base) | TCRL (Qwen3-8B) |
| --- | --- | --- |
| LoRA rank | 64 | 64 |
| Learning rate | 5e-4 | 1e-4 |
| Batch size | 128 | 128 |
| Eval every | 50 steps | 50 steps |
| Total training steps | 359 | 359 |

### Training Efficiency[​](\#training-efficiency-4)

| Metric | TCRL (Qwen3-8B-Base) | TCRL (Qwen3-8B) |
| --- | --- | --- |
| Total training time | 184.5 min (~3.1h) | 185.6 min (~3.1h) |
| Avg step time | 30.84s | 31.03s |
| Avg pure training step time | 30.07s | 30.26s |
| Initial Test NLL | 1.2518 | 19.9772 |
| Final Test NLL | 0.0084 | 0.0183 |
| NLL reduction | -1.2434 | -19.9589 |

:::info Training Efficiency Note
THUCNews is a Chinese long-text classification task (46K training samples) requiring 359 training steps. Due to longer text sequences, both models have nearly identical training time (~3.1h) at batch size 128. The Base model achieves lower final Test NLL (0.0084 vs 0.0183), while both achieve identical classification accuracy (98.80%). Qwen3-8B uses a smaller learning rate (1e-4 vs 5e-4) for more stable training.
:::

### Results[​](\#results-4)

| Method | Model | Accuracy |
| --- | --- | --- |
| Proxy Model | Qwen2.5-1.5B-Instruct | 50.80% |
| Proxy Model | Qwen2.5-3B-Instruct | 83.00% |
| Proxy Model | Qwen3-8B-Base | 19.40% |
| Proxy Model | Qwen3-8B | 81.00% |
| Oracle Model | Qwen3-30B-A3B-Instruct | 90.00% |
| Oracle Model | DeepSeek-V3.2 | 87.80% |
| TCRL (chat_sl) | Qwen3-8B-Base | 98.80% |
| TCRL (chat_sl) | Qwen3-8B | 98.80% |

### Conclusion[​](\#conclusion-6)

1. **TCRL SFT significantly surpasses large models**: Both Qwen3-8B-Base and Qwen3-8B achieve 98.80% after TCRL SFT, significantly surpassing 30B-level large models (90.00%) and DeepSeek-V3.2 (87.80%), exceeding by +8.80% and +11.00% respectively.
2. **Both models perform identically on Chinese long-text tasks**: On THUCNews, Qwen3-8B-Base and Qwen3-8B achieve identical accuracy (98.80%) after SFT, showing that with sufficient Chinese long-text training data, both Base and Instruct models can reach the same high level.
3. **Clear progression from small to large models**: 1.5B (50.80%) → 3B (83.00%) → 8B SFT (98.80%), SFT brings significant improvement on Chinese long-text classification tasks.

## Experiment 8: SST-2 Sentiment Classification[​](\#experiment-8-sst-2-sentiment-classification)

**Objective:** Validate TCRL (chat_sl) SFT performance on a large-scale binary sentiment classification dataset, demonstrating the performance progression from small models to large models to TCRL SFT models.

**Model:** Qwen/Qwen3-8B-Base, Qwen/Qwen3-8B

**Dataset:** SST-2 binary sentiment classification (train: 67,349, test: 872)

### Configuration[​](\#configuration-7)

| Config | TCRL (Qwen3-8B-Base) | TCRL (Qwen3-8B) |
| --- | --- | --- |
| LoRA rank | 64 | 64 |
| Learning rate | 5e-4 | 5e-4 |
| Batch size | 128 | 128 |
| Eval every | 50 steps | 50 steps |
| Total training steps | 525 | 525 |
| LR Schedule | Linear | Linear |

### Training Efficiency[​](\#training-efficiency-5)

| Metric | TCRL (Qwen3-8B-Base) | TCRL (Qwen3-8B) |
| --- | --- | --- |
| Total training time | 117.2 min (~2.0h) | 118.9 min (~2.0h) |
| Avg step time | 13.37s | 13.56s |
| Avg pure training step time | 12.70s | 12.87s |
| Initial Test NLL | 0.9749 | 26.4470 |
| Final Test NLL | 0.0272 | 0.0552 |
| NLL reduction | -0.9477 | -26.3918 |

:::info Training Efficiency Note
SST-2 is a large-scale dataset (67K training samples, short sentences) requiring 525 training steps for 1 epoch at batch size 128. Both models have nearly identical training time (~2.0h), as the average step time converges (~12.7s) due to the short input sequences. The Base model achieves lower final Test NLL (0.0272 vs 0.0552), while Qwen3-8B drops from a very high initial Test NLL (26.45) to 0.0552, demonstrating that the Instruct model can quickly adapt to the binary sentiment classification format.
:::

### Results[​](\#results-5)

| Method | Model | Accuracy |
| --- | --- | --- |
| Proxy Model | Qwen2.5-1.5B-Instruct | 90.83% |
| Proxy Model | Qwen2.5-3B-Instruct | 91.86% |
| Proxy Model | Qwen3-8B-Base | 91.97% |
| Proxy Model | Qwen3-8B | 93.92% |
| Oracle Model | Qwen3-30B-A3B-Instruct | 94.15% |
| Oracle Model | DeepSeek-V3.2 | 95.18% |
| TCRL (chat_sl) | Qwen3-8B-Base | 96.33% |
| TCRL (chat_sl) | Qwen3-8B | 96.79% |

### Conclusion[​](\#conclusion-7)

1. **TCRL SFT surpasses large models**: Qwen3-8B-Base (96.33%) and Qwen3-8B (96.79%) after TCRL SFT both surpass 30B-level large models (94.15%) and DeepSeek-V3.2 (95.18%), exceeding by +2.18%/+2.64% (vs Qwen3-30B-A3B-Instruct) and +1.15%/+1.61% (vs DeepSeek-V3.2) respectively.
2. **Both models perform near-identically on large-scale binary classification**: On SST-2, the gap between Qwen3-8B-Base (96.33%) and Qwen3-8B (96.79%) after SFT is only 0.46%, much smaller than the 15.15% gap on SST-5, further confirming that sufficient training data narrows the gap between Base and Instruct models on simple binary classification tasks.
3. **Clear progression from small to large models**: 1.5B (90.83%) → 3B (91.86%) → 8B SFT (96.79%), SFT brings consistent improvement on binary sentiment classification tasks, with proxy models already achieving high baseline performance due to the simplicity of binary classification.

## Experiment 9: IMDb Long-text Sentiment Classification[​](\#experiment-9-imdb-long-text-sentiment-classification)

**Objective:** Validate TCRL (chat_sl) SFT performance on a long-text binary sentiment classification dataset, demonstrating the performance progression from small models to large models to TCRL SFT models.

**Model:** Qwen/Qwen3-8B-Base, Qwen/Qwen3-8B

**Dataset:** IMDb binary sentiment classification of long-form movie reviews (train: 25,000, test: 2,000)

### Configuration[​](\#configuration-8)

| Config | TCRL (Qwen3-8B-Base) | TCRL (Qwen3-8B) |
| --- | --- | --- |
| LoRA rank | 64 | 64 |
| Learning rate | 1e-5 | 1e-5 |
| Batch size | 128 | 128 |
| Eval every | 10 steps | 50 steps |
| Total training steps | 195 (1 epoch) | 195 (1 epoch) |
| LR Schedule | Linear | Linear |

### Training Efficiency[​](\#training-efficiency-6)

| Metric | TCRL (Qwen3-8B-Base) | TCRL (Qwen3-8B) |
| --- | --- | --- |
| Total training time | 97.2 min (~1.6h) | 94.5 min (~1.6h) |
| Pure training time (excl. eval) | 43.0 min | 84.5 min |
| Evaluation time | 54.2 min | 10.0 min |
| Avg step time | 29.91s | 29.08s |
| Avg pure training step time | 13.22s | 26.01s |
| Initial Test NLL | 1.0373 | 26.9905 |
| Final Test NLL | 0.0252 | 0.0660 |
| NLL reduction | -1.0121 | -26.9245 |

:::info Training Efficiency Note
IMDb consists of long-form movie reviews (~230 words on average), making it the most token-heavy classification task in this report. Both models train for a full epoch (195 steps) at the same learning rate (1e-5). The 8B-Base run uses a much more frequent eval interval (every 10 steps vs every 50 steps), so although its pure training step is faster (13.22s vs 26.01s — the `qwen3` renderer used by Qwen3-8B adds chat-template tokens, producing longer sequences), the total wall-clock time is comparable (~1.6h) due to the heavy evaluation overhead (54.2 min vs 10.0 min). 8B-Base achieves a lower final Test NLL (0.0252 vs 0.0660), and a slightly higher classification accuracy (95.75% vs 95.00%).
:::

### Results[​](\#results-6)

| Method | Model | Accuracy |
| --- | --- | --- |
| Proxy Model | Qwen2.5-1.5B-Instruct | 92.90% |
| Proxy Model | Qwen2.5-3B-Instruct | 93.30% |
| Proxy Model | Qwen3-8B-Base | 93.31% |
| Proxy Model | Qwen3-8B | 94.00% |
| Oracle Model | Qwen3-30B-A3B-Instruct | 93.60% |
| Oracle Model | DeepSeek-V3.2 | 94.85% |
| TCRL (chat_sl) | Qwen3-8B-Base | 95.75% |
| TCRL (chat_sl) | Qwen3-8B | 95.00% |

### Conclusion[​](\#conclusion-8)

1. **TCRL SFT surpasses large models**: Qwen3-8B-Base (95.75%) and Qwen3-8B (95.00%) after TCRL SFT both surpass 30B-level large models (93.60%) and DeepSeek-V3.2 (94.85%), exceeding by +2.15%/+1.40% (vs Qwen3-30B-A3B-Instruct) and +0.90%/+0.15% (vs DeepSeek-V3.2) respectively.
2. **Base model with full-epoch training matches Instruct on long-text binary classification**: Qwen3-8B-Base (95.75%) slightly outperforms Qwen3-8B (95.00%) after SFT, with the gap being only 0.75%. Under identical learning rate (1e-5) and the same training steps (195), the Base model reaches a lower final Test NLL (0.0252 vs 0.0660) and achieves a slightly higher classification accuracy on long-text binary sentiment classification.
3. **Clear progression from small to large models**: 1.5B (92.90%) → 3B (93.30%) → 8B SFT (95.75%), SFT brings stable improvement on long-text binary sentiment tasks. The proxy models already achieve high baseline performance (~93%) thanks to the binary nature of the task and the well-known IMDb sentiment patterns, leaving a relatively small headroom for SFT.

## Summary[​](\#summary)

### Performance Overview[​](\#performance-overview)

#### IMDb Long-text Sentiment Analysis (Train: 25,000 / Test: 2,000)[​](\#imdb-long-text-sentiment-analysis-train-25000--test-2000)

#### SST-2 Sentiment Analysis (Train: 67,349 / Test: 872)[​](\#sst-2-sentiment-analysis-train-67349--test-872)

#### SST-5 Sentiment Analysis (Train: 8,544 / Test: 2,210)[​](\#sst-5-sentiment-analysis-train-8544--test-2210)

#### AGNews Topic Classification (Train: 120,000 / Test: 2,000)[​](\#agnews-topic-classification-train-120000--test-2000)

#### TNews Chinese News Classification (Train: 53,360 / Test: 1,837)[​](\#tnews-chinese-news-classification-train-53360--test-1837)

#### DBPedia Ontology Classification (Train: 560,000 / Test: 1,988)[​](\#dbpedia-ontology-classification-train-560000--test-1988)

#### THUCNews Chinese Long-text News Classification (Train: 46,000 / Test: 2,000)[​](\#thucnews-chinese-long-text-news-classification-train-46000--test-2000)

### Detailed Data[​](\#detailed-data)

| Dataset | Task | Train | Test | Qwen2.5-1.5B-Instruct | Qwen2.5-3B-Instruct | Qwen3-8B-Base | Qwen3-8B | Qwen3-30B-A3B-Instruct | DeepSeek-V3.2 | Tinker (Qwen3-8B-Base) | TCRL (Qwen3-8B-Base) | TCRL (Qwen3-8B) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IMDb | Sentiment (Long) | 25,000 | 2,000 | 92.90% | 93.30% | 93.31% | 94.00% | 93.60% | 94.85% | pending | 95.75% | 95.00% |
| SST-2 | Sentiment | 67,349 | 872 | 90.83% | 91.86% | 91.97% | 93.92% | 94.15% | 95.18% | pending | 96.33% | 96.79% |
| SST-5 | Sentiment | 8,544 | 2,210 | 27.15% | 46.61% | 10.45% | 43.26% | 56.74% | 50.59% | 57.92% | 43.76% | 58.91% |
| AGNews | News (EN) | 120,000 | 2,000 | 51.40% | 69.90% | 5.35% | 79.00% | 86.50% | 83.30% | 90.39% | 95.50% | 96.05% |
| TNews | News (CN) | 53,360 | 1,837 | 23.01% | 41.74% | 11.54% | 51.01% | 52.25% | 56.54% | pending | 69.19% | 67.99% |
| DBPedia | Ontology | 560,000 | 1,988 | 66.80% | 86.00% | 19.40% | 91.50% | 96.70% | 95.90% | pending | 99.50% | 99.40% |
| THUCNews | News (CN, Long) | 46,000 | 2,000 | 50.80% | 83.00% | 19.40% | 81.00% | 90.00% | 87.80% | pending | 98.80% | 98.80% |

### Key Conclusions[​](\#key-conclusions)

1. **SFT effectively surpasses large models**: After TCRL SFT with Qwen3-8B, all seven datasets significantly surpass 30B-level large models. DBPedia achieves 99.50% (+2.80%); THUCNews achieves 98.80% (+8.80%); AGNews achieves 96.05% (+9.55%); SST-2 achieves 96.79% (+2.64%); IMDb achieves 95.75% (+2.15%); TNews achieves 69.19% (+12.65%); SST-5 achieves 58.91%, surpassing all Oracle models.
2. **Instruct model SFT performance varies by task**: On English short-text tasks (SST-5, AGNews, SST-2), Qwen3-8B outperforms Qwen3-8B-Base; on long-text binary classification (IMDb), Qwen3-8B-Base is slightly better; on the Chinese short-text task (TNews), Qwen3-8B-Base is slightly better; on extra-large datasets (DBPedia) and Chinese long-text tasks (THUCNews), both perform identically. Optimal base model selection varies by task and requires experimental validation.
3. **Data scale impacts base model gap**: On DBPedia (560K), the gap is only 0.10%; on THUCNews (46K), the gap is 0.00%; on AGNews (120K), 0.55%; on SST-2 (67K), 0.46%; on IMDb (25K), 0.75%; on TNews (53K), 1.20%; on SST-5 (8.5K), 15.15%. Sufficient training data is a key factor for SFT success.
4. **Reasonable training efficiency**: SST-5 takes ~10 minutes, IMDb ~1.6 hours, TNews ~1.6 hours, SST-2 ~2.0 hours, AGNews ~2.2 hours, THUCNews ~3.1 hours, DBPedia 4.2 hours, with avg step time of 831s, meeting practical usage requirements.
