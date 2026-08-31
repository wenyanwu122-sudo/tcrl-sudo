# Cross-Entropy

**Type:** SFT — Standard supervised fine-tuning loss.

The standard cross-entropy loss (negative log-likelihood), which optimizes the policy pθp_\thetapθ​ to maximize the log-probability of the target tokens xxx:

L(θ)=−Ex[log⁡pθ(x)]\mathcal{L}(\theta) = -\mathbb{E}_x[\log p_\theta(x)]L(θ)=−Ex​[logpθ​(x)]

where `weights` is either 0 or 1, typically generated from `renderer.build_supervised_example()` which returns `(model_input, weights)` to specify the desired assistant turns to train on.

### Implementation[​](\#implementation)

```
# Apply weights and compute elementwise losselementwise_loss = -target_logprobs * weights# Apply sum reduction to get the total lossloss = elementwise_loss.sum()  # scalar
```

### Input tensors[​](\#input-tensors)

| Key | Shape | Description |
| --- | --- | --- |
| target_tokens | (N,) or (N, K) | Target token IDs |
| weights | (N,) or (N, K) | Token-level loss weights (typically from the renderer) |

### Output tensors[​](\#output-tensors)

| Key | Shape | Description |
| --- | --- | --- |
| logprobs | (N,) or (N, K) | Log probabilities of the requested target tokens |

### Diagnostics[​](\#diagnostics)

- `loss:sum`
  
  (scalar) — Sum of weighted cross-entropy losses

## Top-K Distillation[​](\#top-k-distillation)

When the input tensors have shape `(N, K)`, `cross_entropy` extracts the student's logprobs for KKK target tokens per position and computes:

LCE-topK(θ)=−∑t∑k=1Kwt,k⋅log⁡pθ(xt,k)\mathcal{L}_{\text{CE-topK}}(\theta) = -\sum_{t}\sum_{k=1}^{K} w_{t,k} \cdot \log p_\theta(x_{t,k})LCE-topK​(θ)=−t∑​k=1∑K​wt,k​⋅logpθ​(xt,k​)

where wt,kw_{t,k}wt,k​ are the user-provided weights. For **soft-target** distillation, set wt,k=p~teacher(xt,k)w_{t,k} = \tilde{p}_{\text{teacher}}(x_{t,k})wt,k​=p~​teacher​(xt,k​) — the teacher's probabilities renormalized over the top-K tokens. For **hard-target** training, put weight 1.0 on a single candidate and 0.0 on the rest.

### Example: Distilling Qwen3-235B → Qwen3-30B[​](\#example-distilling-qwen3-235b--qwen3-30b)

The example below samples a completion from the teacher, recovers its top-KKK distribution at each generated position, and trains the student to match it.

```
import tinkerimport torchfrom transformers import AutoTokenizertokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-235B-A22B-Instruct-2507")K = 20service_client = tinker.ServiceClient()teacher_sampling_client = await service_client.create_sampling_client_async(    base_model="Qwen/Qwen3-235B-A22B-Instruct-2507")student_training_client = await service_client.create_lora_training_client_async(    base_model="Qwen/Qwen3-30B-A3B-Instruct-2507")messages = [{"role": "user", "content": "Write a Python function to compute the nth Fibonacci number efficiently."}]prompt_tokens = tokenizer.apply_chat_template(messages, add_generation_prompt=True)# 1. Sample a completion from the teacher.sample_response = await teacher_sampling_client.sample_async(    prompt=tinker.ModelInput.from_ints(prompt_tokens),    num_samples=1,    sampling_params=tinker.SamplingParams(max_tokens=512, temperature=0.7),)sampled_tokens = list(sample_response.sequences[0].tokens)# 2. Teacher-force the completion to recover top-K logprobs at each position.teacher_forced = tinker.ModelInput.from_ints(prompt_tokens + sampled_tokens)topk_response = await teacher_sampling_client.sample_async(    prompt=teacher_forced,    num_samples=1,    sampling_params=tinker.SamplingParams(max_tokens=1),    include_prompt_logprobs=True,    topk_prompt_logprobs=K,)output_toks_with_logprobs = topk_response.topk_prompt_logprobs[len(prompt_tokens):]seq_len = len(output_toks_with_logprobs)teacher_tokens = torch.tensor(    [[tok_id for tok_id, _ in row] for row in output_toks_with_logprobs], dtype=torch.long)  # [seq_len, K]teacher_logprobs = torch.tensor(    [[lp for _, lp in row] for row in output_toks_with_logprobs])  # [seq_len, K]# Renormalize teacher logprobs over top-K via logsumexp.teacher_logprobs -= torch.logsumexp(teacher_logprobs, dim=-1, keepdim=True)# Build shifted student_input: prompt + completion[:-1], so position t predicts token t+1.student_input = prompt_tokens + sampled_tokens[:-1]gen_start = len(prompt_tokens) - 1target_tokens = torch.zeros(len(student_input), K, dtype=torch.long)target_tokens[gen_start : gen_start + seq_len] = teacher_tokensweights = torch.zeros(len(student_input), K)weights[gen_start : gen_start + seq_len] = teacher_logprobs.exp()datum = tinker.Datum(    model_input=tinker.ModelInput.from_ints(student_input),    loss_fn_inputs={        "target_tokens": target_tokens,        "weights": weights,    },)fwdbwd_future = await student_training_client.forward_backward_async(    [datum], loss_fn="cross_entropy")fwdbwd_result = await fwdbwd_future.result_async()
```
