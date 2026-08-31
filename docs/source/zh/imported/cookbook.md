# Tinker Cookbook

**Tinker Cookbook** 是围绕 [Tinker SDK](tinker.md) 构建的训练生态，提供 SFT / RL / DPO 等训练管线、渲染器、权重管理、评测等上层抽象。

📖 **完整的 Cookbook 文档请参考：[tinker-docs.thinkingmachines.ai/cookbook](https://tinker-docs.thinkingmachines.ai/cookbook/)**

本文档不再重复维护 Cookbook 的 API 细节与教程，而是提供快速入门和关键参考。对比实验请查看[对比实验](cookbook__experiments.md)。

## Cookbook vs. SDK[​](\#cookbook-vs-sdk)

|  | Tinker SDK | Tinker Cookbook |
| --- | --- | --- |
| 定位 | 核心 API 客户端 | 训练生态与上层抽象 |
| 适用场景 | 需要细粒度控制每个 API 调用 | 开箱即用的训练管线 |
| 示例 | training_client.forward_backward(data, "cross_entropy") | asyncio.run(train.main(config)) |
| 安装 | uv pip install tinker | uv pip install tinker-cookbook |

大多数用户会同时使用两者——SDK 用于理解底层行为，Cookbook 用于构建生产级训练流程。

更多 Cookbook 用法（安装、Storage、Evaluation 等）请查阅 [官方文档](https://tinker-docs.thinkingmachines.ai/cookbook/)。
