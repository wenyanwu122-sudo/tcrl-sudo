# tinker.types.TopkPromptLogprobs

## *class* [**tinker.types.TopkPromptLogprobs**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/types/topk_prompt_logprobs.py\#L11)(**)[​](\#class-tinkertypestopkpromptlogprobs)

Top-k most likely tokens at each prompt position, as dense numpy matrices.

Both matrices have shape `(prompt_length, k)` where `k` is the number of top tokens requested. Empty positions are filled with sentinel values (`token_id=0`, `logprob=-99999.0`).

**Fields:**

- **token_ids**
  
  – int32 matrix of token IDs, shape
  
  `(prompt_length, k)`
  
  .
- **logprobs**
  
  – float32 matrix of log probabilities, shape
  
  `(prompt_length, k)`
  
  .
