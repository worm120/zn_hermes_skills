# Zn's Hermes Skills

这是我的 Hermes Agent 技能库，包含个人学习记录、交易知识和自动化工具。

## 📂 目录结构

```
├── README.md                          ← 本文件
├── pdf/                               ← PDF 学习资料
│   └── htt-pa/
│       ├── HTT_PA_part1_Ch1-36.pdf    ← Al Brooks HTT PA 课程 (上半部分, 66MB)
│       └── HTT_PA_part2_Ch37-52.pdf   ← Al Brooks HTT PA 课程 (下半部分, 64MB)
├── research/
│   └── price-action-learning/         ← 价格行为学学习技能
│       ├── SKILL.md                   ← 主文件（知识+进度+流程）
│       ├── references/
│       │   └── al-brooks-price-action-rules.md  ← 88条量化交易规则
│       ├── scripts/
│       │   └── pdf_to_pngs.py         ← PDF→PNG 批处理工具
│       └── templates/
│           └── brooks-pa-monitor.pine ← TradingView Pine指标
├── autonomous-ai-agents/              ← AI代理技能
├── software-development/              ← 开发技能
├── ...                                 ← 其他Hermes官方技能
```

## 📖 价格行为学学习（当前进度）

### 已学完：第37-43章 (p.1-488)
- **第37章** — 市场周期框架 (BO/Channel/TR)
- **第38-39章** — MTR Tops & Bottoms (主要趋势反转)
- **第40章** — 通道内部交易
- **第41章** — 盘整区交易
- **第42章** — 止损与止盈
- **第43章** — 高潮与衰竭

### 待学习：第44-52章 (p.489-1375)

### 学习流程

```bash
# 1. 加载技能
hermes chat -s price-action-learning

# 2. 渲染待学章节为PNG（如果还没渲染）
python3 ~/.hermes/skills/research/price-action-learning/scripts/pdf_to_pngs.py \
  ~/.hermes/skills/pdf/htt-pa/HTT_PA_part2_Ch37-52.pdf \
  --pages 0-900 \
  --dpi 150 \
  --output /tmp/htt_pages_44_52

# 3. 用 Claude Code 分批读取（每批10-25页）
claude --dangerously-skip-permissions \
  -p "请看 /tmp/htt_pages_44_52/ 第44章的图片，提取核心交易规则，用量化表格输出" \
  --model sonnet --allowedTools 'Read' --max-turns 40

# 4. 提取的规则追加到 references 文件中
vim ~/.hermes/skills/research/price-action-learning/references/al-brooks-price-action-rules.md

# 5. 提交更新回仓库
cd ~/.hermes/skills
git add -A && git commit -m "补充第44章规则" && git push
```

### 注意事项
- ⚠️ **每批10-25页** — 超过会触发 Claude SIGINT (exit 130)
- 🎯 优先用 `--model sonnet`，视觉识别效果好
- 📊 规则用**量化表格**输出（强K线条件、进场、止损、盈亏比）
- 🔄 学习完后 `git push` 回仓库，两台机器共享进度

## 🔧 初始化公司机器

```bash
# 1. 克隆仓库到 skills 目录（必须克隆到 ~/.hermes/skills）
cd ~/.hermes
mv skills skills.bak  # 备份原技能
git clone git@github.com:worm120/zn_hermes_skills.git skills
# 或合并到现有 skills：
cd skills && git init && git remote add origin git@github.com:worm120/zn_hermes_skills.git && git fetch && git checkout -f main

# 2. 加载价格行为学技能
hermes chat -s price-action-learning

# 3. 查看已学知识和进度
# 技能加载后直接询问即可
```

## 📤 推送更新回本机

在公司学完新章节后，将提取的规则和进度推回仓库，本机 `git pull` 即可同步：

```bash
cd ~/.hermes/skills
git add -A
git commit -m "补充第N章规则 + 更新进度"
git push
# 本机执行 git pull 同步
```

## 🚀 技能加载方式

```bash
# 启动时加载
hermes chat -s price-action-learning

# 对话中加载
/skill price-action-learning
```
