# Importance Sampling

**Type:** RL — Off-policy policy gradient with importance weighting.

A common variant of the policy gradient objective ([Sutton et al., 1999](https://www.cs.cmu.edu/~sutton/poirl.html)), used when the **learner policy** pθp_\thetapθ​ may differ from the **sampling policy** qqq due to non-determinism, lagging policy updates, or other sources of on-policy discrepancy.

The naive objective:

L(θ)=Ex∼pθ[A(x)]\mathcal{L}(\theta) = \mathbb{E}_{x\sim p_\theta}\bigl[A(x)\bigr]L(θ)=Ex∼pθ​​[A(x)]

is biased when x∼qx \sim qx∼q (sampler) doesn't match x∼pθx \sim p_\thetax∼pθ​ (learner). Importance sampling corrects this:

LIS(θ)=Ex∼q[pθ(x)q(x)A(x)]\mathcal{L}_{\text{IS}}(\theta) = \mathbb{E}_{x\sim q}\Bigl[\frac{p_\theta(x)}{q(x)}A(x)\Bigr]LIS​(θ)=Ex∼q​[q(x)pθ​(x)​A(x)]

where:

- log⁡pθ(x)\log p_\theta(x)logpθ​(x)
  
  —
  
  `target_logprobs`
  
  from the learner (forward pass of
  
  `forward_backward`
  
  )
- log⁡q(x)\log q(x)logq(x)
  
  —
  
  `sampling_logprobs`
  
  from the sampler (recorded during rollout)

### Implementation[​](\#implementation)

```
# Compute probability ratioprob_ratio = torch.exp(target_logprobs - sampling_logprobs)# Compute importance-weighted lossloss = -(prob_ratio * advantages).sum()
```

### Input tensors[​](\#input-tensors)

| Key | Shape | Description |
| --- | --- | --- |
| target_tokens | (N,) | Target token IDs (from the sampler q q q ) |
| logprobs | (N,) | sampling_logprobs for the tokens |
| advantages | (N,) | Advantage values (positive to reinforce, negative to discourage) |

### Output tensors[​](\#output-tensors)

| Key | Shape | Description |
| --- | --- | --- |
| logprobs | (N,) | target_logprobs for the tokens |

### Diagnostics[​](\#diagnostics)

- `loss:sum`
  
  (scalar) — Sum of importance-weighted policy gradient losses
  
  LIS\mathcal{L}_{\text{IS}}LIS​
