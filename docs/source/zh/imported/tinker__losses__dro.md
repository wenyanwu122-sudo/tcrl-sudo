# DRO

**Type:** RL — Quadratic penalty for off-policy / offline reinforcement learning.

DRO ([Richemond et al., 2024](https://arxiv.org/abs/2405.19107); [Kimi Team et al., 2025](https://arxiv.org/abs/2501.12599)) is a general off-policy (and even offline) RL method that uses a quadratic penalty term to constrain the policy update. Note that this loss uses a different (soft) formulation of the advantage estimation, which needs to be implemented on the client side.

The DRO objective is:

LDRO(θ)=Ex∼q[log⁡pθ(x)⋅A(x)−12β(log⁡pθ(x)q(x))2]\mathcal{L}_{\text{DRO}}(\theta) = \mathbb{E}_{x \sim q}\left[\log p_\theta(x) \cdot A(x) - \frac{1}{2}\beta \left(\log \frac{p_\theta(x)}{q(x)}\right)^2\right]LDRO​(θ)=Ex∼q​[logpθ​(x)⋅A(x)−21​β(logq(x)pθ​(x)​)2]

The quadratic penalty 12β(log⁡pθq)2\frac{1}{2}\beta(\log \frac{p_\theta}{q})^221​β(logqpθ​​)2 prevents the learner from straying too far from the sampling distribution.

### Implementation[​](\#implementation)

```
# Compute quadratic penalty termquadratic_term = (target_logprobs - sampling_logprobs) ** 2# Compute DRO objectivedro_objective = target_logprobs * advantages - 0.5 * beta * quadratic_term# DRO loss is negative of objectiveloss = -dro_objective.sum()
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
  
  (scalar) — Sum of DRO losses

## Custom beta[​](\#custom-beta)

```
fwd_bwd_future = await training_client.forward_backward_async(    data=data,    loss_fn="dro",    loss_fn_config={"beta": 0.05})fwd_bwd_result = await fwd_bwd_future.result_async()
```
