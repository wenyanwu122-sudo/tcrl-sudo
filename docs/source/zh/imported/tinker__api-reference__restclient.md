# RestClient

## *class* [**tinker.RestClient**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/rest_client.py)(*holder*)[​](\#class-tinkerrestclientholder)

Client for REST API operations like listing checkpoints and metadata.

The RestClient provides access to various REST endpoints for querying model information, checkpoints, and other resources. You typically get one by calling `service_client.create_rest_client()`.

**Key methods:**

- list_checkpoints() - list available model checkpoints (both training and sampler)
- list_user_checkpoints() - list all checkpoints across all user's training runs
- get_training_run() - get model information and metadata as ModelEntry
- delete_checkpoint() - delete an existing checkpoint for a training run
- get_checkpoint_archive_url() - get signed URL to download checkpoint archive
- publish_checkpoint_from_tinker_path() - publish a checkpoint to make it public
- unpublish_checkpoint_from_tinker_path() - unpublish a checkpoint to make it private
- set_checkpoint_ttl_from_tinker_path() - set or remove TTL on a checkpoint
- assign_session_project() - move a session into a project

```
rest_client = service_client.create_rest_client()training_run = rest_client.get_training_run("run-id").result()print(f"Training Run: {training_run.training_run_id}, LoRA: {training_run.is_lora}")checkpoints = rest_client.list_checkpoints("run-id").result()print(f"Found {len(checkpoints.checkpoints)} checkpoints")for checkpoint in checkpoints.checkpoints:    print(f"  {checkpoint.checkpoint_type}: {checkpoint.checkpoint_id}")
```

**Parameters:**

- **holder**
  
  (
  
  *InternalClientHolder*
  
  ) –

### [**get_training_run**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/rest_client.py\#L86)(*training_run_id* , *access_scope='owned'*)[​](\#get_training_runtraining_run_id--access_scopeowned)

Get training run info.

**Returns:** `Future` — training run information

```
future = rest_client.get_training_run("run-id")response = future.result()print(f"Training Run ID: {response.training_run_id}, Base: {response.base_model}")
```

*Async variant:* `get_training_run_async()`

### [**get_training_run_by_tinker_path**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/rest_client.py\#L117)(*tinker_path* , *access_scope='owned'*)[​](\#get_training_run_by_tinker_pathtinker_path--access_scopeowned)

Get training run info.

**Returns:** `Future` — training run information

```
future = rest_client.get_training_run_by_tinker_path("tinker://run-id/weights/checkpoint-001")response = future.result()print(f"Training Run ID: {response.training_run_id}, Base: {response.base_model}")
```

*Async variant:* `get_training_run_by_tinker_path_async()`

### [**get_weights_info_by_tinker_path**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/rest_client.py\#L157)(*tinker_path*)[​](\#get_weights_info_by_tinker_pathtinker_path)

Get checkpoint information from a tinker path.

**Returns:** `APIFuture` — checkpoint information (awaitable)

```
future = rest_client.get_weights_info_by_tinker_path("tinker://run-id/weights/checkpoint-001")response = future.result()  # or await futureprint(f"Base Model: {response.base_model}, LoRA Rank: {response.lora_rank}")
```

### [**list_training_runs**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/rest_client.py\#L218)(*limit=20* , *offset=0* , *access_scope='owned'*)[​](\#list_training_runslimit20--offset0--access_scopeowned)

List training runs with pagination support.

**Returns:** `Future` — `TrainingRunsResponse` with training runs and cursor info

```
future = rest_client.list_training_runs(limit=50)response = future.result()print(f"Found {len(response.training_runs)} training runs")print(f"Total: {response.cursor.total_count}")# Get next pagenext_page = rest_client.list_training_runs(limit=50, offset=50)
```

*Async variant:* `list_training_runs_async()`

### [**list_checkpoints**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/rest_client.py\#L279)(*training_run_id*)[​](\#list_checkpointstraining_run_id)

List available checkpoints (both training and sampler).

**Returns:** `Future` — `CheckpointsListResponse` with available checkpoints

