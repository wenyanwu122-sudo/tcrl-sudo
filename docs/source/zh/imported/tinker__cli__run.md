# tinker run

## **tinker run**[​](\#tinker-run-1)

管理训练任务。

### tinker run list[​](\#tinker-run-list)

列出训练任务，显示状态、模型信息和 LoRA 秩。

**选项：**

- `--limit INTEGER`
  
  — 最大获取任务数量（默认：20，使用 0 显示全部）
- `-c, --columns TEXT`
  
  — 显示的列（逗号分隔）。可用值：
  
  `id`
  
  、
  
  `model`
  
  、
  
  `owner`
  
  、
  
  `lora`
  
  、
  
  `updated`
  
  、
  
  `status`
  
  、
  
  `checkpoint`
  
  、
  
  `checkpoint_time`
  
  。默认：
  
  `id, model, lora, updated, status`
- `-f, --format [table|json]`
  
  — 输出格式（默认：table）

```
$ tinker run list --limit 3         3 training runs (1377 more not shown)┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━┓┃ Run ID                              ┃ Base Model  ┃ LoRA   ┃ Last Upd  ┃ Stat  ┃┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━┩│ cda26fb4-...:train:0                │ Qwen3-8B    │ Rank 8 │ 3h ago    │ OK    ││ ea779368-...:train:0                │ Llama-3.1…  │ Rank32 │ 4h ago    │ OK    ││ 251b8fc3-...:train:0                │ Nemotron…   │ Rank32 │ 9h ago    │ OK    │└─────────────────────────────────────┴─────────────┴────────┴───────────┴───────┘
```

### tinker run info *RUN_ID*[​](\#tinker-run-info-run_id)

显示指定训练任务的详细信息。

```
$ tinker run info cda26fb4-baf6-5b13-9011-e908ccaf30b9:train:0
```
