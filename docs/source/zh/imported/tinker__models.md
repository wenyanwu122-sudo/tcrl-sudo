# 模型

| Model | Tinker ID | Type | Arch | Size | Context | Prefill | Sample | Train |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Llama 3.2 1B | meta-llama/Llama-3.2-1B | Base | Dense | 1B | 32k |  |  |  |
| Qwen2.5 0.5B Instruct | Qwen/Qwen2.5-0.5B-Instruct | Instruction | Dense | 0.5B | 32k |  |  |  |
| Qwen3 4B Instruct | Qwen/Qwen3-4B-Instruct-2507 | Instruction | Dense | 4B | 32k |  |  |  |
| Qwen3 8B | Qwen/Qwen3-8B | Base | Dense | 8B | 16K |  |  |  |
| Qwen3 8B Base | Qwen/Qwen3-8B-Base | Base | Dense | 8B | 16K |  |  |  |

## 模型术语[​](\#模型术语)

- **Prefill**
  
  ：处理输入/prompt token（仅前向传播）
- **Sample**
  
  ：生成输出 token（前向传播 + 采样）
- **Train**
  
  ：前向和反向传播，计算梯度
- **Context**
  
  ：最大序列长度。
- **Tinker ID**
  
  ：传给
  
  `create_lora_training_client(base_model=...)`
  
  或
  
  `create_sampling_client(base_model=...)`
  
  的精确字符串

MoE 模型按活跃参数计费，相比同等质量的稠密模型更具性价比。

## 模型选择指南[​](\#模型选择指南)

| 场景 | 推荐 |
| --- | --- |
| 研究与后训练 | 使用 Base 模型 |
| 特定任务微调 | 从 Instruction 或 Hybrid 模型开始 |
| 低延迟 | 使用 Instruction 模型（无思维链） |
| 高智能 | 使用 Reasoning 或 Hybrid 模型（带思维链） |
| 视觉任务 | 使用类型中包含 Vision 的模型 |
