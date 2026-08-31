# Get Started

## Installation[​](\#installation)

```
uv pip install tinker-cookbook tinker==0.12.0
```

Set your environment variables (contact us via WeCom to get an API key: **maximuswang** or **kellancai**):

```
export TINKER_API_KEY="your-api-key-here"export TINKER_BASE_URL="your-base-url-here"
```

Optional extras: `[math-rl]`, `[modal]`, `[wandb]`, `[cloud]`, `[inspect]`, `[all]`.

For nightly builds:

```
uv pip install 'tinker-cookbook @ git+https://github.com/thinking-machines-lab/tinker-cookbook.git@nightly'
```

For the full installation guide, see the [official Cookbook Quickstart](https://tinker-docs.thinkingmachines.ai/cookbook/quickstart/).

The cookbook provides higher-level abstractions on top of the [Tinker SDK](tinker__quickstart.md). Where the SDK gives you raw operations (`forward_backward`, `optim_step`, `sample`), the cookbook gives you configurable training pipelines that handle pipelining, checkpointing, evaluation, and logging automatically.

- **SFT**
  
  : Run a complete supervised fine-tuning loop with a single
  
  `train.Config`
- **RL**
  
  : Compose
  
  `Env`
  
  +
  
  `EnvGroupBuilder`
  
  +
  
  `RLDataset`
  
  into a full RL training pipeline
- **DPO**
  
  : Perform preference learning with
  
  `Comparison`
  
  /
  
  `LabeledComparison`

For detailed code examples and API docs, see the [official Cookbook docs](https://tinker-docs.thinkingmachines.ai/cookbook/).
