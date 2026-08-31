# tinker.types

All public types in the [`tinker.types`](https://github.com/thinking-machines-lab/tinker/tree/main/src/tinker/types) module, organized by function.

## Data & Input[​](\#data--input)

Types for preparing training data and model inputs.

| Type | Description |
| --- | --- |
| Datum | A single training example with input tokens and loss mask |
| ModelInput | Token sequence input for sampling or training |
| TensorData | Tensor container with dtype and shape metadata |
| EncodedTextChunk | A chunk of encoded text tokens |
| ImageChunk | Image data chunk for vision-language models |
| ImageAssetPointerChunk | Pointer to a pre-uploaded image asset |

## Training[​](\#training)

Types for configuring and observing training operations.

| Type | Description |
| --- | --- |
| ForwardBackwardOutput | Result of a forward-backward pass (loss, gradients, metrics) |
| OptimStepResponse | Result of an optimizer step |
| AdamParams | Adam optimizer hyperparameters (learning rate, betas, epsilon) |
| LoraConfig | LoRA adapter configuration (rank, which layers to train) |
| GetInfoResponse | Information about a training client's model |
| ModelData | Metadata about a model's architecture and configuration |

## Sampling & Inference[​](\#sampling--inference)

Types for text generation and sampling results.

| Type | Description |
| --- | --- |
| SamplingParams | Sampling configuration (temperature, max tokens, stop sequences) |
| SampleResponse | Response from a sampling request |
| SampledSequence | A single generated sequence with tokens and log-probabilities |
| TopkPromptLogprobs | Top-k log-probabilities over the prompt tokens |

## Models & Checkpoints[​](\#models--checkpoints)

Types for managing models, checkpoints, and training runs.

| Type | Description |
| --- | --- |
| Checkpoint | A saved model checkpoint |
| ParsedCheckpointTinkerPath | Parsed components of a tinker:// checkpoint path |
| TrainingRun | Metadata about a training run |
| SupportedModel | Information about a model supported by the server |
| GetServerCapabilitiesResponse | Server capabilities including supported models |
| CheckpointsListResponse | Paginated list of checkpoints |
| CheckpointArchiveUrlResponse | Download URL for a checkpoint archive |
| TrainingRunsResponse | Paginated list of training runs |
| Cursor | Pagination cursor for list responses |
| SaveWeightsResponse | Response from saving model weights |
| SaveWeightsForSamplerResponse | Response from saving weights for a sampler |
| WeightsInfoResponse | Minimal information for loading public checkpoints |

## Authentication & Client Configuration[​](\#authentication--client-configuration)

Types for authentication and client configuration.

| Type | Description |
| --- | --- |
| AuthTokenResponse | Response from an authentication token request |
| ClientConfigRequest | Request for client configuration |
| ClientConfigResponse | Server-provided client configuration |