```
future = rest_client.list_checkpoints("run-id")response = future.result()for checkpoint in response.checkpoints:    if checkpoint.checkpoint_type == "training":        print(f"Training checkpoint: {checkpoint.checkpoint_id}")    elif checkpoint.checkpoint_type == "sampler":        print(f"Sampler checkpoint: {checkpoint.checkpoint_id}")
```

*Async variant:* `list_checkpoints_async()`

### [**get_checkpoint_archive_url**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/rest_client.py\#L343)(*training_run_id* , *checkpoint_id*)[​](\#get_checkpoint_archive_urltraining_run_id--checkpoint_id)

Get signed URL to download checkpoint archive.

**Returns:** `Future` — `CheckpointArchiveUrlResponse` with signed URL and expiration

```
future = rest_client.get_checkpoint_archive_url("run-id", "checkpoint-123")response = future.result()print(f"Download URL: {response.url}")print(f"Expires at: {response.expires_at}")# Use the URL to download the archive with your preferred HTTP client
```

*Async variant:* `get_checkpoint_archive_url_async()`

### [**delete_checkpoint**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/rest_client.py\#L392)(*training_run_id* , *checkpoint_id*)[​](\#delete_checkpointtraining_run_id--checkpoint_id)

Delete a checkpoint for a training run.

**Returns:** `ConcurrentFuture[None]`

*Async variant:* `delete_checkpoint_async()`

### [**delete_checkpoint_from_tinker_path**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/rest_client.py\#L409)(*tinker_path*)[​](\#delete_checkpoint_from_tinker_pathtinker_path)

Delete a checkpoint referenced by a tinker path.

**Returns:** `ConcurrentFuture[None]`

*Async variant:* `delete_checkpoint_from_tinker_path_async()`

### [**get_audit_log**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/rest_client.py\#L428)(*event_type='all'* , *day=None*)[​](\#get_audit_logevent_typeall--daynone)

Get an audit log of events for the caller's organization.

Requires the tinker-admin RBAC role (VIEW_AUDIT_LOG capability).

**Returns:** `Future` — `AuditLogResponse` with audit log entries

```
from datetime import datefuture = rest_client.get_audit_log()response = future.result()print(f"Found {len(response.entries)} audit entries")for entry in response.entries:    print(f"  {entry.timestamp}: {entry.event} ({entry.tinker_path})")# Query a specific dayfuture = rest_client.get_audit_log(day=date(2025, 1, 15))
```

*Async variant:* `get_audit_log_async()`

### [**get_checkpoint_archive_url_from_tinker_path**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/rest_client.py\#L490)(*tinker_path*)[​](\#get_checkpoint_archive_url_from_tinker_pathtinker_path)

Get signed URL to download checkpoint archive.

**Returns:** `Future` — `CheckpointArchiveUrlResponse` with signed URL and expiration

*Async variant:* `get_checkpoint_archive_url_from_tinker_path_async()`

### [**publish_checkpoint_from_tinker_path**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/rest_client.py\#L535)(*tinker_path*)[​](\#publish_checkpoint_from_tinker_pathtinker_path)

Publish a checkpoint referenced by a tinker path to make it publicly accessible.

Only the exact owner of the training run can publish checkpoints. Published checkpoints can be unpublished using the unpublish_checkpoint_from_tinker_path method.

**Returns:** `Future` — completes when the checkpoint is published

```
future = rest_client.publish_checkpoint_from_tinker_path("tinker://run-id/weights/0001")future.result()  # Wait for completionprint("Checkpoint published successfully")
```

*Async variant:* `publish_checkpoint_from_tinker_path_async()`

### [**unpublish_checkpoint_from_tinker_path**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/rest_client.py\#L592)(*tinker_path*)[​](\#unpublish_checkpoint_from_tinker_pathtinker_path)

Unpublish a checkpoint referenced by a tinker path to make it private again.

Only the exact owner of the training run can unpublish checkpoints. This reverses the effect of publishing a checkpoint.

**Returns:** `Future` — completes when the checkpoint is unpublished

```
future = rest_client.unpublish_checkpoint_from_tinker_path("tinker://run-id/weights/0001")future.result()  # Wait for completionprint("Checkpoint unpublished successfully")
```

