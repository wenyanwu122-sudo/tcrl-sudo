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
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>TCRL 文档</title>
  <style>
    :root {
      color-scheme: light;
      --ink: #111827;
      --muted: #667085;
      --line: #e5e7eb;
      --brand: #5b4bff;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      color: var(--ink);
      background: #ffffff;
    }
    a { color: inherit; text-decoration: none; }
    .topbar {
      height: 52px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 22px;
      border-bottom: 1px solid var(--line);
      background: rgba(255, 255, 255, 0.96);
      position: sticky;
      top: 0;
      z-index: 10;
    }
    .brand { display: flex; align-items: center; gap: 9px; font-weight: 700; font-size: 14px; }
    .brand-mark {
      width: 22px; height: 22px; border-radius: 7px;
      display: grid; place-items: center;
      color: #fff; font-size: 12px; font-weight: 800;
      background: linear-gradient(135deg, #6366f1, #22d3ee);
      box-shadow: 0 8px 22px rgba(99, 102, 241, 0.25);
    }
    .nav { display: flex; align-items: center; gap: 22px; font-size: 13px; color: #1f2937; }
    .nav a:hover { color: var(--brand); }
    .tools { display: flex; align-items: center; gap: 14px; font-size: 12px; color: #374151; }
    .hero {
      min-height: 230px;
      display: grid;
      place-items: center;
      text-align: center;
      padding: 52px 20px 56px;
      color: #e5ecff;
      background:
        radial-gradient(circle at 14% 24%, rgba(99, 102, 241, 0.50), transparent 30%),
        radial-gradient(circle at 84% 54%, rgba(14, 165, 233, 0.35), transparent 28%),
        linear-gradient(135deg, #131833 0%, #11182f 48%, #0e2740 100%);
    }
    .badge {
      display: inline-flex; align-items: center; gap: 6px;
      padding: 5px 11px;
      border: 1px solid rgba(255,255,255,0.18);
      border-radius: 999px;
      background: rgba(255,255,255,0.08);
      color: #cbd5e1;
      font-size: 12px;
      margin-bottom: 18px;
    }
    .badge-dot { width: 6px; height: 6px; border-radius: 50%; background: #22c55e; }
    h1 { margin: 0; font-size: clamp(38px, 4vw, 54px); line-height: 1; letter-spacing: -0.04em; color: #eef2ff; }
    .subtitle { margin: 18px auto 0; max-width: 640px; color: #a8b3cf; font-size: 15px; line-height: 1.8; }
    .actions { display: flex; justify-content: center; gap: 12px; margin-top: 24px; flex-wrap: wrap; }
    .btn {
      display: inline-flex; align-items: center; justify-content: center;
      min-width: 132px; height: 36px; padding: 0 18px;
      border-radius: 999px; font-weight: 700; font-size: 14px;
      border: 1px solid rgba(255,255,255,0.22);
    }
    .btn.primary { color: #fff; background: linear-gradient(135deg, #6857ff, #5146e5); box-shadow: 0 12px 28px rgba(81,70,229,.32); }
    .btn.secondary { color: #dbeafe; background: rgba(255,255,255,0.07); }
    .section { padding: 76px 20px 92px; background: #ffffff; }
    .section h2 { text-align: center; margin: 0; font-size: 30px; letter-spacing: -0.03em; }
    .section p.lead { text-align: center; max-width: 720px; margin: 14px auto 42px; color: var(--muted); line-height: 1.8; }
    .cards { max-width: 1040px; margin: 0 auto; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px; }
    .card {
      min-height: 206px;
      border: 1px solid #eef0f5;
      border-radius: 16px;
      padding: 26px 26px 24px;
      background: #ffffff;
      box-shadow: 0 20px 50px rgba(15, 23, 42, 0.04);
    }
    .card-top { display: flex; align-items: center; justify-content: space-between; margin-bottom: 18px; }
    .icon {
      width: 34px; height: 34px; border-radius: 12px;
      display: grid; place-items: center;
      background: #eef2ff; color: var(--brand); font-weight: 800;
    }
    .tag { color: #635bff; background: #f1f0ff; padding: 5px 9px; border-radius: 999px; font-size: 12px; font-weight: 700; }
    .card h3 { margin: 0 0 10px; font-size: 18px; }
    .card p { margin: 0 0 16px; color: #667085; font-size: 13px; line-height: 1.75; }
    .card ul { margin: 0 0 18px; padding-left: 16px; color: #344054; font-size: 13px; line-height: 1.9; }
    .card li::marker { color: var(--brand); }
    .read { color: var(--brand); font-size: 13px; font-weight: 800; }
    .footer-band { height: 34px; background: #0d1524; }
    @media (max-width: 820px) {
      .nav { display: none; }
      .cards { grid-template-columns: 1fr; }
      .topbar { padding: 0 14px; }
      .tools { gap: 8px; }
    }
  </style>
</head>
<body>
  <header class="topbar">
    <a class="brand" href="zh/main/index.html"><span class="brand-mark">T</span><span>TCRL 文档</span></a>
    <nav class="nav" aria-label="主导航">
      <a href="zh/main/imported/tinker.html">Tinker SDK</a>
      <a href="zh/main/imported/cookbook.html">Cookbook</a>
      <a href="https://tinker-docs.thinkingmachines.ai/tutorials/">教程</a>
    </nav>
    <div class="tools">
      <a href="en/main/index.html">English</a>
      <span>简体中文</span>
    </div>
  </header>

  <main>
    <section class="hero">
      <div>
        <div class="badge"><span class="badge-dot"></span><span>Beta · v0.1</span></div>
        <h1>TCRL 文档</h1>
        <p class="subtitle">完全兼容 Tinker SDK，一站式 API、Cookbook 与教程。</p>
        <div class="actions">
          <a class="btn primary" href="zh/main/index.html">为什么选择 TCRL?</a>
          <a class="btn secondary" href="zh/main/imported/tinker__quickstart.html">快速开始</a>
        </div>
      </div>
    </section>

    <section class="section">
      <h2>专注核心</h2>
      <p class="lead">专注于 LLM 后训练中真正重要的事——你的数据与算法；分布式训练的繁重工作交给我们。</p>
      <div class="cards">
        <article class="card">
          <div class="card-top"><span class="icon">S</span><span class="tag">核心 API</span></div>
          <h3>Tinker SDK</h3>
          <p>完全兼容 Tinker SDK 协议。快速开始、模型列表、损失函数、CLI，以及核心训练 / 采样客户端的完整 API 参考。</p>
          <ul><li>LoRA 微调</li><li>RL 与 SFT 损失</li><li>异步采样器</li></ul>
          <a class="read" href="zh/main/imported/tinker.html">浏览 →</a>
        </article>
        <article class="card">
          <div class="card-top"><span class="icon">C</span><span class="tag">实战示例</span></div>
          <h3>Cookbook</h3>
          <p>生产级实战配方、评测套件、偏好学习、权重管理，以及 Cookbook 的 API 参考。</p>
          <ul><li>评测套件</li><li>偏好学习</li><li>Checkpoint 工具</li></ul>
          <a class="read" href="zh/main/imported/cookbook.html">浏览 →</a>
        </article>
        <article class="card">
          <div class="card-top"><span class="icon">T</span><span class="tag">上手指南</span></div>
          <h3>教程</h3>
          <p>来自上游 Tinker 文档的分步教程，涵盖常见的端到端微调工作流。</p>
          <ul><li>SFT 全流程</li><li>RLHF 入门</li><li>真实数据集</li></ul>
          <a class="read" href="https://tinker-docs.thinkingmachines.ai/tutorials/">前往 →</a>
        </article>
      </div>
    </section>
  </main>
  <div class="footer-band"></div>
</body>
</html>
""",
        encoding="utf-8",
    )
    print(f"Built site at {SITE}")


if __name__ == "__main__":
    main()
