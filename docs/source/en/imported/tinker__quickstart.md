# Quick Start

## Installation[​](\#installation)

```
uv pip install tinker==0.12.0
```

**Note**: The latest version of Tinker SDK is coming soon.

Set your environment variables (contact us via WeCom to get an API key: **maximuswang** or **kellancai**):

```
export TINKER_API_KEY="your-api-key-here"export TINKER_BASE_URL="your-base-url-here"
```

This gives you the Python SDK (`import tinker`) and the CLI (`tinker run list`, `tinker checkpoint download`).

This page walks through the two main LLM fine-tuning workflows — supervised fine-tuning (SFT) and reinforcement learning (RL) — showing how each step maps to Tinker SDK calls.

## Supervised Fine-Tuning (SFT)[​](\#supervised-fine-tuning-sft)

SFT trains a model to imitate examples:

1. **Create clients**
  
  — connect to Tinker, create a TrainingClient
2. **Prepare data**
  
  — tokenize examples into
  
  `Datum`
  
  objects with loss masks
3. **Train**
  
  —
  
  `forward_backward`
  
  (gradients) +
  
  `optim_step`
  
  (update weights)
4. **Evaluate**
  
  — save weights, create a SamplingClient, sample

## Reinforcement Learning (RL)[​](\#reinforcement-learning-rl)

RL trains a model to maximize a reward signal:

1. **Create clients**
  
  — connect to Tinker, create a TrainingClient
2. **Get on-policy sampler**
  
  —
  
  `save_weights_and_get_sampling_client`
3. **Sample rollouts**
  
  — generate completions from the on-policy model
4. **Score**
  
  — compute rewards and log-probabilities
5. **Train**
  
  —
  
  `forward_backward`
  
  with RL loss +
  
  `optim_step`
6. **Repeat**
  
  — new weights → new SamplingClient → sample again

## API Cheatsheet[​](\#api-cheatsheet)

### Create clients[​](\#create-clients)

```
import tinkerfrom tinker import types# Entry point — reads TINKER_API_KEY from environmentservice_client = tinker.ServiceClient()# Training client (LoRA fine-tuning)training_client = service_client.create_lora_training_client(    base_model="Qwen/Qwen3-8B", rank=32)# Sampling client (text generation)sampling_client = service_client.create_sampling_client(    base_model="Qwen/Qwen3-8B")# Tokenizertokenizer = training_client.get_tokenizer()
```

💡 **Subprocess sampling**
SamplingClient is picklable — you can pass it to other processes for parallel sampling. If your training loop has CPU-heavy work (grading, environment logic), set `TINKER_SUBPROCESS_SAMPLING=1` to run sample() and compute_logprobs() in a dedicated subprocess, preventing GIL contention.

### Prepare training data[​](\#prepare-training-data)

A `Datum` is a single training example. It contains input tokens, target tokens, and per-token loss weights (0 = ignore, 1 = compute loss).

```
datum = types.Datum(    model_input=types.ModelInput.from_ints(tokens=input_tokens),    loss_fn_inputs=dict(        weights=weights,           # 0 for prompt, 1 for completion        target_tokens=target_tokens  # shifted by 1 from input    ))
```

For RL losses (importance_sampling, PPO, CISPO), the `loss_fn_inputs` also includes `logprobs` and `advantages`:

```
rl_datum = types.Datum(    model_input=types.ModelInput.from_ints(tokens=tokens),    loss_fn_inputs=dict(        target_tokens=target_tokens,        weights=weights,        logprobs=sampling_logprobs,  # from the rollout policy        advantages=advantages,        # reward - baseline    ))
```

### Sample text[​](\#sample-text)

```
prompt = types.ModelInput.from_ints(tokenizer.encode("The capital of France is"))params = types.SamplingParams(max_tokens=50, temperature=0.7, stop=["\n"])# Single sample — sample_async returns the result directlyresult = await sampling_client.sample_async(prompt=prompt, num_samples=1, sampling_params=params)print(tokenizer.decode(result.sequences[0].tokens))# Multiple samples in one callresult = await sampling_client.sample_async(prompt=prompt, num_samples=8, sampling_params=params)for seq in result.sequences:    print(tokenizer.decode(seq.tokens))
```

