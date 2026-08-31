# tinker run

## **tinker run**[​](\#tinker-run-1)

Manage training runs.

### tinker run list[​](\#tinker-run-list)

List training runs with status, model info, and LoRA rank.

**Options:**

- `--limit INTEGER`
  
  — Maximum runs to fetch (default: 20, use 0 for all)
- `-c, --columns TEXT`
  
  — Columns to display (comma-separated). Available:
  
  `id`
  
  ,
  
  `model`
  
  ,
  
  `owner`
  
  ,
  
  `lora`
  
  ,
  
  `updated`
  
  ,
  
  `status`
  
  ,
  
  `checkpoint`
  
  ,
  
  `checkpoint_time`
  
  . Default:
  
  `id, model, lora, updated, status`
- `-f, --format [table|json]`
  
  — Output format (default: table)

```
$ tinker run list --limit 3         3 training runs (1377 more not shown)┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━┓┃ Run ID                              ┃ Base Model  ┃ LoRA   ┃ Last Upd  ┃ Stat  ┃┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━┩│ cda26fb4-...:train:0                │ Qwen3-8B    │ Rank 8 │ 3h ago    │ OK    ││ ea779368-...:train:0                │ Llama-3.1…  │ Rank32 │ 4h ago    │ OK    ││ 251b8fc3-...:train:0                │ Nemotron…   │ Rank32 │ 9h ago    │ OK    │└─────────────────────────────────────┴─────────────┴────────┴───────────┴───────┘
```

### tinker run info *RUN_ID*[​](\#tinker-run-info-run_id)

Show details of a specific training run.

```
$ tinker run info cda26fb4-baf6-5b13-9011-e908ccaf30b9:train:0
```
