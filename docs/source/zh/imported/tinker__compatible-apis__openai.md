# OpenAI API 兼容推理（Beta）

⚠️ **即将推出** — 此功能尚未支持。

OpenAI 兼容推理允许你使用兼容 [OpenAI Completions API](https://platform.openai.com/docs/api-reference/chat) 的端点，与 Tinker 中的任何模型检查点进行交互。它旨在让你在训练过程中轻松地"测试"你的模型。

对于训练过程中的推理（例如 RL），我们推荐使用 Tinker 的标准采样客户端（参见 [API 参考](tinker__api-reference__samplingclient.md)）。

目前，OpenAI 兼容推理适用于低内部流量的测试和内部使用场景，而非面向用户的大规模高吞吐量部署。延迟和吞吐量可能因模型而异，并且在 Beta 期间可能会随时变化。如果你需要更高或更稳定的吞吐量，请在 [我们的 Discord](https://discord.gg/KqqEZNX88c) 联系 Tinker 团队，获取更大规模部署的指导。

## 适用场景[​](\#适用场景)

OpenAI 兼容推理适用于：

- **训练期间快速反馈**
  
  ：从训练过程中获取的任何采样器检查点快速开始采样。
- **训练过程中同时采样**
  
  ：即使该实验的训练任务仍在运行，也可以进行采样。
- **开发者与内部工作流**
  
  ：适用于测试、评测和内部工具。

我们即将发布生产级推理服务，届时将通知用户。

## 通过 OpenAI 客户端使用兼容推理[​](\#通过-openai-客户端使用兼容推理)

新接口提供了一个 OpenAI 兼容的 HTTP API。你可以使用任何允许自定义 base URL 的 OpenAI SDK 或 HTTP 客户端。

1. 将 OpenAI 兼容客户端的 base URL 设置为：

```
https://tinker.thinkingmachines.dev/services/tinker-prod/oai/api/v1
```

1. 使用 Tinker 采样器权重路径作为模型名称。例如：

```
tinker://0034d8c9-0a88-52a9-b2b7-bce7cb1e6fef:train:0/sampler_weights/000080
```

任何有效的 Tinker 采样器检查点路径都可以使用。你可以在继续训练的同时从同一检查点进行采样。

1. 使用你的 Tinker API Key 进行认证，将用于 Tinker 的 API Key 传递给 OpenAI 客户端。

**注意：** 我们同时支持 `/completions` 和 `/chat/completions` 端点。Chat 请求将使用模型的默认 Hugging Face 聊天模板进行渲染；如果你的检查点需要不同的渲染器，请自行渲染 prompt（参见[渲染文档](https://tinker-docs.thinkingmachines.ai/tutorials/core-concepts/rendering)）并使用 `/completions`。

## 代码示例[​](\#代码示例)

```
from os import getenvfrom openai import OpenAIBASE_URL = "https://tinker.thinkingmachines.dev/services/tinker-prod/oai/api/v1"MODEL_PATH = "tinker://0034d8c9-0a88-52a9-b2b7-bce7cb1e6fef:train:0/sampler_weights/000080"api_key = getenv("TINKER_API_KEY")client = OpenAI(    base_url=BASE_URL,    api_key=api_key,)response = client.completions.create(    model=MODEL_PATH,    prompt="The capital of France is",    max_tokens=50,    temperature=0.7,    top_p=0.9,)print(f"{response.choices[0].text}")
```
