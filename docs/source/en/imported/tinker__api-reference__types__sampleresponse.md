# tinker.types.SampleResponse

## *class* [**tinker.types.SampleResponse**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/types/sample_response.py\#L18)(**)[​](\#class-tinkertypessampleresponse)

Response from a sampling request.

Contains generated sequences and optional prompt-level log probabilities. Numpy fields provide direct array access without format conversion. The corresponding Python-list properties convert lazily on first access.

**Fields:**

- **sequences**
  
  – Generated sequences. Each contains token IDs, optional logprobs, and stop reason.
- **prompt_logprobs_np**
  
  – Per-token log probabilities for the prompt as a 1-D float32 numpy array, shape
  
  `(prompt_length,)`
  
  .
  
  `NaN`
  
  at positions where logprobs were not computed (e.g. the first prompt token). None if prompt logprobs were not requested.
- **topk_prompt_logprobs_np**
  
  – Top-k prompt logprobs as a pair of dense matrices (see
  
  `TopkPromptLogprobs`
  
  ). None if top-k was not requested.

### [**prompt_logprobs**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/types/sample_response.py\#L47)()[​](\#prompt_logprobs)

Per-token log probabilities for the prompt as a Python list.

If prompt_logprobs was set to true in the request, logprobs are computed for every token in the prompt. Each entry is a float, or `None` for positions where logprobs were not computed (e.g. the first prompt token). Returns `None` if prompt logprobs were not requested.

Converted from `prompt_logprobs_np` on first access (cached afterwards).

**Returns:** `Optional[List[Optional[float]]]`

### [**topk_prompt_logprobs**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/types/sample_response.py\#L68)()[​](\#topk_prompt_logprobs)

Top-k prompt logprobs as nested Python lists.

If topk_prompt_logprobs was set to a positive integer k in the request, the top-k logprobs are computed for every token in the prompt. For each prompt position: a list of up to k `(token_id, logprob)` tuples, or `None` for positions where logprobs were not computed. Returns `None` if top-k was not requested.

Converted from `topk_prompt_logprobs_np` on first access (cached afterwards).

**Returns:** `Optional[list[Optional[list[tuple[int, float]]]]]`
