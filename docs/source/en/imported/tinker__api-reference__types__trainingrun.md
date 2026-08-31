# tinker.types.TrainingRun

## *class* [**tinker.types.TrainingRun**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/types/training_run.py\#L9)(*BaseModel*)[​](\#class-tinkertypestrainingrunbasemodel)

**Fields:**

- **training_run_id**
  
  – The unique identifier for the training run
- **base_model**
  
  – The base model name this model is derived from
- **model_owner**
  
  – The owner/creator of this model
- **is_lora**
  
  – Whether this model uses LoRA (Low-Rank Adaptation)
- **corrupted**
  
  – Whether the model is in a corrupted state
- **lora_rank**
  
  – The LoRA rank if this is a LoRA model, null otherwise
- **last_request_time**
  
  – The timestamp of the last request made to this model
- **last_checkpoint**
  
  – The most recent training checkpoint, if available
- **last_sampler_checkpoint**
  
  – The most recent sampler checkpoint, if available
- **user_metadata**
  
  – Optional metadata about this training run, set by the end-user
