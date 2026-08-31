# tinker checkpoint

## **tinker checkpoint**[​](\#tinker-checkpoint-1)

管理检查点 — 列出、下载、发布、删除以及上传到 HuggingFace。

所有检查点命令接受格式为 `tinker://run-id/sampler_weights/final` 的 `CHECKPOINT_PATH` 参数。

所有命令支持 `-f, --format [table|json]` 输出格式选项。

### tinker checkpoint list[​](\#tinker-checkpoint-list)

列出所有训练任务的检查点，或指定训练任务的检查点。

**选项：**

- `-f, --format [table|json]` — 输出格式（默认：table）
- `--run-id TEXT` — 列出指定训练任务的检查点
- `--limit INTEGER` — 最大显示检查点数量（默认：20，使用 0 显示全部）

```
$ tinker checkpoint list --limit 3          3 checkpoints (1789 more not shown)┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━┳━━━━━━━┳━━━━━━━┳━━━━━━━┓┃ Checkpoint ID                  ┃ Type    ┃ Size    ┃ Pub   ┃ Crea  ┃ Expir ┃┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━╇━━━━━━━╇━━━━━━━╇━━━━━━━┩│ sampler_weights/lifecycle_test │ sampler │ 88.2 MB │ No    │ 3h    │ Never ││ sampler_weights/final          │ sampler │ 102 MB  │ No    │ 4h    │ Never ││ weights/final                  │ train   │ 306 MB  │ No    │ 4h    │ Never │└────────────────────────────────┴─────────┴─────────┴───────┴───────┴───────┘
```

### tinker checkpoint info *CHECKPOINT_PATH*[​](\#tinker-checkpoint-info-checkpoint_path)

显示指定检查点的详细信息。

```
$ tinker checkpoint info tinker://run-id/sampler_weights/final
```

**选项：**

- `-f, --format [table|json]`
  
  — 输出格式（默认：table）

### tinker checkpoint download *CHECKPOINT_PATH*[​](\#tinker-checkpoint-download-checkpoint_path)

下载并解压检查点到本地目录。

**选项：**

- `-f, --format [table|json]` — 输出格式（默认：table）
- `-o, --output PATH` — 解压检查点的父目录（默认：当前目录）
- `--force` — 如果目录已存在则覆盖

```
# 下载到当前目录$ tinker checkpoint download tinker://run-id/sampler_weights/final# 下载到指定目录$ tinker checkpoint download tinker://run-id/sampler_weights/final -o ./models/# 强制覆盖$ tinker checkpoint download tinker://run-id/sampler_weights/final --force
```

### tinker checkpoint publish *CHECKPOINT_PATH*[​](\#tinker-checkpoint-publish-checkpoint_path)

将检查点设置为公开访问。其他用户可以通过路径加载。

```
$ tinker checkpoint publish tinker://run-id/sampler_weights/final
```

**选项：**

- `-f, --format [table|json]`
  
  — 输出格式（默认：table）

### tinker checkpoint unpublish *CHECKPOINT_PATH*[​](\#tinker-checkpoint-unpublish-checkpoint_path)

将已发布的检查点恢复为私有。

```
$ tinker checkpoint unpublish tinker://run-id/sampler_weights/final
```

**选项：**

- `-f, --format [table|json]`
  
  — 输出格式（默认：table）

### tinker checkpoint set-ttl *CHECKPOINT_PATH*[​](\#tinker-checkpoint-set-ttl-checkpoint_path)

设置或移除检查点的存活时间（TTL）。TTL 到期后，检查点将被自动删除。

**选项：**

- `-f, --format [table|json]` — 输出格式（默认：table）
- `--ttl SECONDS` — TTL 秒数（必须为正整数，最小值 3600）
- `--remove` — 移除过期设置，使检查点永久保留

```
# 7 天后过期$ tinker checkpoint set-ttl tinker://run-id/sampler_weights/step-100 --ttl 604800# 永久保留（移除过期设置）$ tinker checkpoint set-ttl tinker://run-id/sampler_weights/step-100 --remove
```

### tinker checkpoint delete *CHECKPOINT_PATH [...]*[​](\#tinker-checkpoint-delete-checkpoint_path-)

永久删除一个或多个检查点。

```
$ tinker checkpoint delete tinker://run-id/sampler_weights/step-100# 删除多个$ tinker checkpoint delete \    tinker://run-id/sampler_weights/step-100 \    tinker://run-id/sampler_weights/step-200
```

**选项：**

- `-f, --format [table|json]`
  
  — 输出格式（默认：table）

### tinker checkpoint push-hf *CHECKPOINT_PATH*[​](\#tinker-checkpoint-push-hf-checkpoint_path)

将检查点上传到 HuggingFace Hub 作为 PEFT LoRA 适配器。

**选项：**

- `-f, --format [table|json]` — 输出格式（默认：table）
- `-r, --repo TEXT` — HuggingFace 仓库 ID（例如 `username/my-lora-adapter`）。如果省略，则从训练任务推导。
- `--public` — 创建或上传到公开仓库（默认：私有）
- `--revision TEXT` — 目标分支/版本
- `--commit-message TEXT` — 提交信息
- `--create-pr` — 创建 Pull Request 而非直接推送到 main 分支
- `--allow-pattern TEXT` — 仅上传匹配此模式的文件（可重复使用）
- `--ignore-pattern TEXT` — 跳过匹配此模式的文件（可重复使用）
- `--no-model-card` — 不创建 README.md 模型卡片

```
$ tinker checkpoint push-hf tinker://run-id/sampler_weights/final --repo my-org/my-model$ tinker checkpoint push-hf tinker://run-id/sampler_weights/final --repo my-org/my-model --public --create-pr
```
