# 为什么选择 TCRL

TCRL 完全兼容 [Tinker SDK](https://tinker-docs.thinkingmachines.ai/tinker/) —— 你在自己机器上写 Python 代码，TCRL 负责在 GPU 上做分布式训练。

## TCRL vs 传统训练框架[​](\#tcrl-vs-传统训练框架)

|  | 传统框架（如 Verl） | TCRL |
| --- | --- | --- |
| 你怎么写代码 | 写 YAML 配置 | 写 Python 代码 |
| 训练循环谁控制 | 框架（ RayPPOTrainer.fit() ） | 你自己（ for step in range(...) ） |
| 奖励函数怎么写 | 改 reward.py 文件 | 直接写 Python 函数 |
| 想在训练中间加逻辑 | 很难，循环在框架里 | 随便加，循环是你写的 |
| 需要自己管 GPU 吗 | 需要，你自己起集群 | 不需要，TCRL 服务管 |
| 数据在哪处理 | 训练节点（GPU 机器） | 你的本地 Python 进程 |

## 浏览文档[​](\#浏览文档)

- **[Tinker SDK](tinker.md)**
  
  — 快速开始、模型、损失函数、CLI 及 API 参考。
- **[Cookbook](cookbook.md)**
  
  — 训练方案、评测与对比实验。
- **[教程](https://tinker-docs.thinkingmachines.ai/tutorials/)**
  
  — Tinker 官方文档中的分步教程。
