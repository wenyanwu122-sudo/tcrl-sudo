# Tinker：面向研究者和开发者的训练 API

TCRL 完全兼容 [Tinker SDK](https://tinker-docs.thinkingmachines.ai/tinker/)。你只需在 CPU 机器上编写一个简单的训练循环，包括数据/环境定义和损失函数。Tinker 负责将训练高效地分布到多 GPU 上执行。更换模型只需修改代码中的一个字符串。

Tinker 保留你对训练循环和所有算法细节的完全控制——它不是让微调变"简单"的黑盒，而是一个在屏蔽分布式训练复杂性的同时保留控制力的清晰抽象。

以下是职责划分：

| 你负责 | 你编写 | Tinker 负责 |
| --- | --- | --- |
| 数据与 RL 环境 — 自定义训练数据，在 CPU 上运行 | 简单 Python 脚本 | 大模型高效分布式训练（Llama 70B、Qwen 235B 等） |
| 训练逻辑 — 损失函数、训练循环、评测 | API 调用： forward_backward() 、 optim_step() 、 sample() 、 save_state() | 可靠性 — 硬件故障透明处理 |

## 功能特性[​](\#功能特性)

Tinker 服务当前支持的功能：

- Tinker 支持微调 1B 到 1T+ 参数的开源模型，包括稠密模型和 MoE 架构。完整列表见
  
  [模型列表](tinker__models.md)
  
  。
- Tinker 支持视觉语言模型（如 Qwen3-VL），可用于图像理解任务。详见
  
  [官方文档](https://tinker-docs.thinkingmachines.ai/tutorials/core-concepts/rendering)
  
  。
- Tinker 采用 LoRA 微调而非全量微调。在许多重要场景（尤其是 RL）中，LoRA 与全量微调性能相当（参见
  
  [LoRA Without Regret](https://thinkingmachines.ai/blog/lora/)
  
  ）。
- 你可以下载训练好的模型权重，在 Tinker 之外使用。

## 功能速览[​](\#功能速览)

Tinker 的核心功能集中在以下几个关键函数：

- `forward_backward`
  
  ：输入数据和损失函数，计算并累积梯度。
- `optim_step`
  
  ：使用累积的梯度更新模型参数。
- `sample`
  
  ：从训练好的模型生成输出。
- 其他用于保存/加载权重和优化器状态的函数。
