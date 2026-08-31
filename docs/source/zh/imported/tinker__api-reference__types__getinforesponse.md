# tinker.types.GetInfoResponse

## *class* [**tinker.types.GetInfoResponse**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/types/_pydantic_types/get_info_response.py\#L21)(*BaseModel*)[​](\#class-tinkertypesgetinforesponsebasemodel)

Response containing information about a training client's model.

**Fields:**

- **type**
  
  – Response type identifier.
- **model_data**
  
  – Detailed metadata about the model.
- **model_id**
  
  – Unique identifier for the model.
- **is_lora**
  
  – Whether this is a LoRA fine-tuned model.
- **lora_rank**
  
  – The rank of the LoRA adaptation, if applicable.
- **model_name**
  
  – The name of the model.
