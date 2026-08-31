# tinker.types.AdamParams

## *class* [**tinker.types.AdamParams**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/types/optim_step_request.py\#L12)(*StrictBase*)[​](\#class-tinkertypesadamparamsstrictbase)

**Fields:**

- **learning_rate**
  
  – Learning rate for the optimizer
- **beta1**
  
  – Coefficient used for computing running averages of gradient
- **beta2**
  
  – Coefficient used for computing running averages of gradient square
- **eps**
  
  – Term added to the denominator to improve numerical stability
- **weight_decay**
  
  – Weight decay for the optimizer. Uses decoupled weight decay.
- **grad_clip_norm**
  
  – Maximum global gradient norm. If the global gradient norm is greater than this value, it will be clipped to this value. 0.0 means no clipping.
