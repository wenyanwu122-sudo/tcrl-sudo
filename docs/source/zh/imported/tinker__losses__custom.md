# Custom Loss Functions

**Type:** Any — User-defined loss via `forward_backward_custom`.

For use cases outside of the built-in losses, Tinker provides `forward_backward_custom` and `forward_backward_custom_async` to compute a more general class of loss functions (at the cost of some additional latency).

## Basic usage[​](\#basic-usage)

A custom loss function receives the data and the model's logprobs, and returns a scalar loss plus optional metrics:

```
def logprob_squared_loss(data: list[Datum], logprobs: list[torch.Tensor]) -> tuple[torch.Tensor, dict[str, float]]:    loss = (logprobs ** 2).sum()    return loss, {"logprob_squared_loss": loss.item()}
```

```
future = training_client.forward_backward_custom(data, logprob_squared_loss)result = future.result()print(f"Loss: {result.loss}, Metrics: {result.metrics}")
```

### Multi-sequence loss[​](\#multi-sequence-loss)

You can also define loss functions that operate on multiple sequences at a time:

```
def variance_loss(data: list[Datum], logprobs: list[torch.Tensor]) -> tuple[torch.Tensor, dict[str, float]]:    flat_logprobs = torch.cat(logprobs)    variance = torch.var(flat_logprobs)    return variance, {"variance_loss": variance.item()}
```

A more practical use case is computing a Bradley-Terry loss on pairwise comparison data ([Learning to Summarize](https://arxiv.org/abs/2009.01325)), or [Direct Preference Optimization](https://arxiv.org/abs/2305.18290) — see the [DPO & Preferences tutorial](https://tinker-docs.thinkingmachines.ai/tutorials/advanced/dpo-preferences) for details.

## Multi-target loss[​](\#multi-target-loss)

You can use `forward_backward_custom` with multi-target `target_tokens` to define losses over a small candidate set at specific sequence positions. For example, a masked cross-entropy loss that trains on multiple-choice questions by renormalizing over four answer tokens instead of the full vocabulary:

```
import torchimport tinkermessages = [{"role": "user", "content": (    "What is the capital of France?\n"    "A) London\n"    "B) Paris\n"    "C) Berlin\n"    "D) Madrid\n"    "Answer Letter:")}]prompt_tokens = tokenizer.apply_chat_template(messages, add_generation_prompt=True)# Extract token IDs for the four answer letters.a_token = tokenizer.encode(" A", add_special_tokens=False)[0]b_token = tokenizer.encode(" B", add_special_tokens=False)[0]c_token = tokenizer.encode(" C", add_special_tokens=False)[0]d_token = tokenizer.encode(" D", add_special_tokens=False)[0]target_tokens = torch.zeros(len(prompt_tokens), 4, dtype=torch.long)target_tokens[-1] = torch.tensor([a_token, b_token, c_token, d_token])datum = tinker.Datum(    model_input=tinker.ModelInput.from_ints(prompt_tokens),    loss_fn_inputs={"target_tokens": target_tokens},)CORRECT_ANSWER_IDX = 1  # B) Parisdef masked_ce_loss(data, logprobs_list):    # logprobs_list[i] has shape [N, K=4] for each datum    # Renormalize over just the four answer tokens instead of the full vocabulary.    answer_logprobs = logprobs_list[0][-1]  # shape [K=4]    answer_logprobs = answer_logprobs - torch.logsumexp(answer_logprobs, dim=-1)    loss = -answer_logprobs[CORRECT_ANSWER_IDX]    return loss, {"masked_ce": loss.item()}future = training_client.forward_backward_custom([datum], masked_ce_loss)result = future.result()
```

If you're using a custom loss function that you think is generally useful, please let us know and we'll add it to the list of built-in loss functions. See the [Async Patterns](https://tinker-docs.thinkingmachines.ai/tutorials/basics/async-patterns) tutorial for the `async` version of these methods.

## How `forward_backward_custom` works[​](\#how-forward_backward_custom-works)

You don't need to read this section to use `forward_backward_custom`, but here's the key insight: Tinker does **NOT** pickle your function or send it to the server. Instead, it decomposes the gradient computation into a `forward` call followed by a `forward_backward` call on a weighted cross-entropy loss, which computes exactly the right gradient.

Mathematically, starting from the full nonlinear loss:

loss=f(log⁡pθ(x))\text{loss} = f\bigl(\log p_\theta(x)\bigr)loss=f(logpθ​(x))

Tinker constructs a surrogate loss that is linear in the logprobs but has the same gradient:

Lsurrogate=∑i∂f∂log⁡pθ(xi)⋅log⁡pθ(xi)\mathcal{L}_{\text{surrogate}} = \sum_i \frac{\partial f}{\partial \log p_\theta(x_i)} \cdot \log p_\theta(x_i)Lsurrogate​=i∑​∂logpθ​(xi​)∂f​⋅logpθ​(xi​)
