# TrainingClient

## *class* [**tinker.TrainingClient**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/training_client.py)(*holder* , *model_seq_id* , *model_id*)[​](\#class-tinkertrainingclientholder--model_seq_id--model_id)

Client for training ML models with forward/backward passes and optimization.

The TrainingClient corresponds to a fine-tuned model that you can train and sample from. You typically get one by calling `service_client.create_lora_training_client()`. **Key methods:**

- forward_backward() - compute gradients for training
- optim_step() - update model parameters with Adam optimizer
- save_weights_and_get_sampling_client() - export trained model for inference

```
training_client = service_client.create_lora_training_client(base_model="Qwen/Qwen3-8B")fwdbwd_future = training_client.forward_backward(training_data, "cross_entropy")optim_future = training_client.optim_step(types.AdamParams(learning_rate=1e-4))fwdbwd_result = fwdbwd_future.result()  # Wait for gradientsoptim_result = optim_future.result()    # Wait for parameter updatesampling_client = training_client.save_weights_and_get_sampling_client("my-model")
```

**Parameters:**

- **holder**
  
  (
  
  *InternalClientHolder*
  
  ) –
- **model_seq_id**
  
  (
  
  *int*
  
  ) –
- **model_id**
  
  (
  
  *types.ModelID*
  
  ) –

### [**forward**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/training_client.py\#L212)(*data* , *loss_fn* , *loss_fn_config=None*)[​](\#forwarddata--loss_fn--loss_fn_confignone)

Compute forward pass without gradients.

**Returns:** `APIFuture` — forward pass outputs and loss

```
data = [types.Datum(model_input=types.ModelInput.from_ints(tokenizer.encode("Hello")),loss_fn_inputs={"target_tokens": types.ModelInput.from_ints(tokenizer.encode("world"))})]future = training_client.forward(data, "cross_entropy")result = await futureprint(f"Loss: {result.loss}")
```

*Async variant:* `forward_async()`

### [**forward_backward**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/training_client.py\#L286)(*data* , *loss_fn* , *loss_fn_config=None*)[​](\#forward_backwarddata--loss_fn--loss_fn_confignone)

Compute forward pass and backward pass to calculate gradients.

**Returns:** `APIFuture` — forward/backward outputs, loss, and gradients

```
data = [types.Datum(model_input=types.ModelInput.from_ints(tokenizer.encode("Hello")),loss_fn_inputs={"target_tokens": types.ModelInput.from_ints(tokenizer.encode("world"))})]# Compute gradientsfwdbwd_future = training_client.forward_backward(data, "cross_entropy")# Update parametersoptim_future = training_client.optim_step(types.AdamParams(learning_rate=1e-4))fwdbwd_result = await fwdbwd_futureprint(f"Loss: {fwdbwd_result.loss}")
```

*Async variant:* `forward_backward_async()`

### [**forward_backward_custom**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/training_client.py\#L402)(*data* , *loss_fn* , *loss_type_input='logprobs'*)[​](\#forward_backward_customdata--loss_fn--loss_type_inputlogprobs)

Compute forward/backward with a custom loss function.

Allows you to define custom loss functions that operate on log probabilities. The custom function receives logprobs and computes loss and gradients.

**Returns:** `APIFuture` — forward/backward outputs with custom loss

```
def custom_loss(data, logprobs_list):# Custom loss computationloss = torch.mean(torch.stack([torch.mean(lp) for lp in logprobs_list]))metrics = {"custom_metric": loss.item()}return loss, metricsfuture = training_client.forward_backward_custom(data, custom_loss)result = future.result()print(f"Custom loss: {result.loss}")print(f"Metrics: {result.metrics}")
```

*Async variant:* `forward_backward_custom_async()`

### [**optim_step**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/training_client.py\#L566)(*adam_params*)[​](\#optim_stepadam_params)

Update model parameters using Adam optimizer.

