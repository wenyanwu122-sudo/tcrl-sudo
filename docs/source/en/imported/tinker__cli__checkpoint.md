# tinker checkpoint

## **tinker checkpoint**[​](\#tinker-checkpoint-1)

Manage checkpoints — list, download, publish, delete, and upload to HuggingFace.

All checkpoint commands take a `CHECKPOINT_PATH` in the format `tinker://run-id/sampler_weights/final`.

All commands support `-f, --format [table|json]` for output format.

### tinker checkpoint list[​](\#tinker-checkpoint-list)

List checkpoints across all runs, or for a specific run.

**Options:**

- `-f, --format [table|json]` — Output format (default: table)
- `--run-id TEXT` — List checkpoints for a specific training run
- `--limit INTEGER` — Max checkpoints to show (default: 20, use 0 for all)

```
$ tinker checkpoint list --limit 3          3 checkpoints (1789 more not shown)┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━┳━━━━━━━┳━━━━━━━┳━━━━━━━┓┃ Checkpoint ID                  ┃ Type    ┃ Size    ┃ Pub   ┃ Crea  ┃ Expir ┃┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━╇━━━━━━━╇━━━━━━━╇━━━━━━━┩│ sampler_weights/lifecycle_test │ sampler │ 88.2 MB │ No    │ 3h    │ Never ││ sampler_weights/final          │ sampler │ 102 MB  │ No    │ 4h    │ Never ││ weights/final                  │ train   │ 306 MB  │ No    │ 4h    │ Never │└────────────────────────────────┴─────────┴─────────┴───────┴───────┴───────┘
```

### tinker checkpoint info *CHECKPOINT_PATH*[​](\#tinker-checkpoint-info-checkpoint_path)

Show details of a specific checkpoint.

```
$ tinker checkpoint info tinker://run-id/sampler_weights/final
```

**Options:**

- `-f, --format [table|json]`
  
  — Output format (default: table)

### tinker checkpoint download *CHECKPOINT_PATH*[​](\#tinker-checkpoint-download-checkpoint_path)

Download and extract a checkpoint to a local directory.

**Options:**

- `-f, --format [table|json]` — Output format (default: table)
- `-o, --output PATH` — Parent directory for extracted checkpoint (default: current directory)
- `--force` — Overwrite existing directory if it exists

```
# Download to current directory$ tinker checkpoint download tinker://run-id/sampler_weights/final# Download to a specific directory$ tinker checkpoint download tinker://run-id/sampler_weights/final -o ./models/# Force overwrite$ tinker checkpoint download tinker://run-id/sampler_weights/final --force
```

### tinker checkpoint publish *CHECKPOINT_PATH*[​](\#tinker-checkpoint-publish-checkpoint_path)

Make a checkpoint publicly accessible. Other users can load it by path.

```
$ tinker checkpoint publish tinker://run-id/sampler_weights/final
```

**Options:**

- `-f, --format [table|json]`
  
  — Output format (default: table)

### tinker checkpoint unpublish *CHECKPOINT_PATH*[​](\#tinker-checkpoint-unpublish-checkpoint_path)

Make a published checkpoint private again.

```
$ tinker checkpoint unpublish tinker://run-id/sampler_weights/final
```

**Options:**

- `-f, --format [table|json]`
  
  — Output format (default: table)

### tinker checkpoint set-ttl *CHECKPOINT_PATH*[​](\#tinker-checkpoint-set-ttl-checkpoint_path)

Set or remove the time-to-live on a checkpoint. After the TTL expires, the checkpoint is automatically deleted.

**Options:**

- `-f, --format [table|json]` — Output format (default: table)
- `--ttl SECONDS` — TTL in seconds (must be a positive integer, minimum 3600)
- `--remove` — Remove the expiration so the checkpoint is kept forever

```
# Expire after 7 days$ tinker checkpoint set-ttl tinker://run-id/sampler_weights/step-100 --ttl 604800# Keep forever (remove expiration)$ tinker checkpoint set-ttl tinker://run-id/sampler_weights/step-100 --remove
```

### tinker checkpoint delete *CHECKPOINT_PATH [...]*[​](\#tinker-checkpoint-delete-checkpoint_path-)

Permanently delete one or more checkpoints.

```
$ tinker checkpoint delete tinker://run-id/sampler_weights/step-100# Delete multiple$ tinker checkpoint delete \    tinker://run-id/sampler_weights/step-100 \    tinker://run-id/sampler_weights/step-200
```

**Options:**

- `-f, --format [table|json]`
  
  — Output format (default: table)

### tinker checkpoint push-hf *CHECKPOINT_PATH*[​](\#tinker-checkpoint-push-hf-checkpoint_path)

Upload a checkpoint to the HuggingFace Hub as a PEFT LoRA adapter.

**Options:**

- `-f, --format [table|json]` — Output format (default: table)
- `-r, --repo TEXT` — HuggingFace repo ID (e.g., `username/my-lora-adapter`). If omitted, derived from run.
- `--public` — Create or upload to a public repo (default: private)
- `--revision TEXT` — Target branch/revision
- `--commit-message TEXT` — Commit message
- `--create-pr` — Create a pull request instead of pushing to main
- `--allow-pattern TEXT` — Only upload files matching this pattern (repeatable)
- `--ignore-pattern TEXT` — Skip files matching this pattern (repeatable)
- `--no-model-card` — Do not create a README.md model card

```
$ tinker checkpoint push-hf tinker://run-id/sampler_weights/final --repo my-org/my-model$ tinker checkpoint push-hf tinker://run-id/sampler_weights/final --repo my-org/my-model --public --create-pr
```
