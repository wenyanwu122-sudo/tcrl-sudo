# OpenAI API Compatible Inference (in beta)

⚠️ **Coming soon** — This feature is not yet supported.

OpenAI-compatible inference lets you interact with any model checkpoint in Tinker, using an endpoint compatible with the [OpenAI Completions API](https://platform.openai.com/docs/api-reference/chat). It's designed to let you easily "poke at" your model while you're training it.

For inference within your training runs (e.g. RL), we recommend using Tinker's standard sampling client (see the [API Reference](tinker__api-reference__samplingclient.md)).

Currently, OpenAI-compatible inference is meant for testing and internal use with low internal traffic, rather than large, high-throughput, user-facing deployments. Latency and throughput may vary by model and may change without notice during the beta. If you need higher or more stable throughput, contact the Tinker team in [our Discord](https://discord.gg/KqqEZNX88c) for guidance on larger-scale setups.

## Use Cases[​](\#use-cases)

OpenAI-compatible inference is designed for:

- **Fast feedback while training**
  
  : Start sampling very quickly from any sampler checkpoint obtained during training.
- **Sampling while training continues**
  
  : Sample even while the training job is still running on that experiment.
- **Developer & internal workflows**
  
  : Intended for testing, evaluation, and internal tools.

We will release production-grade inference soon and will update our users then.

## Using OpenAI compatible inference from an OpenAI client[​](\#using-openai-compatible-inference-from-an-openai-client)

The new interface exposes an OpenAI-compatible HTTP API. You can use any OpenAI SDK or HTTP client that lets you override the base URL.

1. Set the base URL of your OpenAI-compatible client to:

```
https://tinker.thinkingmachines.dev/services/tinker-prod/oai/api/v1
```

1. Use a Tinker sampler weight path as the model name. For example:

```
tinker://0034d8c9-0a88-52a9-b2b7-bce7cb1e6fef:train:0/sampler_weights/000080
```

Any valid Tinker sampler checkpoint path works here. You can keep training and sample from the same checkpoint simultaneously.

1. Authenticate with your Tinker API key, by passing the same key used for Tinker as the API key to the OpenAI client.

**Note:** We support both `/completions` and `/chat/completions` endpoints. Chat requests are rendered with the model's default Hugging Face chat template; if your checkpoint expects a different renderer, render the prompt yourself (see the [Rendering docs](https://tinker-docs.thinkingmachines.ai/tutorials/core-concepts/rendering)) and use `/completions`.

## Code Example[​](\#code-example)

```
from os import getenvfrom openai import OpenAIBASE_URL = "https://tinker.thinkingmachines.dev/services/tinker-prod/oai/api/v1"MODEL_PATH = "tinker://0034d8c9-0a88-52a9-b2b7-bce7cb1e6fef:train:0/sampler_weights/000080"api_key = getenv("TINKER_API_KEY")client = OpenAI(    base_url=BASE_URL,    api_key=api_key,)response = client.completions.create(    model=MODEL_PATH,    prompt="The capital of France is",    max_tokens=50,    temperature=0.7,    top_p=0.9,)print(f"{response.choices[0].text}")
```
