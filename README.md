# OVO

让 Agent 交付真实工作，而不只是建议。三个独立开源产品：

| 产品 | 你会得到什么 |
| --- | --- |
| [Askovo](https://github.com/roy-tong/Askovo) | 真实研究证据、反证和可复审的产品决定 |
| [Growovo](https://github.com/roy-tong/Growovo) | 授权内的持续运营、业务回执和后续行动 |
| [Verovo](https://github.com/roy-tong/Verovo) | 独立经济事实、工具比较和优化复核 |

**官网**：[中文](https://roy-tong.github.io/ovo/) · [English](https://roy-tong.github.io/ovo/en.html) · [案例与 Demo](https://roy-tong.github.io/ovo/cases.html) · [不用安装先看结果](https://roy-tong.github.io/ovo/start.html)

Stable：Askovo `2.25.0`、Growovo `0.23.0`、Verovo `0.20.0`；Preview：Askovo `2.25.1rc3`、Growovo `0.23.1rc3`、Verovo `0.20.1rc4`。版本事实源为 `versions.json`，安装块由 `python3 assets/sync_versions.py` 同步。产品级入口为 `/askovo/`、`/growovo/`、`/verovo/`，Agent 任务清单为 `agent-tools.json`。本地 Demo 使用合成数据，公开案例链接原始来源。这里展示产品机制与实际交付，不把它写成外部采用证明。

## 本地预览

双语静态 HTML、本地字体、CSS 和 JavaScript，无需构建：

```bash
python3 -m http.server 4173 --bind 127.0.0.1
```

发布前检查中英文文案、产品切换、案例筛选、Demo 输出、命令复制、移动导航和所有链接。

---

## OVO in English

Give your agent real work, not just prompts. Three independent open-source products:

| Product | What you get |
| --- | --- |
| [Askovo](https://github.com/roy-tong/Askovo) | Real research evidence, counterevidence and reviewable product decisions |
| [Growovo](https://github.com/roy-tong/Growovo) | Authorized continuous operations, business receipts and next actions |
| [Verovo](https://github.com/roy-tong/Verovo) | Independent economic facts, tool comparisons and optimization review |

**Website**: [English](https://roy-tong.github.io/ovo/en.html) · [中文](https://roy-tong.github.io/ovo/) · [Cases & demos](https://roy-tong.github.io/ovo/en-cases.html) · [See results before installing](https://roy-tong.github.io/ovo/en-start.html)

Stable: Askovo `2.25.0`, Growovo `0.23.0` and Verovo `0.20.0`. Preview: Askovo `2.25.1rc3`, Growovo `0.23.1rc3` and Verovo `0.20.1rc4`. `versions.json` is the release source; run `python3 assets/sync_versions.py` to synchronize marked install blocks. Product entries live under `/askovo/`, `/growovo/` and `/verovo/`; `agent-tools.json` describes real first tasks. Local demos use synthetic data and public cases link to their sources. This demonstrates product mechanisms and deliverables, not external adoption.

Run the same preview command above, then check both languages, product switching, filters, demo output, copy actions, mobile navigation and links before publishing.
