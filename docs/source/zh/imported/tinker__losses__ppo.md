# PPO

**Type:** RL — Clipped surrogate objective for stable policy updates.

PPO ([Schulman et al., 2017](https://arxiv.org/abs/1707.06347)) introduces a clipping objective that limits policy updates within a close neighborhood of the sampling distribution. This prevents destructively large updates, especially when taking multiple gradient steps on the same rollout distribution.

The clipping objective is:

LCLIP(θ)=−Ex∼q[clip(pθ(x)q(x), 1−ϵlow, 1+ϵhigh)⋅A(x)]\mathcal{L}_{\text{CLIP}}(\theta) = -\mathbb{E}_{x \sim q}\left[\text{clip}\left(\frac{p_\theta(x)}{q(x)},\, 1-\epsilon_{\text{low}},\, 1+\epsilon_{\text{high}}\right) \cdot A(x)\right]LCLIP​(θ)=−Ex∼q​[clip(q(x)pθ​(x)​,1−ϵlow​,1+ϵhigh​)⋅A(x)]

The final PPO loss takes the minimum of the clipped and unclipped objectives:

LPPO(θ)=−Ex∼q[min⁡(pθ(x)q(x)⋅A(x),  clip(pθ(x)q(x), 1−ϵlow, 1+ϵhigh)⋅A(x))]\mathcal{L}_{\text{PPO}}(\theta) = -\mathbb{E}_{x \sim q}\left[\min\left(\frac{p_\theta(x)}{q(x)} \cdot A(x),\;\text{clip}\left(\frac{p_\theta(x)}{q(x)},\, 1-\epsilon_{\text{low}},\, 1+\epsilon_{\text{high}}\right) \cdot A(x)\right)\right]LPPO​(θ)=−Ex∼q​[min(q(x)pθ​(x)​⋅A(x),clip(q(x)pθ​(x)​,1−ϵlow​,1+ϵhigh​)⋅A(x))]

where ϵlow\epsilon_{\text{low}}ϵlow​ and ϵhigh\epsilon_{\text{high}}ϵhigh​ are hyperparameters (default: 0.20.20.2). Note that clipping and loss computation are applied **token-wise**.

### Implementation[​](\#implementation)

```
# Compute probability ratioprob_ratio = torch.exp(target_logprobs - sampling_logprobs)# Apply clippingclipped_ratio = torch.clamp(prob_ratio, clip_low_threshold, clip_high_threshold)# Compute both objectivesunclipped_objective = prob_ratio * advantagesclipped_objective = clipped_ratio * advantages# Take minimum (most conservative)ppo_objective = torch.min(unclipped_objective, clipped_objective)# PPO loss is negative of objectiveloss = -ppo_objective.sum()
```

### Input tensors[​](\#input-tensors)

| Key | Shape | Description |
| --- | --- | --- |
| target_tokens | (N,) | Target token IDs (from the sampler q q q ) |
| logprobs | (N,) | sampling_logprobs for the tokens |
| advantages | (N,) | Advantage values for RL |

### Output tensors[​](\#output-tensors)

| Key | Shape | Description |
| --- | --- | --- |
| logprobs | (N,) | target_logprobs for the tokens |

### Diagnostics[​](\#diagnostics)

- `loss:sum`
  
  (scalar) — Sum of PPO clipped losses

## Custom clipping thresholds[​](\#custom-clipping-thresholds)

```
fwd_bwd_future = await training_client.forward_backward_async(    data=data,    loss_fn="ppo",    loss_fn_config={"clip_low_threshold": 0.9, "clip_high_threshold": 1.1})fwd_bwd_result = await fwd_bwd_future.result_async()
```
