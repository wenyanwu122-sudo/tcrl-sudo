# 为什么选择 TCRL

TCRL 完全兼容 [Tinker SDK](https://tinker-docs.thinkingmachines.ai/tinker/) —— 你在自己机器上写 Python 代码，TCRL 负责在 GPU 上做分布式训练。

```{toctree}
:hidden:
:maxdepth: 2
:caption: 章节导航

imported/intro
imported/tinker
imported/tinker__quickstart
imported/tinker__models
imported/tinker__lora-primer
imported/tinker__losses
imported/tinker__losses__cross-entropy
imported/tinker__losses__importance-sampling
imported/tinker__losses__ppo
imported/tinker__losses__dro
imported/tinker__losses__cispo
imported/tinker__losses__custom
imported/tinker__cli
imported/tinker__cli__checkpoint
imported/tinker__cli__run
imported/tinker__compatible-apis
imported/tinker__compatible-apis__openai
imported/tinker__api-reference
imported/tinker__api-reference__apifuture
imported/tinker__api-reference__exceptions
imported/tinker__api-reference__restclient
imported/tinker__api-reference__samplingclient
imported/tinker__api-reference__serviceclient
imported/tinker__api-reference__trainingclient
imported/tinker__api-reference__types
imported/cookbook
imported/cookbook__quickstart
imported/cookbook__experiments
imported/cookbook__experiments__supervised-learning
imported/cookbook__experiments__reinforce-learning
```

## TCRL vs 传统训练框架

|  | 传统框架（如 Verl） | TCRL |
| --- | --- | --- |
| 你怎么写代码 | 写 YAML 配置 | 写 Python 代码 |
| 训练循环谁控制 | 框架（`RayPPOTrainer.fit()`） | 你自己（`for step in range(...)`） |
| 奖励函数怎么写 | 改 `reward.py` 文件 | 直接写 Python 函数 |
| 想在训练中间加逻辑 | 很难，循环在框架里 | 随便加，循环是你写的 |
| 需要自己管 GPU 吗 | 需要，你自己起集群 | 不需要，TCRL 服务管 |
| 数据在哪处理 | 训练节点（GPU 机器） | 你的本地 Python 进程 |

## 浏览文档

- **[Tinker SDK](imported/tinker.md)** — 快速开始、模型、损失函数、CLI 及 API 参考。
- **[Cookbook](imported/cookbook.md)** — 训练方案、评测与对比实验。
- **[教程](https://tinker-docs.thinkingmachines.ai/tutorials/)** — Tinker 官方文档中的分步教程。
