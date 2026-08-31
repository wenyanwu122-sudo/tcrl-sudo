# tinker.types.LoraConfig

## *class* [**tinker.types.LoraConfig**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/types/lora_config.py\#L8)(*StrictBase*)[​](\#class-tinkertypesloraconfigstrictbase)

**Fields:**

- **rank**
  
  – LoRA rank (dimension of low-rank matrices)
- **seed**
  
  – Seed used for initialization of LoRA weights.

Useful if you need deterministic or reproducible initialization of weights. - **train_unembed** – Whether to add lora to the unembedding layer - **train_mlp** – Whether to add loras to the MLP layers (including MoE layers) - **train_attn** – Whether to add loras to the attention layers
