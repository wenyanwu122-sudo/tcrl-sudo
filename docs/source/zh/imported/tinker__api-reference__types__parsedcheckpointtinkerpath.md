# tinker.types.ParsedCheckpointTinkerPath

## *class* [**tinker.types.ParsedCheckpointTinkerPath**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/types/checkpoint.py\#L34)(*BaseModel*)[​](\#class-tinkertypesparsedcheckpointtinkerpathbasemodel)

**Fields:**

- **tinker_path**
  
  – The tinker path to the checkpoint
- **training_run_id**
  
  – The training run ID
- **checkpoint_type**
  
  – The type of checkpoint (training or sampler)
- **checkpoint_id**
  
  – The checkpoint ID

### [**from_tinker_path**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/types/checkpoint.py\#L48)(*tinker_path*)[​](\#from_tinker_pathtinker_path)

Parse a tinker path to an instance of ParsedCheckpointTinkerPath

**Returns:** `'ParsedCheckpointTinkerPath'`