The Adam optimizer used by tinker is identical to [torch.optim.AdamW](https://docs.pytorch.org/docs/stable/generated/torch.optim.AdamW.html). Note that unlike PyTorch, Tinker's default weight decay value is 0.0 (no weight decay).

**Returns:** `APIFuture` — optimizer step response

```
# First compute gradientsfwdbwd_future = training_client.forward_backward(data, "cross_entropy")# Then update parametersoptim_future = training_client.optim_step(types.AdamParams(learning_rate=1e-4,weight_decay=0.01))# Wait for both to completefwdbwd_result = await fwdbwd_futureoptim_result = await optim_future
```

*Async variant:* `optim_step_async()`

### [**save_state**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/training_client.py\#L634)(*name* , *ttl_seconds=None* , *overwrite=False*)[​](\#save_statename--ttl_secondsnone--overwritefalse)

Save model weights to persistent storage.

**Returns:** `APIFuture` — save response with checkpoint path

```
# Save after trainingsave_future = training_client.save_state("checkpoint-001")result = await save_futureprint(f"Saved to: {result.path}")
```

*Async variant:* `save_state_async()`

### [**load_state**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/training_client.py\#L730)(*path* , *weights_access_token=None*)[​](\#load_statepath--weights_access_tokennone)

Load model weights from a saved checkpoint.

This loads only the model weights, not optimizer state (e.g., Adam momentum). To also restore optimizer state, use load_state_with_optimizer.

**Returns:** `APIFuture` — load response

```
# Load checkpoint to continue training (weights only, optimizer resets)load_future = training_client.load_state("tinker://run-id/weights/checkpoint-001"))await load_future# Continue training with restored optimizer momentum
```

*Async variant:* `load_state_async()`

### [**load_state_with_optimizer**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/training_client.py\#L763)(*path* , *weights_access_token=None*)[​](\#load_state_with_optimizerpath--weights_access_tokennone)

Load model weights and optimizer state from a checkpoint.

**Returns:** `APIFuture` — load response

```
# Resume training with optimizer stateload_future = training_client.load_state_with_optimizer("tinker://run-id/weights/checkpoint-001":)await load_future# Continue training with restored optimizer momentum
```

*Async variant:* `load_state_with_optimizer_async()`

### [**save_weights_for_sampler**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/training_client.py\#L849)(*name* , *ttl_seconds=None*)[​](\#save_weights_for_samplername--ttl_secondsnone)

Save model weights for use with a SamplingClient.

**Returns:** `APIFuture` — save response with sampler path

```
# Save weights for inferencesave_future = training_client.save_weights_for_sampler("sampler-001")result = await save_futureprint(f"Sampler weights saved to: {result.path}")# Use the path to create a sampling clientsampling_client = service_client.create_sampling_client(model_path=result.path)
```

*Async variant:* `save_weights_for_sampler_async()`

### [**get_info**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/training_client.py\#L903)()[​](\#get_info)

Get information about the current model.

**Returns:** `GetInfoResponse` — model configuration and metadata

```
info = training_client.get_info()print(f"Model ID: {info.model_data.model_id}")print(f"Base model: {info.model_data.model_name}")print(f"LoRA rank: {info.model_data.lora_rank}")
```

*Async variant:* `get_info_async()`

### [**get_tokenizer**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/training_client.py\#L923)()[​](\#get_tokenizer)

Get the tokenizer for the current model.

**Returns:** `PreTrainedTokenizer` — compatible with the model

```
tokenizer = training_client.get_tokenizer()tokens = tokenizer.encode("Hello world")text = tokenizer.decode(tokens)
```

### [**create_sampling_client**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/training_client.py\#L938)(*model_path* , *retry_config=None*)[​](\#create_sampling_clientmodel_path--retry_confignone)

Create a SamplingClient from saved weights.

**Returns:** `SamplingClient` — configured with the specified weights

```
sampling_client = training_client.create_sampling_client("tinker://run-id/weights/checkpoint-001")# Use sampling_client for inference
```

*Async variant:* `create_sampling_client_async()`

### [**save_weights_and_get_sampling_client**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/training_client.py\#L970)(*name=None* , *retry_config=None*)[​](\#save_weights_and_get_sampling_clientnamenone--retry_confignone)

Save current weights and create a SamplingClient for inference.

**Returns:** `SamplingClient` — configured with the current model weights

```
# After training, create a sampling client directlysampling_client = training_client.save_weights_and_get_sampling_client()# Now use it for inferenceprompt = types.ModelInput.from_ints(tokenizer.encode("Hello"))params = types.SamplingParams(max_tokens=20)result = sampling_client.sample(prompt, 1, params).result()
```
