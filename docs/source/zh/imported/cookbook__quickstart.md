# 快速开始

## 安装[​](\#安装)

```
uv pip install tinker==0.12.0 tinker-cookbook
```

设置环境变量（通过企业微信联系我们获取 API Key：**maximuswang** 或 **kellancai**）：

```
export TINKER_API_KEY="your-api-key-here"export TINKER_BASE_URL="your-base-url-here"
```

可选扩展：`[math-rl]`、`[modal]`、`[wandb]`、`[cloud]`、`[inspect]`、`[all]`。

完整安装指南请参考 [官方 Cookbook Quickstart](https://tinker-docs.thinkingmachines.ai/cookbook/quickstart/)。

Cookbook 在 [Tinker SDK](tinker__quickstart.md) 之上提供了更高层的抽象——SDK 提供原始操作（`forward_backward`、`optim_step`、`sample`），Cookbook 提供可配置的训练管线，自动处理流水线、checkpoint、评测和日志。

- **SFT**
  
  ：通过
  
  `train.Config`
  
  一行配置即可运行完整的监督微调循环
- **RL**
  
  ：通过
  
  `Env`
  
  +
  
  `EnvGroupBuilder`
  
  +
  
  `RLDataset`
  
  组合出完整的 RL 训练流程
- **DPO**
  
  ：通过
  
  `Comparison`
  
  /
  
  `LabeledComparison`
  
  进行偏好学习

详细代码示例和 API 说明请查阅 [官方文档](https://tinker-docs.thinkingmachines.ai/cookbook/)。
