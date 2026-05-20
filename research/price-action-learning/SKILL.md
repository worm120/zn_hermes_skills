---
name: price-action-learning
description: "Al Brooks Price Action (HTT PA) 学习技能 — 完整进阶篇知识体系、量化规则、视觉分析工作流"
version: 2.0.0
author: Agent
created_by: agent
platforms: [linux, macos]
tags: [trading, price-action, al-brooks, completed]
metadata:
  progress:
    pdf_part1: /home/zn/.hermes/skills/pdf/htt-pa/HTT_PA_part1_Ch1-36.pdf
    pdf_part2: /home/zn/.hermes/skills/pdf/htt-pa/HTT_PA_part2_Ch37-52.pdf
    total_pages: 1375
    chapters_done: "37-52 (全部进阶篇)"
    status: COMPLETED
    completed_date: "2026-05-20"
---

# Al Brooks Price Action — HTT PA 学习技能

## 课程概览

| 项目 | 内容 |
|------|------|
| 教材 | HTT PA(带书签).pdf (1375页) |
| 基础篇 | 1_阿布PA基础1-36.pdf (370MB) — 未学习 |
| 进阶篇 | 2_阿布PA进阶37-52.pdf (266MB) — **已全部学完** |
| 已学完 | 第37-52章 (全部进阶篇, p.1-1375) |
| 待学习 | 无 |

## 完整知识体系

### 市场状态机（一切交易的基础）

```
市场循环: BO → Channel → TR → BO → ...

BO (突破): 强动量，按突破交易，25%成功
  ├─ 成功 → 新趋势/通道
  └─ 75-80%失败 → 返回TR

Channel (通道):
  ├─ Tight (紧窄): 回调浅(1-3根K线)，只做趋势方向，胜率60-70%+
  │   ├─ Tight Bull: Only buy, pullback entry
  │   └─ Tight Bear: Only sell, pullback entry
  └─ Broad (宽幅): 回调深(>50%)，双向交易，胜率~55%
      ├─ Broad Bull: Buy for swings/scalps, sell for scalps
      └─ Broad Bear: Sell for swings/scalps, buy for scalps
      └─ 两者都≈盘整区（90%的K线行为相同）

TR (盘整区): 无明显方向，胜率~50%
  ├─ 80%突破失败 → 逆突破交易更可靠
  ├─ BLSHS: Buy Low, Sell High, Scalp
  └─ 底部1/3买入，顶部1/3卖出
```

### 核心概率体系

| 市场环境 | 胜率 | 策略 |
|---------|------|------|
| 紧窄通道(顺趋势) | 60-70%+ | Swing |
| 宽幅通道(顺趋势) | ~55-60% | Swing/Scalp |
| 宽幅通道(逆趋势) | ~45% | Scalp only |
| 盘整区(TR) | ~50% | BLSHS |
| 突破成功 | 20-25% | 但成功后回报大 |
| 突破失败(逆突破) | 75-80% | 逆突破交易更可靠 |
| 50%回调(趋势中) | ~60% | Limit order |

### Trader's Equation（交易者方程）

```
期望值 = Probability × Reward - (1 - Probability) × Risk

Risk = |entry - stop|     (止损距离)
Reward = |target - entry| (目标距离)
Probability = 止损前获利的概率

正期望值条件: Probability × Reward > (1 - Probability) × Risk

50%回调做多: 60%胜率 × 1:1盈亏比 = 正期望值
```

### 10条核心交易原则

1. **永远先判断市场状态**（紧窄/宽幅/TR）→ 执行对应策略
2. **紧窄通道只做趋势方向**，不做逆势
3. **宽幅通道可双向交易**但顺趋势优先
4. **TR内80%突破失败** → 逆突破交易更可靠
5. **不确定时假设是紧窄通道**（保守原则）
6. **HTF确认强度**（5分钟紧窄 = HTF上的突破）
7. **50%回调是黄金入场点**（1:1风险回报，60%胜率）
8. **每次交易前明确：** 止损位、目标位、胜率估计
9. **强反转时提前出场**，不等止损被触发
10. **分批止盈：** 部分scalp锁定利润，部分swing跟随趋势

