# Reproducible Social Science Research Template

A lifecycle-based repository template for quantitative and computational social science. It keeps data collection, analysis, manuscripts, slides, releases, and replication materials in one traceable workflow.

**Designed for:** Python, R, LaTeX, Word, and PowerPoint research projects where every result should be traceable to its inputs and source code.

**Includes:** a clear data/code/output boundary, versioned manuscript and slide releases, and Python/R replication entry points.

## Quick start

Use **Use this template** on GitHub, or clone it locally:

```bash
git clone https://github.com/Yuxuan-THU/research-project-template.git my-research-project
cd my-research-project
python replication/run_all.py
```

## Citation and license

When this template materially informs a project workflow, cite the repository URL, release or commit, and access date. This repository is released under the MIT License.

---

## 中文说明

一套面向量化社会科学、计算社会科学与 AI for Social Science 的通用项目目录。它把数据获取、数据清洗、统计分析、论文写作、演示文稿和复现交付放进同一个可追踪的研究流程，同时兼容 Python、R、LaTeX、Word 和 PowerPoint。

## 背景与来龙去脉

许多研究项目最初只有“论文、PPT、数据代码、历史文件”几类目录。项目变复杂后，常见问题也随之出现：原始数据和清洗数据混在一起，采集代码和分析代码相互交叉，论文中的表图找不到生成脚本，Word/PPT 出现大量 `final_v2_最终版`，复现材料则在投稿前临时拼装。

本模板由这些实际问题反推而来。它不按文件格式分类，而是按研究生命周期划分职责：

```text
获取数据 → 保存原始数据 → 清洗 → 分析 → 生成结果 → 写作与汇报 → 冻结版本 → 复现
```

核心目标只有三个：

1. 任意结果都能追溯到生成代码和输入数据；
2. 当前工作稿与正式历史版本明确分开；
3. 本机工作、Git 版本控制和公开复现使用同一套结构。

## 目录结构

```text
project-name/
├── README.md                 # 项目总说明
├── CHANGELOG.md              # 全项目唯一变更记录
├── AGENTS.md                 # Agent 工作与推送规则
├── .gitignore
├── docs/                     # 研究计划、决策和会议记录
├── data/
│   ├── collection/           # 爬虫、API 和其他数据采集代码
│   └── raw/                  # 未经人工修改的原始数据
├── source/
│   ├── cleaning/             # 清洗、合并和构造分析数据的代码
│   └── analysis/             # 统计分析、机器学习和绘图代码
├── outputs/
│   ├── data/                 # 清洗代码生成的分析数据
│   ├── figures/              # 代码生成的图片
│   ├── tables/               # 代码生成的表格
│   ├── models/               # 模型文件或模型指针
│   └── other/                # 日志、诊断等其他派生产物
├── manuscript/
│   ├── source/               # 当前唯一论文工作稿
│   └── releases/             # 投稿、返修、接收等冻结版本
├── slides/
│   ├── source/               # 当前唯一演示文稿工作稿
│   └── releases/             # 会议、组会、答辩等冻结版本
└── replication/
    ├── MANIFEST.csv          # 结果—代码—数据对应表
    ├── run_all.py            # Python 一键复现入口
    └── run_all.R             # R 一键复现入口
```

目录中的 `.gitkeep` 仅用于让 Git 保留空文件夹，开始项目后可以保留或删除。

## 三组关键关系

### `data`、`source` 与 `outputs`

- `data/collection/` 负责获取数据，结果写入 `data/raw/`。
- `data/raw/` 是只读输入，不在其中直接清洗或覆盖文件。
- `source/cleaning/` 读取原始数据，生成 `outputs/data/` 中的分析数据。
- `source/analysis/` 读取分析数据，生成 `outputs/tables/`、`outputs/figures/` 和 `outputs/models/`。
- `outputs/` 中的内容原则上由代码生成；发现错误时修改源代码，不手工修补生成结果。

### `manuscript/source` 与 `manuscript/releases`

- `source/` 保存持续编辑的当前权威工作稿，例如 `main.tex` 或 `main.docx`。
- `releases/` 保存重要节点的不可变快照，例如 `2026-10-12_submission-r1/`。
- 日常版本由 Git 管理，不创建 `main_final_v3` 一类副本。
- Word 的句子级变化使用修订模式；投稿时同时冻结可编辑文件与 PDF。

### `replication`

`replication/` 是复现控制台，不是第二套代码目录。`run_all.py` 或 `run_all.R` 按顺序调用 `data/collection/`、`source/cleaning/` 和 `source/analysis/` 中的正式代码；`MANIFEST.csv` 则记录每个表图对应的输出文件、生成脚本、输入数据、Git commit 和检查状态。

## 快速开始

在 GitHub 页面点击 **Use this template**，或直接克隆：

```bash
git clone https://github.com/Yuxuan-THU/research-project-template.git my-research-project
cd my-research-project
```

然后：

1. 修改本 README，填写研究问题、负责人、数据权限和运行环境；
2. 将采集代码放入 `data/collection/`，原始数据放入 `data/raw/`；
3. 将清洗与分析代码分别放入 `source/cleaning/` 和 `source/analysis/`；
4. 根据主要语言保留一个复现入口；
5. 检查 `.gitignore` 后再进行第一次提交。

运行 Python 流程：

```bash
python replication/run_all.py
python replication/run_all.py --include-collection
```

运行 R 流程：

```bash
Rscript replication/run_all.R
Rscript replication/run_all.R --include-collection
```

脚本按文件名排序运行，建议使用 `01_`、`02_`、`03_` 表示执行顺序。

## 数据与隐私

模板默认忽略 `data/raw/`、`outputs/data/`、模型文件、密钥和本机环境文件。公开项目前仍需人工确认：

- 数据许可是否允许公开；
- 是否包含个人可识别信息或敏感字段；
- API 密钥、Cookie、账号和密码是否已移除；
- 大文件是否应改用 OSF、Dataverse、Zenodo 或 Git LFS。

原始数据不能公开时，应公开获取方法、变量说明和可运行代码，而不是上传受限数据。

## 版本管理约定

- 全项目只使用根目录的 `README.md` 和 `CHANGELOG.md`。
- 子目录不再建立 README 或 CHANGELOG。
- 具有研究意义的变化写入 `CHANGELOG.md`；细小编辑由 Git commit 保存。
- `AGENTS.md` 要求 Agent 在每次 `git push` 前检查并更新 CHANGELOG。
- 论文和幻灯片的正式节点使用日期加阶段命名，并且冻结后不再覆盖。

示例：

```text
manuscript/releases/2026-10-12_submission-r1/
manuscript/releases/2027-02-08_revision-r1/
slides/releases/2026-09-15_conference/
```

## 自定义项目

这是一个起点，而不是强制标准。正式使用时可以删除不需要的语言入口，也可以增加环境锁定文件、问卷、预分析计划或期刊要求的材料，但应保持“输入、代码、输出、工作稿、冻结版本、复现入口”之间的边界。
