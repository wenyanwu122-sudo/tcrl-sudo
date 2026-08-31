# Tinker: a training API for researchers and developers

TCRL is fully compatible with the [Tinker SDK](https://tinker-docs.thinkingmachines.ai/tinker/). You write a simple loop that runs on your CPU-only machine, including the data or environment and the loss function. We figure out how to make the training work on a bunch of GPUs, doing the exact computation you specified, efficiently. To change the model you're working with, you only need to change a single string in your code.

Tinker gives you full control over the training loop and all the algorithmic details. It's not a magic black box that makes fine-tuning "easy". It's a clean abstraction that shields you from the complexity of distributed training while preserving your control.

Here's how the division of responsibilities works in practice:

| You focus on | You write | We handle |
| --- | --- | --- |
| Data & RL environments — your custom data, running on your CPU | Simple Python script | Efficient distributed training of large models (Llama 70B, Qwen 235B, …) |
| Training logic — your loss functions, training loop, and evals | API calls: forward_backward() , optim_step() , sample() , save_state() | Reliability — hardware failures handled transparently |

## Features[​](\#features)

What the Tinker service currently supports:

- Tinker lets you fine-tune open-weight models ranging from 1B to 1T+ parameters, including both dense and mixture-of-experts architectures. See
  
  [Models](tinker__models.md)
  
  for the full list.
- Tinker supports vision-language models (VLMs) like Qwen3-VL for image understanding tasks. See the
  
  [official docs](https://tinker-docs.thinkingmachines.ai/tutorials/core-concepts/rendering)
  
  for details.
- Tinker implements low-rank adaptation (LoRA) fine-tuning, not full fine-tuning. However, we believe that LoRA gives the same performance as full fine-tuning for many important use cases, especially in RL (see
  
  [LoRA Without Regret](https://thinkingmachines.ai/blog/lora/)
  
  ).
- You can download the weights of your trained model to use outside of Tinker, for example with your inference provider of choice.

## A quick look at functionality[​](\#a-quick-look-at-functionality)

Tinker's main functionality is contained in a few key functions:

- `forward_backward`
  
  : feed in your data and loss function, and we'll compute and accumulate the gradients for you.
- `optim_step`
  
  : update your model using the accumulated gradients
- `sample`
  
  : Generate outputs from your trained model
- other functions for saving and loading weights and optimizer state
