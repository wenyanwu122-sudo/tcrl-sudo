# Tinker Cookbook

The **Tinker Cookbook** is the ecosystem around the [Tinker SDK](tinker.md). While the SDK provides the core client-server API for training and sampling, the cookbook gives you everything else:

- Training abstractions —
  
  `Env`
  
  ,
  
  `EnvGroupBuilder`
  
  ,
  
  `RLDataset`
  
  ,
  
  `train.Config`
- Renderers — Convert chat messages to tokens for every supported model family
- Production recipes — 15+ end-to-end training examples (SFT, RL, DPO, distillation, tool use, multi-agent, and more)
- Weight management — Download, merge, export, and publish trained models to HuggingFace
- Evaluation — 20+ standardized benchmarks (GSM8K, MMLU, MATH, IFEval, SWE-Bench, …)

📖 **Full Cookbook documentation: [tinker-docs.thinkingmachines.ai/cookbook](https://tinker-docs.thinkingmachines.ai/cookbook/)**

This mirror no longer duplicates Cookbook API details and tutorials. Instead, it focuses on providing quick-start guides and key references. For comparison experiments, see [Comparison Experiments](cookbook__experiments.md).

## Cookbook vs. SDK[​](\#cookbook-vs-sdk)

|  | Tinker SDK | Tinker Cookbook |
| --- | --- | --- |
| What | Core API client | Training ecosystem |
| Use when | You want full control over every API call | You want batteries-included training |
| Examples | training_client.forward_backward(data, "cross_entropy") | asyncio.run(train.main(config)) |
| Install | uv pip install "tinker==0.12.0" | uv pip install tinker-cookbook |

Most users will use both — the SDK for understanding what's happening, and the cookbook for building production training pipelines.

For more Cookbook usage (installation, Storage, Evaluation, etc.), see the [official docs](https://tinker-docs.thinkingmachines.ai/cookbook/).
