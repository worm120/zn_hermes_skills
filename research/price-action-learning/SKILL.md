---
name: price-action-learning
description: "Al Brooks Price Action (HTT PA) 学习技能 — 课程知识、进度跟踪、Claude Code 批处理流程"
version: 1.0.0
author: Agent
created_by: agent
platforms: [linux, macos]
tags: [trading, price-action, al-brooks, learning]
metadata:
  progress:
    pdf: /home/zn/Downloads/HTT PA(带书签).pdf
    total_pages: 1375
    chapters_done: "37-43"
    chapters_remaining: "44-52"
    pages_done: 1-488
    pages_remaining: 489-1375
---

# Al Brooks Price Action — HTT PA 学习技能

## 课程概览

| 项目 | 内容 |
|------|------|
| 教材 | HTT PA(带书签).pdf (1375页) |
| 基础篇 | 1_阿布PA基础1-36.pdf (370MB) |
| 进阶篇 | 2_阿布PA进阶37-52.pdf (266MB) |
| 已学完 | 第37-43章 (p.1-488) |
| 待学习 | 第44-52章 (p.489-1375) |

---

## 已学内容（第37-43章）

### 第37章 — 市场周期框架 BO/Channel/TR

**三大市场状态：**
- **Breakout (突破)** — 价格突破现有结构，强动量 K 线
- **Channel (通道)** — 趋势持续阶段，有角度的价格走廊
- **Trading Range (TR / 盘整区)** — 价格在一定范围内震荡，无明确方向

**循环规律：** BO → Channel → TR → BO → ... 市场在这三种状态间循环。

### 第38-39章 — MTR Tops & Bottoms (主要趋势反转顶底)

- **MTR Top:** 长时间上涨后的反转顶部形态，通常包含楔形 (wedge) 或双顶
- **MTR Bottom:** 长时间下跌后的反转底部形态，通常包含楔形或双底
- **关键规则:** 反转需要 **跟进确认 (follow-through)**，单根K线反转不可靠

### 第40章 — 通道内部交易

- 窄通道只顺趋势方向交易（pullback entries）
- 宽通道可以高抛低吸（mean reversion）
- 通道宽度测量：用 ATR 和通道线的斜率判断

### 第41章 — 盘整区交易

- 80%的突破会失败 → 逆突破交易更可靠
- 用 80% 规则判断盘整区内的动量延续
- 双顶/双底/楔形是盘整区内最高质量信号

### 第42章 — 止损与止盈

- 最小盈亏比 >= 1:2
- 止损放在信号K线对面极值 +1 tick
- 强趋势中至少让一部分仓位奔跑

### 第43章 — 高潮与衰竭

- 卖出高潮：窄通道 + >=4根连续强牛K线 + ATR放大
- 买入高潮：窄通道 + >=4根连续强熊K线 + ATR放大
- 高潮后不追，等待反转信号+跟进确认

---

## 已提取的量化规则

完整的量化规则表见：
`autonomous-ai-agents/claude-code/references/al-brooks-price-action-rules.md`

包含：
- 市场状态机：通道侦测表（窄牛/窄熊/宽牛/宽熊/盘整区）
- 强K线检测公式
- 各状态下的具体交易规则
- 止损/止盈规则
- 高潮检测条件
- 何时不交易

TradingView Pine Script 监控指标：
`autonomous-ai-agents/claude-code/templates/brooks-pa-monitor.pine`

---

## 继续学习（第44-52章）

### 学习流程

```bash
# 1. 渲染待学习章节的PDF为PNG
python3 scripts/pdf_to_pngs.py "/path/to/HTT PA(带书签).pdf" \
  --pages 488-1375 \
  --dpi 150 \
  --output /tmp/htt_pages_44_52

# 2. 分批次用 Claude Code 读取（每批10-25页，多了会SIGINT）
claude --dangerously-skip-permissions \
  -p "请看 /tmp/htt_pages_44_52/page_0489.png 到 page_0510.png，提取第44章的核心交易规则，用量化表格输出" \
  --model sonnet --allowedTools 'Read' --max-turns 40

# 3. 将提取的规则追加到 references 文件中
```

### 注意事项
- **批量大小：** 每次10-25页最佳（超过会触发 SIGINT exit 130）
- **模型：** 优先用 `sonnet`，视觉识别效果好
- **记录方式：** 每章提取的规则按量化表格格式输出（强K线条件、进场条件、止损位、盈亏比要求）
- **已渲染的图片：** `/tmp/htt_pages/` 下有全部1375页的PNG

---

## PDF 文件

> ⚠️ PDF 文件体积较大（130-370MB），不推荐放在 git 仓库中。

**获取方式：**
1. **scp 拷贝到公司机器：**
   ```bash
   scp /home/zn/Downloads/HTT\ PA\(带书签\).pdf user@公司机器:~/pa/
   scp /home/zn/Downloads/1_阿布PA基础1-36.pdf user@公司机器:~/pa/
   scp /home/zn/Downloads/2_阿布PA进阶37-52.pdf user@公司机器:~/pa/
   ```
2. **使用网盘链接**（如百度云/阿里云）
3. **在目标机器上重新渲染 PNG：**
   ```bash
   python3 ~/.hermes/skills/autonomous-ai-agents/claude-code/scripts/pdf_to_pngs.py ~/pa/HTT\ PA\(带书签\).pdf --output /tmp/htt_pages
   ```