### Compute log-probabilities[​](\#compute-log-probabilities)

Used for scoring in RL (comparing the training policy against the sampling policy).

```
# Prompt logprobsresult = await sampling_client.sample_async(    prompt=prompt, num_samples=1,    sampling_params=types.SamplingParams(max_tokens=1),    include_prompt_logprobs=True,)print(result.prompt_logprobs)  # [None, -9.5, -1.6, ...]# Shorthand — compute_logprobs_async returns the result directlylogprobs = await sampling_client.compute_logprobs_async(prompt)# Top-k logprobs (for distillation)result = await sampling_client.sample_async(    prompt=prompt, num_samples=1,    sampling_params=types.SamplingParams(max_tokens=1),    include_prompt_logprobs=True,    topk_prompt_logprobs=5,)print(result.topk_prompt_logprobs)  # [None, [(token_id, logprob), ...], ...]
```

### Forward-backward[​](\#forward-backward)

Computes gradients for the given data and loss function. Returns immediately with a future.

```
# SFT: cross-entropy lossfwdbwd_future = await training_client.forward_backward_async(data=[datum], loss_fn="cross_entropy")fwdbwd_result = await fwdbwd_future.result_async()print(f"Loss: {fwdbwd_result.loss}")# RL lossesfwdbwd_future = await training_client.forward_backward_async(data, "importance_sampling")fwdbwd_future = await training_client.forward_backward_async(data, "ppo")fwdbwd_future = await training_client.forward_backward_async(data, "cispo")fwdbwd_future = await training_client.forward_backward_async(data, "dro")# Custom lossfwdbwd_future = await training_client.forward_backward_custom_async(data, my_loss_fn)
```

See [Loss Functions](tinker__losses.md) for the math behind each loss.

### Optimizer step[​](\#optimizer-step)

Updates model weights using the gradients from the last `forward_backward`.

```
optim_future = await training_client.optim_step_async(    types.AdamParams(learning_rate=1e-4))await optim_future.result_async()
```

### Save and load weights[​](\#save-and-load-weights)

```
# Save weights → get a sampling client for evaluationsampling_client = training_client.save_weights_and_get_sampling_client(name="checkpoint-1")# Save full state (weights + optimizer) for resumingtraining_client.save_state(name="step-100")# Resume from weights onlytraining_client = await service_client.create_training_client_from_state_async(    path="tinker://run-id/sampler_weights/checkpoint-1")# Resume with optimizer statetraining_client = await service_client.create_training_client_from_state_with_optimizer_async(    path="tinker://run-id/weights/step-100")
```

### Vision inputs[​](\#vision-inputs)

```
import requestsimage_data = requests.get("https://example.com/image.png").contentmodel_input = tinker.ModelInput(chunks=[    types.EncodedTextChunk(tokens=tokenizer.encode("<|im_start|>user\n<|vision_start|>")),    types.ImageChunk(data=image_data, format="png"),    types.EncodedTextChunk(tokens=tokenizer.encode("<|vision_end|>Describe this image<|im_end|>\n<|im_start|>assistant\n")),])
```

### Concurrent requests[​](\#concurrent-requests)

```
import asyncio# Multiple samples from the same prompt — just increase num_samplesresult = await sampling_client.sample_async(prompt=prompt, num_samples=16, sampling_params=params)for seq in result.sequences:  # 16 independent completions    print(tokenizer.decode(seq.tokens))# Multiple different prompts in parallel — use asyncio.gatherresults = await asyncio.gather(    sampling_client.sample_async(prompt=prompt1, num_samples=1, sampling_params=params),    sampling_client.sample_async(prompt=prompt2, num_samples=1, sampling_params=params),    sampling_client.sample_async(prompt=prompt3, num_samples=1, sampling_params=params),)# Pipeline training: overlap forward-backward with optimizer stepfwdbwd = await training_client.forward_backward_async(batch1, "cross_entropy")optim_future = training_client.optim_step(types.AdamParams(learning_rate=1e-4))next_fwdbwd = await training_client.forward_backward_async(batch2, "cross_entropy")await optim_future
```