---

## 已学内容（第37-52章，全部进阶篇）

### 第37章 — 市场周期框架 BO/Channel/TR
**三大市场状态：** 突破(BO) / 通道(Channel) / 盘整区(TR)
**循环规律：** BO → Channel → TR → BO → ...

### 第38-39章 — MTR Tops & Bottoms
- MTR Top/Bottom: 长时间趋势后的反转形态，通常含楔形或双顶/底
- 关键规则: 反转需要 **跟进确认 (follow-through)**，单根K线反转不可靠

### 第40章 — 通道内部交易
- 窄通道只顺趋势方向交易（pullback entries）
- 宽通道可以高抛低吸（mean reversion）
- 通道宽度测量：用 ATR 和通道线的斜率判断

### 第41章 — 盘整区交易
- 80%的突破会失败 → 逆突破交易更可靠
- 双顶/双底/楔形是盘整区内最高质量信号

### 第42章 — 止损与止盈
- 最小盈亏比 >= 1:2，止损放在信号K线对面极值 +1 tick
- 强趋势中至少让一部分仓位奔跑

### 第43章 — 高潮与衰竭
- 卖出高潮：窄通道 + >=4根连续强牛K线 + ATR放大
- 买入高潮：窄通道 + >=4根连续强熊K线 + ATR放大
- 高潮后不追，等待反转信号+跟进确认

### 第44章 — 交易紧窄空头通道 (Trading Tight Bear Channels)
- **核心原则：** 紧窄通道只做空；不确定时假设是紧窄通道
- **HTF确认：** 5分钟紧窄通道 = 更高时间框架的突破
- **进场：** 回调到50%阻力位做空、弱买入信号上方做空
- **止损：** 初始=空头波段高点+1tick；Actual Risk=回调高点+1tick；强突破后追踪
- **止盈：** 最小1x Actual Risk；分批(1x/2x)；最佳="2个以上支撑理由"位
- **多头禁忌：** 紧窄空头通道中永远不要用止损单做多
- **趋势结束：** ~20根K线后警惕TR；三角形=Final Flag；最强阴线=Exhaustion Gap
- **概率：** 趋势交易~60%；PB概率<BO但更易交易
- **Bear Flag vs 反转：** >10根K线才考虑"无尽回调"

### 第45章 — 交易宽幅多头通道 (Trading Broad Bull Channels)
- **核心：** 宽幅通道≈盘整区（90%的K线行为相同），可双向交易
- **50%回调：** 黄金入场点，Limit Order，Risk=Reward(1:1)，胜率~60%
- **HTF视角：** 5分钟宽幅通道 = 60min/日线的紧窄通道
- **每个TR都是多头旗形：** "Every TR in bull trend is a Bull Flag"
- **逆势做空：** 通道上轨做空（scalp）；止损=2×最大突破幅度
- **趋势结束：** Lower Lows=多头结束；Lower Highs=空头通道确认
- **突破概率：** 通道上方牛突破25%成功/75%失败（5根K线内反转）
- **2nd Leg Trap：** TR内第二腿下跌通常是陷阱

### 第46章 — 交易宽幅空头通道 (Trading Broad Bear Channels)
- **核心：** 对称于宽幅多头通道，做空波段/scalp，做多scalp
- **3次下推规则：** 通常需要3 pushes down才结束 → Wedge Bottom → 买入反转
- **日内交易：** 每日单独交易，不视为多日通道的一部分
- **TR内概率≈50%**，趋势中高概率setup在TR中降到~50%

