# Why TCRL

TCRL is fully compatible with the [Tinker SDK](https://tinker-docs.thinkingmachines.ai/tinker/) — you write Python code on your own machine, and TCRL handles the distributed training on GPUs.

## TCRL vs Traditional Training Frameworks[​](\#tcrl-vs-traditional-training-frameworks)

|  | Traditional (e.g. Verl) | TCRL |
| --- | --- | --- |
| How you write code | YAML configuration | Python code |
| Who controls the training loop | The framework ( RayPPOTrainer.fit() ) | You ( for step in range(...) ) |
| How you write reward functions | Modify reward.py file | Write a Python function directly |
| Adding logic mid-training | Hard — the loop lives in the framework | Easy — you own the loop |
| Do you manage GPUs? | Yes — you provision the cluster yourself | No — TCRL service manages it |
| Where is data processed? | Training nodes (GPU machines) | Your local Python process |

## Explore the docs[​](\#explore-the-docs)

- **[Tinker SDK](tinker.md)**
  
  — Quick start, models, losses, CLI and API reference.
- **[Cookbook](cookbook.md)**
  
  — Production recipes, evaluation, and comparison experiments.
- **[Tutorials](https://tinker-docs.thinkingmachines.ai/tutorials/)**
  
  — Step-by-step walkthroughs on the official Tinker docs.
