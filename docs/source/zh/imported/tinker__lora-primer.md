# LoRA 入门

Tinker 支持 [LoRA 微调](https://arxiv.org/abs/2106.09685)——仅调整少量参数，而非全量微调中调整原始模型的所有参数。

## 关键发现[​](\#关键发现)

目前的理解是：在 RL 或小规模 SL 数据集上，LoRA 与全量微调性能相当；在更大规模数据集上，LoRA 性能较弱。具体而言：

- 在中小规模的指令微调和推理数据集上，LoRA 与全量微调性能相同。
- 当数据集超过 LoRA 容量时，LoRA 不如全量微调。损失不会达到一个明确的下限，而是训练效率下降，取决于模型容量与数据集大小的关系。
- 在某些场景下，LoRA 对大 batch size 的容忍度低于全量微调——超过某个阈值后损失惩罚更大。增大 LoRA rank 不能缓解此问题，这是矩阵乘积参数化的固有属性。
- 即使在小数据场景下，将 LoRA 应用于所有权重矩阵（尤其是 MLP 和 MoE 层）效果更好。仅对 Attention 做 LoRA 效果较差，即使提高 rank 以匹配参数量也不够。
- RL 中即使使用小 rank，LoRA 与全量微调性能也相当。RL 所需的模型容量很低，这与信息论分析一致。

更多细节和实验结果见 [LoRA Without Regret](https://thinkingmachines.ai/blog/lora)。

## 超参数[​](\#超参数)

学习率（LR）通常是 ML 实验中最重要的超参数。

LoRA 需要比全量微调大得多的 LR——通常大 20-100 倍，取决于模型大小。常见错误是在迁移到 LoRA 时保留了全量微调的 LR，导致误认为 LoRA 效果差。

**计算正确的 LoRA 学习率：**

```
from tinker_cookbook.hyperparam_utils import get_lora_lr_over_full_finetune_lrmodel_name = "meta-llama/Llama-3.1-8B"print(get_lora_lr_over_full_finetune_lr(model_name))
```

注意：`Llama-3.2-1B` 的系数为 32，而 `Llama-3.1-70B` 的系数为 128。

## LoRA 究竟是什么？[​](\#lora-究竟是什么)

LoRA 全称 Low-Rank Adaptation。原始模型有权重矩阵 WWW，我们将其替换为 W′=W+BAW'=W + BAW′=W+BA，其中 BBB 和 AAA 是低秩矩阵。若 WWW 是 n×nn \times nn×n 矩阵，则 BBB 和 AAA 分别为 n×rn \times rn×r 和 r×nr \times nr×n 矩阵，rrr 为低秩近似的秩。Tinker 默认 rank 为 32。

LoRA 使用低秩近似这一事实并不关键。我们更倾向于将 LoRA 视为参数空间的一个随机投影，恰好可以高效实现。在 RL 或小规模 SL 训练中，我们只学习少量信息，缩减的参数集绰绰有余。

## 选择多大的 rank？[​](\#选择多大的-rank)

Tinker 默认 rank 为 32。如果在大型数据集上做 SL，应使用更大的 rank。粗略来说，只要 LoRA 参数量不小于 completion token 数（即 weight=1 的 token 数），LoRA 就能取得良好效果。可以用以下工具计算 LoRA 参数量：

```
from tinker_cookbook.hyperparam_utils import get_lora_param_countmodel_name = "meta-llama/Llama-3.1-8B"print(get_lora_param_count(model_name, lora_rank=32))
```
