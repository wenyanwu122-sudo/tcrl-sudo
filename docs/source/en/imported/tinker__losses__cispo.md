# CISPO

**Type:** RL — Detached clipped importance ratio for policy gradient.

CISPO ([Chen et al., 2024](https://arxiv.org/abs/2506.13585); [Khatri et al., 2024](https://arxiv.org/abs/2510.13786)) is a policy gradient method that uses a clipped importance ratio as a coefficient. Unlike PPO which clips the objective directly, CISPO clips the ratio, **detaches it from the computation graph**, and uses it to weight the log probability.

The CISPO objective is:

LCISPO(θ)=Ex∼q[sg(clip(pθ(x)q(x), 1−ϵlow, 1+ϵhigh))⋅log⁡pθ(x)⋅A(x)]\mathcal{L}_{\text{CISPO}}(\theta) = \mathbb{E}_{x \sim q}\left[\textbf{sg}\left( \text{clip}\left(\frac{p_\theta(x)}{q(x)},\, 1-\epsilon_{\text{low}},\, 1+\epsilon_{\text{high}}\right) \right) \cdot \log p_\theta(x) \cdot A(x)\right]LCISPO​(θ)=Ex∼q​[sg(clip(q(x)pθ​(x)​,1−ϵlow​,1+ϵhigh​))⋅logpθ​(x)⋅A(x)]

The key difference from PPO: the clipping mask is detached (`sg` = stop-gradient), so it acts as a pure weighting coefficient rather than affecting the gradient flow.

### Implementation[​](\#implementation)

```
# Compute probability ratioprob_ratio = torch.exp(target_logprobs - sampling_logprobs)# Apply clippingclipped_ratio = torch.clamp(prob_ratio, clip_low_threshold, clip_high_threshold)# Compute CISPO objective (detach the clipped ratio — this is the key difference from PPO)cispo_objective = clipped_ratio.detach() * target_logprobs * advantages# CISPO loss is negative of objectiveloss = -cispo_objective.sum()
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
  
  (scalar) — Sum of CISPO losses

## Custom clipping thresholds[​](\#custom-clipping-thresholds)

```
fwd_bwd_future = await training_client.forward_backward_async(    data=data,    loss_fn="cispo",    loss_fn_config={"clip_low_threshold": 0.8, "clip_high_threshold": 1.2})fwd_bwd_result = await fwd_bwd_future.result_async()
```
