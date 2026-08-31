# ServiceClient

## *class* [**tinker.ServiceClient**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/service_client.py)(*user_metadata=None* , *project_id=None*)[​](\#class-tinkerserviceclientuser_metadatanone--project_idnone)

The ServiceClient is the main entry point for the Tinker API. It provides methods to:

- Query server capabilities and health status
- Generate TrainingClient instances for model training workflows
- Generate SamplingClient instances for text generation and inference
- Generate RestClient instances for REST API operations like listing weights

```
# Near instantclient = ServiceClient()# Takes a moment as we initialize the model and assign resourcestraining_client = client.create_lora_training_client(base_model="Qwen/Qwen3-8B")# Near-instantsampling_client = client.create_sampling_client(base_model="Qwen/Qwen3-8B")# Near-instantrest_client = client.create_rest_client()
```

**Parameters:**

- **user_metadata**
  
  (
  
  *dict[str, str] | None*
  
  ) – Default:
  
  `None`
  
  .
- **project_id**
  
  (
  
  *str | None*
  
  ) – Default:
  
  `None`
  
  .

### [**get_server_capabilities**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/service_client.py\#L91)()[​](\#get_server_capabilities)

Query the server's supported features and capabilities.

**Returns:** `GetServerCapabilitiesResponse` — available models, features, and limits

```
capabilities = service_client.get_server_capabilities()print(f"Supported models: {capabilities.supported_models}")print(f"Max batch size: {capabilities.max_batch_size}")
```

*Async variant:* `get_server_capabilities_async()`

### [**create_lora_training_client**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/service_client.py\#L165)(*base_model* , *rank=32* , *seed=None* , *train_mlp=True* , *train_attn=True* , *train_unembed=True* , *user_metadata=None*)[​](\#create_lora_training_clientbase_model--rank32--seednone--train_mlptrue--train_attntrue--train_unembedtrue--user_metadatanone)

Create a TrainingClient for LoRA fine-tuning.

**Returns:** `TrainingClient` configured for LoRA training

```
training_client = service_client.create_lora_training_client(base_model="Qwen/Qwen3-8B",rank=16,train_mlp=True,train_attn=True)# Now use training_client.forward_backward() to train
```

*Async variant:* `create_lora_training_client_async()`

### [**create_training_client_from_state**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/service_client.py\#L245)(*path* , *user_metadata=None* , *weights_access_token=None*)[​](\#create_training_client_from_statepath--user_metadatanone--weights_access_tokennone)

Create a TrainingClient from saved model weights.

This loads only the model weights, not optimizer state. To also restore optimizer state (e.g., Adam momentum), use create_training_client_from_state_with_optimizer.

**Returns:** `TrainingClient` loaded with the specified weights

```
# Resume training from a checkpoint (weights only, optimizer resets)training_client = service_client.create_training_client_from_state("tinker://run-id/weights/checkpoint-001")# Continue training from the loaded state
```

*Async variant:* `create_training_client_from_state_async()`

### [**create_training_client_from_state_with_optimizer**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/service_client.py\#L323)(*path* , *user_metadata=None* , *weights_access_token=None*)[​](\#create_training_client_from_state_with_optimizerpath--user_metadatanone--weights_access_tokennone)

Create a TrainingClient from saved model weights and optimizer state.

This is similar to create_training_client_from_state but also restores optimizer state (e.g., Adam momentum), which is useful for resuming training exactly where it left off.

**Returns:** `TrainingClient` loaded with the specified weights and optimizer state

```
# Resume training from a checkpoint with optimizer statetraining_client = service_client.create_training_client_from_state_with_optimizer("tinker://run-id/weights/checkpoint-001")# Continue training with restored optimizer momentum
```

*Async variant:* `create_training_client_from_state_with_optimizer_async()`

### [**create_sampling_client**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/service_client.py\#L403)(*model_path=None* , *base_model=None* , *retry_config=None*)[​](\#create_sampling_clientmodel_pathnone--base_modelnone--retry_confignone)

Create a SamplingClient for text generation.

**Returns:** `SamplingClient` configured for text generation

```
# Use a base modelsampling_client = service_client.create_sampling_client(base_model="Qwen/Qwen3-8B")# Or use saved weightssampling_client = service_client.create_sampling_client(model_path="tinker://run-id/weights/checkpoint-001")
```

*Async variant:* `create_sampling_client_async()`

### [**create_rest_client**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/service_client.py\#L464)()[​](\#create_rest_client)

Create a RestClient for REST API operations.

The RestClient provides access to various REST endpoints for querying model information, checkpoints, sessions, and managing checkpoint visibility.

**Returns:** `RestClient` for accessing REST API endpoints

```
rest_client = service_client.create_rest_client()# List checkpoints for a training runcheckpoints = rest_client.list_checkpoints("run-id").result()# Get training run infotraining_run = rest_client.get_training_run("run-id").result()# Publish a checkpointrest_client.publish_checkpoint_from_tinker_path("tinker://run-id/weights/checkpoint-001").result()
```