### 第47章 — 盘整区内交易 (Trading in Trading Ranges)
- **核心：** TR内概率≈50%，80%突破失败
- **BLSHS策略：** Buy Low, Sell High, Scalp — 底部1/3买入，顶部1/3卖出
- **深回调：** "TR has deep PBs" — 止损太远，risk/reward差
- **入场：** Stop Orders优先；无好stop entry时在follow-through bar收盘进场
- **耐心：** "Patiently wait for pattern and good signal bar"

### 第48章 — 交易开盘 (Trading the Open)
- **核心：** 开盘突破第一18根K线范围(BOM)
- **前日高低点：** Failed BO → 2nd entry高概率
- **昨日卖出高潮后：** 50%继续抛售1-2h，75%进入2h横盘到上涨，25%早期V形反转

### 第49章 — 波段交易实例 (Swing Trading Examples)
- **双时间框架：** HTF判断方向，LTF找入场
- **趋势中swing part或all，TR中只scalp**

### 第50章 — 剥头皮 (Scalping)
- **新手避免：** "Beginners should avoid scalping"
- **Emini最小scalp：** 1 point
- **TR中scalp是主要策略（BLSHS）**

### 第51章 — 因错误而亏损 (Losing Because of Mistakes)
- **不忘目标：** "Never Lose Sight of Goal: Make Money"
- **交易者方程：** Risk + Reward + Probability — 三者协作才能盈利
- **避免风险不够：** "Avoiding risk is not enough"

### 第52章 — 好交易变坏时亏损 (Losing When Good Trade Goes Bad)
- **强突破：** 1st PB will be bought → 不等回调直接买在BO bar或follow-through收盘
- **强反转提前出场：** "Exit Early, before Stop Is Hit"
- **反转信号：** Wedge Top + HH MTR + 大阴线收在低点
- **出场触发：** 第2/3/4根连续大阴线收盘时出场

---

## 量化规则参考

完整规则表见：`references/al-brooks-price-action-rules.md`

包含：市场状态机、强K线检测、各状态交易规则、止损止盈、高潮检测、何时不交易、10条核心原则、概率体系、Trader's Equation。

## 学习工作流

### 已验证的最佳实践

```bash
# 1. 找到章节页码范围（通过End of Video标记）
python3 -c "
import pymupdf
doc = pymupdf.open('path/to/pdf.pdf')
for i in range(doc.page_count):
    text = doc[i].get_text()
    if 'End of Video' in text:
        for l in text.split('\n'):
            if 'End of Video' in l.strip():
                print(f'  Page {i}: {l.strip()}')
                break
"

# 2. 渲染目标章节为PNG（120 DPI足够）
python3 -c "
import pymupdf, os
doc = pymupdf.open('path/to/pdf.pdf')
outdir = '/tmp/chXX_pages'
os.makedirs(outdir, exist_ok=True)
for i in range(START, END):
    page = doc[i]
    pix = page.get_pixmap(dpi=120)
    pix.save(f'{outdir}/page_{i:04d}.png')
print(f'Rendered {END-START} pages')
"

# 3. 用 vision_analyze 分批阅读
# - 优先看：标题页(Video XXA)、Main Points目录页、图表分析页、Review总结页
# - 每批4-8张，提取量化规则、进场条件、止损止盈、概率数据
# - 每章规则追加到 references/al-brooks-price-action-rules.md
```

### 关键经验
- **DPI 120足够**，文字清晰可读且渲染更快
- **每批4-8张 vision_analyze** 效果最佳
- **关键页面类型：** 标题页、Main Points、图表分析、Review总结
- **PDF分布：** part1 (Ch1-36) 包含到Video 45E；part2 (Ch37-52) 从Video 46A开始

---

## PDF 文件位置

```
pdf/htt-pa/
├── HTT_PA_part1_Ch1-36.pdf    ← 66MB (page 1-700)
└── HTT_PA_part2_Ch37-52.pdf   ← 64MB (page 701-1375)
```
