# Models

| Model | Tinker ID | Type | Arch | Size | Context | Prefill | Sample | Train |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Llama 3.2 1B | meta-llama/Llama-3.2-1B | Base | Dense | 1B | 32k |  |  |  |
| Qwen2.5 0.5B Instruct | Qwen/Qwen2.5-0.5B-Instruct | Instruction | Dense | 0.5B | 32k |  |  |  |
| Qwen3 4B Instruct | Qwen/Qwen3-4B-Instruct-2507 | Instruction | Dense | 4B | 32k |  |  |  |
| Qwen3 8B | Qwen/Qwen3-8B | Base | Dense | 8B | 16K |  |  |  |
| Qwen3 8B Base | Qwen/Qwen3-8B-Base | Base | Dense | 8B | 16K |  |  |  |

## Model Terms[​](\#model-terms)

- **Prefill**
  
  : Processing input/prompt tokens (forward pass only)
- **Sample**
  
  : Generating output tokens (forward pass + sampling)
- **Train**
  
  : Forward and backward pass for gradient computation
- **Context**
  
  : Maximum sequence length.
- **Tinker ID**
  
  : The exact string to pass to
  
  `create_lora_training_client(base_model=...)`
  
  or
  
  `create_sampling_client(base_model=...)`

MoE models are priced by active parameters, making them significantly more cost-effective than dense models of similar quality.

## Choosing a Model[​](\#choosing-a-model)

| Scenario | Recommendation |
| --- | --- |
| Research / post-training | Use Base models |
| Task-specific fine-tuning | Start with an Instruction or Hybrid model |
| Low latency | Use Instruction models (no chain-of-thought) |
| High intelligence | Use Reasoning or Hybrid models (chain-of-thought) |
| Vision tasks | Use models with Vision in the type |
