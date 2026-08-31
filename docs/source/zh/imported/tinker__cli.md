# CLI 参考

`tinker` 命令行工具用于管理训练任务、检查点和模型权重。

## **tinker** [*OPTIONS*] *COMMAND*[​](\#tinker-options-command)

**全局选项**（所有命令可用）：

- `-f, --format [table|json]`
  
  — 输出格式（默认：table）
- `-h, --help`
  
  — 显示帮助信息并退出

**命令：**

- [`tinker run`](tinker__cli__run.md)
  
  — 列出和查看训练任务
- [`tinker checkpoint`](tinker__cli__checkpoint.md)
  
  — 列出、下载、发布和管理检查点

### tinker version[​](\#tinker-version)

显示已安装的 Tinker SDK 版本。

```
$ tinker versiontinker 0.16.1
```