*Async variant:* `unpublish_checkpoint_from_tinker_path_async()`

### [**set_checkpoint_ttl_from_tinker_path**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/rest_client.py\#L650)(*tinker_path* , *ttl_seconds*)[​](\#set_checkpoint_ttl_from_tinker_pathtinker_path--ttl_seconds)

Set or remove the TTL on a checkpoint referenced by a tinker path.

If ttl_seconds is provided, the checkpoint will expire after that many seconds from now. If ttl_seconds is None, any existing expiration will be removed.

**Returns:** `Future` — completes when the TTL is set

```
future = rest_client.set_checkpoint_ttl_from_tinker_path("tinker://run-id/weights/0001", 86400)future.result()  # Wait for completionprint("Checkpoint TTL set successfully")
```

*Async variant:* `set_checkpoint_ttl_from_tinker_path_async()`

### [**list_user_checkpoints**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/rest_client.py\#L714)(*limit=100* , *offset=0*)[​](\#list_user_checkpointslimit100--offset0)

List all checkpoints for the current user across all their training runs.

This method retrieves checkpoints from all training runs owned by the authenticated user, sorted by time (newest first). It supports pagination for efficiently handling large numbers of checkpoints.

**Returns:** `Future` — `CheckpointsListResponse` with checkpoints and cursor info

```
future = rest_client.list_user_checkpoints(limit=50)response = future.result()print(f"Found {len(response.checkpoints)} checkpoints")print(f"Total: {response.cursor.total_count if response.cursor else 'Unknown'}")for checkpoint in response.checkpoints:    print(f"  {checkpoint.training_run_id}/{checkpoint.checkpoint_id}")# Get next page if there are more checkpointsif response.cursor and response.cursor.offset + response.cursor.limit < response.cursor.total_count:    next_page = rest_client.list_user_checkpoints(limit=50, offset=50)
```

*Async variant:* `list_user_checkpoints_async()`

### [**get_session**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/rest_client.py\#L774)(*session_id* , *access_scope='owned'*)[​](\#get_sessionsession_id--access_scopeowned)

Get session information including all training runs and samplers.

**Returns:** `Future` — `GetSessionResponse` with training_run_ids and sampler_ids

```
future = rest_client.get_session("session-id")response = future.result()print(f"Training runs: {len(response.training_run_ids)}")print(f"Samplers: {len(response.sampler_ids)}")
```

*Async variant:* `get_session_async()`

### [**list_sessions**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/rest_client.py\#L831)(*limit=20* , *offset=0* , *access_scope='owned'*)[​](\#list_sessionslimit20--offset0--access_scopeowned)

List sessions with pagination support.

**Returns:** `Future` — `ListSessionsResponse` with list of session IDs

```
future = rest_client.list_sessions(limit=50)response = future.result()print(f"Found {len(response.sessions)} sessions")# Get next pagenext_page = rest_client.list_sessions(limit=50, offset=50)
```

*Async variant:* `list_sessions_async()`

### [**assign_session_project**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/rest_client.py\#L895)(*session_id* , *project_id*)[​](\#assign_session_projectsession_id--project_id)

Move a session (and all of its training runs/samplers) into a project.

Use this to attach a previously-created session to a project, or to move a session between projects. Clearing the project is not supported — sessions cannot be moved out of a project once placed.

**Returns:** `Future` — completes when the session has been moved

```
future = rest_client.assign_session_project("session-id", "project-id")future.result()
```

*Async variant:* `assign_session_project_async()`

### [**get_sampler**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/rest_client.py\#L928)(*sampler_id*)[​](\#get_samplersampler_id)

Get sampler information.

**Returns:** `APIFuture` — `GetSamplerResponse` with sampler details

```
# Sync usagefuture = rest_client.get_sampler("session-id:sample:0")response = future.result()print(f"Base model: {response.base_model}")print(f"Model path: {response.model_path}")# Async usageresponse = await rest_client.get_sampler("session-id:sample:0")print(f"Base model: {response.base_model}")
```
