from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SITE = Path(os.environ.get("TCRL_DOC_SITE", str(ROOT / "site")))
LANGS = ("zh", "en")
VERSION = os.environ.get("TCRL_DOC_VERSION", "main")


def run(cmd: list[str], env: dict[str, str] | None = None) -> None:
    print("$", " ".join(cmd))
    subprocess.run(cmd, cwd=ROOT, env=env, check=True)


def main() -> None:
    SITE.mkdir(parents=True, exist_ok=True)
    for lang in LANGS:
        env = os.environ.copy()
        env["TCRL_DOC_LANG"] = lang
        env["TCRL_DOC_VERSION"] = VERSION
        src = DOCS / "source" / lang
        out = SITE / lang / VERSION
        run([
            sys.executable,
            "-m",
            "sphinx",
            "-b",
            "html",
            "-E",
            "-c",
            str(DOCS),
            str(src),
            str(out),
        ], env=env)

    root_index = SITE / "index.html"
    root_index.write_text(
        """<!doctype html>
<meta charset="utf-8">
<title>TCRL Docs</title>
<meta http-equiv="refresh" content="0; url=zh/main/index.html">
<a href="zh/main/index.html">进入中文文档</a> / <a href="en/main/index.html">Open English docs</a>
""",
        encoding="utf-8",
    )
    print(f"Built site at {SITE}")


if __name__ == "__main__":
    main()
