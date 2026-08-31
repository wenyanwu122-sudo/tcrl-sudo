# SamplingClient

## *class* [**tinker.SamplingClient**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/sampling_client.py)(*holder* , *sampling_session_id* , *shadow=False* , *retry_config=None* , *subprocess_sampling=None*)[​](\#class-tinkersamplingclientholder--sampling_session_id--shadowfalse--retry_confignone--subprocess_samplingnone)

Client for text generation and inference from trained or base models.

The SamplingClient lets you generate text tokens from either a base model or from weights you've saved using a TrainingClient. You typically get one by calling `service_client.create_sampling_client()` or `training_client.save_weights_and_get_sampling_client()`.

**Key methods:**

- sample() - generate text completions with customizable parameters
- compute_logprobs() - get log probabilities for prompt tokens

**Create method parameters:**

- `model_path`
  
  : Path to saved model weights (starts with 'tinker://')
- `base_model`
  
  : Name of base model to use for inference (e.g., 'Qwen/Qwen3-8B')
- `retry_config`
  
  : Configuration for retrying failed requests

**Multi-processing support:** This class is picklable, so it can be passed to a separate process/worker to sample. It is also safe to pass the same instance of SamplingClient to multiple processes/workers.

If you are using Tinker SDK with more than one process you should always create SamplingClient from the main process and then pass it to the other processes/workers. ServiceClient and TrainingClient should always be managed from the main process.

**Subprocess isolation:** Set `TINKER_SUBPROCESS_SAMPLING=1` to run sample() and compute_logprobs() in a dedicated subprocess, preventing GIL contention from CPU-heavy user code (grading, environment interactions) from stalling networking IO and heartbeats. This is transparent — the same API works with or without it.

```
sampling_client = service_client.create_sampling_client(base_model="Qwen/Qwen3-8B")prompt = types.ModelInput.from_ints(tokenizer.encode("The weather today is"))params = types.SamplingParams(max_tokens=20, temperature=0.7)future = sampling_client.sample(prompt=prompt, sampling_params=params, num_samples=1)result = future.result()
```

**Parameters:**

- **holder**
  
  (
  
  *InternalClientHolder*
  
  ) –
- **sampling_session_id**
  
  (
  
  *str*
  
  ) –
- **shadow**
  
  (
  
  *bool*
  
  ) – Default:
  
  `False`
  
  .
- **retry_config**
  
  (
  
  *RetryConfig | None*
  
  ) – Default:
  
  `None`
  
  .
- **subprocess_sampling**
  
  (
  
  *bool | None*
  
  ) – Default:
  
  `None`
  
  .

### [**sample**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/sampling_client.py\#L287)(*prompt* , *num_samples* , *sampling_params* , *include_prompt_logprobs=False* , *topk_prompt_logprobs=0*)[​](\#sampleprompt--num_samples--sampling_params--include_prompt_logprobsfalse--topk_prompt_logprobs0)

Generate text completions from the model.

**Returns:** `Future` containing the `SampleResponse` with generated text

```
prompt = types.ModelInput.from_ints(tokenizer.encode("The weather today is"))params = types.SamplingParams(max_tokens=20, temperature=0.7)future = sampling_client.sample(prompt=prompt, sampling_params=params, num_samples=1)result = future.result()for sample in result.samples:    print(tokenizer.decode(sample.tokens))
```

*Async variant:* `sample_async()`

### [**compute_logprobs**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/sampling_client.py\#L374)(*prompt*)[​](\#compute_logprobsprompt)

Compute log probabilities for prompt tokens.

**Returns:** `Future` — list of log probabilities for each token in the prompt. `None` values indicate tokens where log probabilities couldn't be computed.

```
prompt = types.ModelInput.from_ints(tokenizer.encode("Hello world"))future = sampling_client.compute_logprobs(prompt)logprobs = future.result()for i, logprob in enumerate(logprobs):    if logprob is not None:        print(f"Token {i}: logprob = {logprob:.4f}")
```
