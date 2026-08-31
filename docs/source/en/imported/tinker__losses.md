# Loss Functions

Tinker provides built-in loss functions for supervised learning and reinforcement learning. You select a loss by passing a string to `forward_backward`:

```
future = await training_client.forward_backward_async(data, loss_fn="cross_entropy")result = await future.result_async()
```

## Overview[​](\#overview)

| Loss Function | loss_fn | Type | Description |
| --- | --- | --- | --- |
| Cross-Entropy | "cross_entropy" | SFT | Standard negative log-likelihood for supervised fine-tuning |
| Importance Sampling | "importance_sampling" | RL | Off-policy policy gradient with importance weighting |
| PPO | "ppo" | RL | Clipped surrogate objective for stable policy updates |
| DRO | "dro" | RL | Quadratic penalty for off-policy / offline RL |
| CISPO | "cispo" | RL | Detached clipped importance ratio for policy gradient |
| Custom | — | Any | User-defined loss via forward_backward_custom |

## How it works[​](\#how-it-works)

Each training example is a `Datum` — a single sequence with all the information needed to compute the loss. A `Datum` contains:

- **`model_input`**
  
  — the token sequence (shape:
  
  `(N,)`
  
  where N is the sequence length)
- **`loss_fn_inputs`**
  
  — a dict of tensors that the loss function needs (targets, weights, advantages, etc.)

The key design principle: **everything the loss needs is in the Datum**. Each Datum is self-contained — no batch-level state, no external lookups.

### SFT example[​](\#sft-example)

```
import tinkerfrom tinker import typesdatum = types.Datum(    model_input=types.ModelInput.from_ints(input_tokens),  # shape: (N,)    loss_fn_inputs={        "target_tokens": target_tokens,  # shape: (N,) — what to predict at each position        "weights": weights,              # shape: (N,) — 0 for prompt, 1 for completion    })future = await training_client.forward_backward_async([datum], loss_fn="cross_entropy")result = await future.result_async()print(f"Loss: {result.loss}")
```

### RL example[​](\#rl-example)

For RL losses, the Datum also includes the sampling log-probabilities and advantages:

```
rl_datum = types.Datum(    model_input=types.ModelInput.from_ints(tokens),    # shape: (N,)    loss_fn_inputs={        "target_tokens": target_tokens,                 # shape: (N,)        "weights": weights,                             # shape: (N,)        "logprobs": sampling_logprobs,                  # shape: (N,) — from the rollout policy        "advantages": advantages,                       # shape: (N,) — reward signal per token    })future = await training_client.forward_backward_async([rl_datum], loss_fn="importance_sampling")
```
