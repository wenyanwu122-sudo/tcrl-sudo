# Why TCRL?

TCRL is fully compatible with the [Tinker SDK](https://tinker-docs.thinkingmachines.ai/tinker/): you write Python code on your own machine, and TCRL handles distributed training on GPUs.

```{toctree}
:hidden:
:maxdepth: 2
:caption: Navigation

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

## TCRL vs traditional training frameworks

|  | Traditional frameworks such as Verl | TCRL |
| --- | --- | --- |
| How you write code | YAML configuration | Python code |
| Who controls the training loop | The framework, such as `RayPPOTrainer.fit()` | You, such as `for step in range(...)` |
| How rewards are defined | Edit a `reward.py` file | Write a Python function directly |
| Adding custom logic during training | Difficult because the loop is inside the framework | Flexible because you write the loop |
| GPU management | You manage the cluster | TCRL service manages it |
| Data processing | Training nodes / GPU machines | Your local Python process |

## Browse the docs

- **[Tinker SDK](imported/tinker.md)** — quick start, models, loss functions, CLI, and API reference.
- **[Cookbook](imported/cookbook.md)** — training recipes, evaluation, and comparison experiments.
- **[Tutorials](https://tinker-docs.thinkingmachines.ai/tutorials/)** — step-by-step tutorials from the upstream Tinker documentation.
