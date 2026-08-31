# tinker.types.SampledSequence

## *class* [**tinker.types.SampledSequence**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/types/sampled_sequence.py\#L15)(**)[​](\#class-tinkertypessampledsequence)

A single sampled sequence from the model.

Provides two ways to access token data:

- **Numpy arrays** (`tokens_np`, `logprobs_np`): As numpy arrays without format conversion.
- **Python lists** (`tokens`, `logprobs`): Standard Python lists, converted lazily on first access.

**Fields:**

- **stop_reason**
  
  – Reason why sampling stopped.
- **tokens_np**
  
  – Generated token IDs as a 1-D int32 numpy array, shape
  
  `(num_tokens,)`
  
  .
- **logprobs_np**
  
  – Log probabilities for each generated token as a 1-D float32 numpy array, shape
  
  `(num_tokens,)`
  
  . None if logprobs were not requested.

### [**tokens**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/types/sampled_sequence.py\#L41)()[​](\#tokens)

Generated token IDs as a Python list.

Converted from `tokens_np` on first access (cached afterwards).

**Returns:** `List[int]`

### [**logprobs**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/types/sampled_sequence.py\#L53)()[​](\#logprobs)

Log probabilities for each generated token (optional).

None if logprobs were not requested. Converted from `logprobs_np` on first access (cached afterwards).

**Returns:** `Optional[List[float]]`
