# CLI Reference

The `tinker` command-line tool manages training runs, checkpoints, and model weights.

## **tinker** [*OPTIONS*] *COMMAND*[​](\#tinker-options-command)

**Global Options** (available on all commands):

- `-f, --format [table|json]`
  
  — Output format (default: table)
- `-h, --help`
  
  — Show this message and exit

**Commands:**

- [`tinker run`](tinker__cli__run.md)
  
  — List and inspect training runs
- [`tinker checkpoint`](tinker__cli__checkpoint.md)
  
  — List, download, publish, and manage checkpoints

### tinker version[​](\#tinker-version)

Show the installed Tinker SDK version.

```
$ tinker versiontinker 0.16.1
```
