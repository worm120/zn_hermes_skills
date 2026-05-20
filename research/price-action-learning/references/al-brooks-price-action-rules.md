# Al Brooks Price Action — Quantifiable Rules

Extracted from HTT PA Course (Ch37-52) via vision_analyze (pymupdf → PNG rendering).

## Market State Machine

```
Enter → detect channel type → execute regime-specific rules → re-evaluate every N bars
```

### Channel Detection (N=20 bars)
| Type | Slope | EMA crossing | Strong bar ratio | Height | Pullbacks |
|------|-------|-------------|-----------------|--------|-----------|
| Tight Bull | >0.3\*ATR/N | ≥70% above | SBull/SBear ≥1.8 | ≤2.5\*ATR | ≤3, max depth ≤0.4\*height |
| Tight Bear | <0.3\*ATR/N | ≥70% below | SBear/SBull ≥1.8 | ≤2.5\*ATR | ≤3, max depth ≤0.4\*height |
| Broad Bull | >0 | Mixed | SBull > SBear | >2.5\*ATR | ≥3, ≥1 deep ≥40% |
| Broad Bear | <0 | Mixed | SBear > SBull | >2.5\*ATR | ≥3, ≥1 deep ≥40% |
| TR (Trading Range) | ~0 | Frequent cross | Balanced | ≥2\*ATR | ≥2 failed BOs each side |

## Strong Bar Detection

**Strong Bull:** `C > O AND Body ≥ 50%×Range AND C ≥ H - 0.2×Range`
**Strong Bear:** `C < O AND Body ≥ 50%×Range AND C ≤ L + 0.2×Range`

## Regime-Specific Rules

### Tight Channels (Bull/Bear)
- **Only trade with trend**. Pullback entries only.
- Buy pullbacks in Tight Bull: retrace 0.2-0.5 of prior leg or 0.3-1.0\*ATR.
- Sell rallies in Tight Bear: retrace 0.2-0.5 of prior leg or 0.3-1.0\*ATR.
- First reversal attempt usually fails — treat as pullback, not trend change.
- **Stop**: signal bar opposite extreme +1 tick, or swing low/high +1-2 ticks.
- **Target**: prior extreme, or measured move = flag height.

### Broad Channels (Bull/Bear)
- **Buy low, sell high** — mean reversion within the channel.
- Buy zone: lower channel band ±0.3\*sigma.
- Sell zone: upper channel band ±0.3\*sigma.
- 50% retrace of prior leg is a high-probability entry.
- Many reversals are channel-internal swings, not trend changes.
- **Stop**: structure extreme +1-2 ticks.
- **Target**: channel midline first, then opposite band.

### Trading Range (TR)
- **Buy low, sell high, scalp**. 80% of breakouts fail.
- Lower half → look for buys. Upper half → look for sells.
- Fade breakouts (failed BO): if price pops above range then closes back inside +1-3 bars, reverse.
- 80% rule: if price crosses midline with momentum, ~80% chance to test opposite side.
- 2-leg setups (double tops/bottoms, wedges) are higher quality than 1-bar signals.
- **Stop**: range boundary +1-2 ticks. Tight ranges (TTR): reduce position, don't tighten stop.
- **Target**: range midline first, then opposite boundary.

### Entry Types
1. **Stop entry**: `buy_stop = signal_bar.high + 1tick`; `sell_stop = signal_bar.low - 1tick`
2. **Limit entry** (advanced): near TR boundaries or after climax
3. **Close entry** (strong trend only): buy/sell at market on strong close

### Stop Loss Rules
| Scenario | Stop placement |
|----------|---------------|
| Pullback entry | Pullback extreme +1 tick |
| Signal bar entry | Signal bar opposite extreme +1 tick |
| Structure entry (wedge/DB/DT) | Structure extreme +1-2 ticks |
| Failed BO fade | Failed breakout extreme |

### Take Profit Rules
- Minimum: target >= 1R (R = |entry - stop|)
- Standard first target: **2R** (Brooks: "always good, rarely best")
- Measured move: `target = breakout ± flag_height`
- In TR: target midline first, then opposite boundary
- Always swing at least part of position in strong trend
- Scale out: take 50% at first target, trail rest

### Climax Detection
| Signal | Condition |
|--------|-----------|
| Sell Climax | Tight Bull + ≥4 consec strong bull bars + ATR > SMA(20)×1.5 |
| Buy Climax | Tight Bear + ≥4 consec strong bear bars + ATR > SMA(20)×1.5 |

After climax: don't chase, wait for reversal signal + follow-through.

## When to Skip (Ch51-52)
- No pre-defined stop → don't enter
- Reward < Risk → don't enter
- Signal comes from 1-2 bars only, ignoring HTF context → don't enter
- First signal in strong trend failed → wait for 2nd signal
- Deep pullback (>50% of leg) → treat as TR, not continuation
- Premise changed (no follow-through in 2-3 bars) → scalp out or exit

---

## 第44章 — Trading Tight Bear Channels (交易紧窄空头通道)

### 核心概念
紧窄空头通道（Tight Bear Channel）是一种强烈的下行趋势形态，价格在一个狭窄的向下倾斜的通道内运行。本章详细讲解如何在这种形态下交易。

### 紧窄通道 vs 宽通道对比

| 特征 | 紧窄空头通道 (Tight Bear) | 宽空头通道 (Broad Bear) |
|------|--------------------------|------------------------|
| 通道宽度 | 窄，价格紧密排列 | 宽，有明显的上下波动 |
| 回调深度 | 浅，通常1-3根K线 | 深，可达40%+ |
| 交易方向 | **只做空** | 可做空（波段/ scalp），也可做多（scalp） |
| 多头强度 | 极弱 |  reasonably strong |
| 交易性质 | 单向交易 | 双向交易 |

### 紧窄通道量化规则

| 规则名称 | 条件/公式 | 操作 | 止损 | 目标 | 备注 |
|---------|----------|------|------|------|------|
| 紧窄通道默认假设 | 如果不是明显宽通道 → 假设是紧窄通道 | 只做空 | 见下方 | 见下方 | 保守原则 |
| 紧窄通道只做空 | 通道内所有交易 | Sell only | 信号K线高点+1tick | 前低或测量目标 | 不做多 |
| 更高时间框架确认 | 5分钟紧窄通道 = 更高时间框架(15/30/60/120min)的突破 | 按突破交易，只做空 | 突破K线高点+1tick | 突破测量目标 | HTF视角确认强度 |
| 微通道规则 | 所有K线都是阴线实体 | 只做空 | - | - | 最强空头信号 |

### 做空进场规则

| 进场方式 | 条件 | 说明 |
|---------|------|------|
| 回调到阻力位做空 | 50%回调位或通道上轨 | "Sell PB to resistance, like 50% PB" |
| 弱买入信号上方做空 | K线为阴线实体（bear body） | "Sell above bar, especially if weak buy setup" |
| 赌多头失败 | 预期多头会平仓 | "Bet bulls will fail and have to sell out of longs" |
| 分批建仓 | 反向移动1-2点时加仓 | "Scale in 1-2 pts higher" |

### 止损规则

| 场景 | 止损位置 |
|------|---------|
| 初始止损 | 空头波段或突破高点上方1tick |
| 实际风险(Actual Risk) | 回调(PB)高点上方1tick |
| 追踪止损 | 每个新的强空头突破后，将止损移至该突破K线高点上方 |
| 不确定突破强度 | 收紧止损或使用前止损位 |
| 同一波段内 | 无论在哪里进场，使用相同止损 |

### 止盈规则

| 规则 | 说明 |
|------|------|
| 最小目标 | 1x Actual Risk（实际风险的1倍） |
| 分批止盈 | 在1x或2x风险位平仓部分，剩余仓位swing |
| 最佳目标 | 持有到"有2个或以上支撑理由"的价格位 |
| 最终出场 | 限价单在目标位出场，或用止损追踪出场 |
| 紧窄通道不做最小止盈 | "Minimum Profit: Rarely Is Best Choice" — 最小利润很少是最佳选择 |

### 多头在紧窄通道中的困境

- **不要在紧窄空头通道中用止损单做多** — "Never buy with stop in Tight Bear Channel"
- 进场位往往已经高于目标位（通道很窄）
- 回调幅度太小，不够scalp利润
- 多头需要完美 timing 才能赚钱，"Being human is more likely than being perfect"
- 多头最终会"stop trying"，这通常导致通道向下突破

### 趋势结束信号

| 信号 | 条件 |
|------|------|
| 趋势持续时间 | 约20根K线后，警惕演变为TR |
| 最终旗形 | 趋势后期出现三角形 = 可能的Final Flag |
| 动量衰竭 | 三角形内大量十字星(dojis) = 空头减弱 |
| 耗尽缺口 | 20+根K线后出现最强阴线 = 可能的Exhaustion Gap |
| 强多头反转 | Final Flag后出现强牛反转 = Always In Long |
| 通道突破 | 突破紧窄通道上方 = 趋势可能结束 |

### Bear Flag vs 反转判断

- 空头趋势中的上涨通常是**回调(Bear Flag)**，不是反转
- 回调常表现为紧窄多头通道或紧窄盘整区
- **10根K线规则**：回调超过10根K线，交易者开始怀疑是否为"无尽回调"
- 反转更可能的条件：
  - 之前是卖出高潮(Sell Climax)
  - 抛物线楔形底部(Parabolic Wedge Bottom)
  - 3-5根连续强牛K线
- 但即使有反转信号，**概率仍然偏向Bear Flag**，除非出现强牛突破+跟进确认

### 概率与期望值

- 紧窄通道交易的胜率约**60%** — "60% is as good as trading gets so TRADE!!"
- 回调(PB)交易的概率低于突破(BO)，但时间压力更小，更容易交易
- PB和BO的风险相同（止损位相同），但PB的回报通常更小（趋势更弱）
- 趋势中使用正确止损时，达到Actual Risk回报的概率为60%

### 关键原则

1. **如果不确定是否是宽通道 → 假设是紧窄通道**（保守原则）
2. **紧窄通道按突破交易**（它在更高时间框架上就是突破）
3. **第一次反转通常是小幅的**（"1st reversal usually minor"）
4. **伟大的交易者很少反转**（"Most Great Traders: Rarely Reverse"）
5. **所有趋势最终都会结束**（"All Trends: Eventually End"）
6. **按通道交易直到不再是通道**（"Trade it like a channel until no longer channel"）

### 何时不做多

- 紧窄空头通道中不要用止损单做多
- 回调深度不足以提供有意义的利润
- 大多数回调仅持续1-3根K线
- 多头需要完美 timing，容错率为零
- 风险回报比不利（进场位可能已高于目标位）

---

## 第45章 — Trading Broad Bull Channels (交易宽幅多头通道)

### 核心概念
宽幅多头通道（Broad Bull Channel）是一种波动较大的上升趋势，价格在较宽的通道内运行，回调深度大。与紧窄通道不同，宽幅通道内可以双向交易。

### 紧窄通道 vs 宽幅通道对比

| 特征 | 紧窄多头通道 (Tight Bull) | 宽幅多头通道 (Broad Bull) |
|------|--------------------------|------------------------|
| 通道宽度 | 窄，价格紧密排列 | 宽，有明显的上下波动 |
| 回调深度 | 浅 | 深，常超过50%，有时100% |
| 交易方向 | **只做多** | 可做多（波段/scalp），也可做空（scalp） |
| 空头强度 | 极弱 | reasonably strong |
| 交易性质 | 单向交易 | 双向交易 |

### 宽幅通道与盘整区的关系

| 规则 | 说明 |
|------|------|
| 宽幅通道≈盘整区 | "Broad Channel and TR: Are Same for 90% of Bars" — 宽幅通道90%的K线表现得像在盘整区内 |
| 视觉驱动行为 | "The more bars look like TR, the more traders trade them like TR" |
| 忽略大趋势 | 当K线看起来像TR时，交易者越来越不关注宽幅多头趋势 |
| 宽幅通道内含TR | "Broad Bull Channels form TRs" — 宽幅通道经常包含盘整区 |
| TR内含突破失败 | "TR often has failed BO below prior HL" |

### 多时间框架视角

| 规则 | 说明 |
|------|------|
| HTF视角 | 5分钟图上的宽幅通道 = 更高时间框架(60min/日线)上的紧窄通道 |
| 持续天数 | 宽幅多头通道通常持续数天，5分钟图上通常2-3天形成 |
| 日内交易者视野 | 日内交易者通常只看1-2天的K线，不关注持续3天以上的宽幅通道 |
| 当日模式优先 | "If trading 5 min chart, trade today based on patterns created today or that started yesterday" |

### 做多进场规则

| 进场方式 | 条件 | 订单类型 | 备注 |
|---------|------|---------|------|
| 回调买入 | 回调到通道下轨或50%位置 | Limit Order | "Buy PBs" |
| 50%回调 | 前一波段的50%回撤位 | Limit Order | 此时Risk=Reward，胜率~60% |
| 下一个信号 | 任何多头信号 | - | "Buy again on next signal" |
| HL+失败突破 | Higher Low + 跌破TR失败 | - | 高质量买入信号 |

### 50%回调的数学逻辑（Trader's Equation）

- 在50%回调位，Risk = Reward（1:1）
- 多头趋势中，达到目标的概率约60%，止损概率约40%
- 60%胜率 × 1:1盈亏比 = 正期望值 → "Good Trader's Equation"
- 使用限价单（Limit Order）在50%位置进场

### 做空规则（在宽幅多头通道中）

| 规则 | 说明 |
|------|------|
| 可以做空 | 宽幅多头通道中可以做空，但只做scalp（快进快出） |
| 空头在通道上轨卖出 | "Bears sell for swing or scalp" at top of channel |
| 在前高上方获利了结区做空 | "Profit Taking Zone is above last high" |
| 大牛突破时分批做空 | "Many bears scale in during big bull BOs by selling below bear bars that close near low" |
| 止损计算 | 做空止损 = 2 × 之前最大突破幅度 + 余量（例：最大突破17ticks → 止损35-36ticks） |
| 止盈 | "Take profit above bull bar closing near high" — 出现强牛K线时平仓 |
| 突破失败时退出 | "Failure to get below BO point" — 无法跌破突破点说明多头仍强 |

### 止损与止盈

| 场景 | 规则 |
|------|------|
| 做多止损 | 放在回调K线低点下方 |
| 做空止损（逆势） | 2 × 之前最大突破(Biggest Prior BO)幅度 |
| 止盈目标 | 在或接近前高时止盈（"Take profit at or near new high"） |
| 分批止盈 | 至少2x Actual Risk 或 1-2x最小scalp幅度（Emini最小1点） |
| 反转时止盈 | 出现下跌反转时止盈，尤其是有弱卖出信号时 |
| 阻力位止盈 | "Take profit at resistance" |
| 可能TR时 | 因为可能是盘整区，scalp出局是可以接受的 |

### 关键模式与形态

| 形态 | 含义 | 操作 |
|------|------|------|
| 2nd Leg Trap | TR和宽幅通道内的第二腿下跌通常是陷阱 | 做多 |
| Minor New Lows | 跌破次要HL是常见现象，不意味着趋势反转 | 保持多头思维 |
| 趋势定义规则 | 只要空头波段保持在多头趋势底部上方，仍属于宽幅多头通道 | - |
| Sell Vacuum | 快速下跌测试支撑位后反转 = 卖出真空陷阱 | 做多 |
| Major Low | 导致强劲反弹和新高的低点 = 主要低点 | 买入反转 |

### 趋势结束信号

| 信号 | 条件 |
|------|------|
|  Lower Lows | 一旦开始形成Lower Lows → 不再是多头趋势 → 平仓多单，停止买入 |
| Lower Highs | 一旦开始形成Lower Highs → 确认为空头通道 |
| 通道不会永续 | "Channels do not last forever" |
| 突破成功率低 | 宽幅多头通道上方的牛突破只有25%成功率 |
| 75%概率演变为 | 75%概率演变为空头趋势或大型TR |
| 牛通道=空头旗形 | "Bull channel is Bear Flag" |
| 突破后反转 | 牛突破有75%概率在5根K线内反转回通道内 |

### 宽幅通道突破规则

| 规则 | 数值 | 说明 |
|------|------|------|
| 突破失败率 | 75% | 宽幅多头通道上方的牛突破有75%概率在5根K线内反转 |
| 突破成功率 | 25% | 只有25%的突破会成功 |
| 成功后的走势 | - | 成功后通常会形成新的多头通道和向上测量目标(MM up) |
| 交易方式 | - | "Trade it like any other BO" — 像其他突破一样交易 |
| 持仓策略 | - | "Buy for any reason and hold for swing up" — 以任何理由买入并持有做波段 |

### 每个TR都是多头旗形

- "Every TR in bull trend is a Bull Flag or contains a Bull Flag"
- 多头趋势中的每个盘整区都是多头旗形或包含多头旗形
- TR处于突破模式（"TR is BO mode"）
- 在多头趋势中，交易者预期下跌会失败，多头趋势会恢复

### 概率与期望值

- 50%回调位做多：60%胜率，Risk=Reward → 正期望值
- 宽幅通道突破：25%成功，75%失败 → 但成功后回报大，仍值得交易
- 60% of Trending TRs reverse and test into early TR（60%的趋势中TR会反转测试早期TR）

### 关键原则

1. **宽幅通道≈盘整区**：90%的K线表现相同，按TR方式交易（高抛低吸）
2. **双向交易**：宽幅通道中可以做多（波段/scalp）也可以做空（scalp）
3. **50%回调是黄金入场点**：Limit order进场，Risk=Reward，胜率60%
4. **每个TR都是多头旗形**：多头趋势中的盘整区是继续上涨的蓄力
5. **通道不会永续**：Lower Lows出现=多头结束；Lower Highs出现=空头通道确认
6. **2nd Leg Trap**：TR内的第二腿下跌通常是陷阱
7. **Minor New Lows是常态**：跌破次要HL不意味着趋势反转
8. **大牛突破时警惕**：分批做空者在熊K线低点下方做空
9. **逆势做空止损** = 2×最大突破幅度
10. **日内交易者只看1-2天**：不要被多日通道影响当日交易决策

---

## 第46章 — Trading Broad Bear Channels (交易宽幅空头通道)

### 核心概念
宽幅空头通道（Broad Bear Channel）的对称于第45章的宽幅多头通道。宽幅通道内波动大，可以双向交易。

### 关键规则

| 规则 | 说明 |
|------|------|
| 宽幅空头通道内含多头趋势和TR | "Broad Bear Channel: Contains Bull Trends, and TRs" |
| 日内交易者只看当日 | "Most Trade Each Day by Itself: Not Part of 9 Day Channel" |
| 需要3次下推 | "Usually need 3 pushes down to conclude Broad Bear Channel" |
| 楔形底部 | 3次下推后形成Wedge Bottom → 买入反转 |
| 15分钟图视角 | 可当TR交易(BLSHS)，或当宽幅通道交易(隔夜做空+宽止损) |
| TR内概率≈50% | 趋势中的高概率setup在TR中降到~50% |
| 每日交易 | "When day trading 5 min chart, trade each day as develops" |
| 宽幅通道包含TR | "Most Broad Channels contain one or more TRs" |
| 失败突破 | TR内经常有Failed BO above prior LH |
| 每根K线提供新信息 | "Never Certain: But Each Bar Gives New Information" |
| 持续判断概率 | 交易者不断判断下一根K线向上/向下的概率是否60% |
| 做空入场 | Bears sell below bear bar that closes near low |
| 做空追单 | Bears sell close of strong bear BO and follow-through |
| 概率估算 | "60% chance of at least 1-3 more bars down to bottom of TR" |
| 第二腿下跌 | 2nd Leg Down likely |

### 宽幅空头通道与宽幅多头通道对比

- 宽幅多头通道：做多波段/scalp，做空scalp
- 宽幅空头通道：做空波段/scalp，做多scalp
- 两者都≈盘整区（90%的K线行为相同）
- 都通常持续数天
- 都在HTF上表现为紧窄通道

---

## 第47章 — Trading in Trading Ranges (盘整区内交易)

### 核心概念
盘整区（Trading Range / TR）是价格在一个范围内震荡，无明确方向。80%的突破会失败。

### 关键规则

| 规则 | 说明 |
|------|------|
| 概率≈50% | "Probabilities Mostly around 50%: Bad Setups Often Work" |
| 趋势中高概率setup在TR中降为50% | "High probability setups in trends have about 50% probability in TRs" |
| 平衡市场中概率约50% | "Probabilities mostly around 50% in balanced markets" |
| BLSHS策略 | **B**uy **L**ow, **S**ell **H**igh, **S**calp — 在底部1/3买入，顶部1/3卖出 |
| 大多数突破失败 | "Most BO fail so probability is low when buying near top or selling near bottom" |
| TR有深回调 | "TR has deep PBs" |
| 止损太远 | Stop is far (opposite end of TR) so risk is big → Bad risk/reward |
| 上下三分之一 | "Bulls and Bears: Some Use Upper and Lower Third" |
| 失败反转 | "Failed reversal of BO of yesterday's range" |
| 昨日高低点突破失败 | "Failed BO of yesterday's H or L" |
| 入场方式 | Stop Orders（或Enter on Close）+ Swing Trade |
| 耐心 | "Patiently wait for pattern and good signal bar" |
| 做空规则 | Sell below bear bar that closes near low and is in a sell setup |
| 做多规则 | Buy above bull bar that closes near high and is in a buy setup |
| 强突破时无好stop entry | 在follow-through bar的收盘价进场 |
| ~10%的日子 | 没有好的stop order entry，等待强突破 |
| 失败突破反做 | Bear BO but no follow-through → bulls buy the close |

### 概率体系总结

| 市场环境 | 高概率setup胜率 | 低概率setup胜率 |
|---------|---------------|---------------|
| 强趋势 | 60-70%+ | 40-50% |
| 宽幅通道 | ~55% | ~45% |
| 盘整区(TR) | ~50% | ~50% |

---

## 第48章 — Trading the Open (交易开盘)

### 核心概念
开盘时段的交易策略，包括突破第一根18根K线范围、前日高低点的突破与失败。

### 关键规则

| 规则 | 说明 |
|------|------|
| 开盘突破模式 | Breakout Mode (BOM) |
| 第一18根K线范围突破 | "BO of 1st 18 Bar Range" |
| 前日高低点突破失败 | "Failed BO of Yesterday's H or L" — 二次信号(2nd entry)做空/做多概率更高 |
| 突破范围的反转失败 | "Failed reversal of BO of yesterday's range" |
| 隔夜反转 | "ORV: 2nd Reversal up from below Yesterday's Low" |
| 开盘反转 | "BOM on Open: Buy BO above Reversal down for MM Up" |
| 前18根K线常横盘 | "BOM of 1st 18 Bars: Often Goes Sideways" |
| 开盘后交易者行为 | 在15-25根K线之间，交易者会在低点附近买入反转，在高点附近卖出反转 |

### 昨日卖出高潮后的次日概率

| 情景 | 概率 | 说明 |
|------|------|------|
| 继续抛售1-2小时 | 50% | 卖出高潮后不一定立即反转 |
| 2小时横盘到上涨 | 75% | 可能在开盘时或1-2小时抛售后发生 |
| 早期反转 | 25% | V形反转概率较低 |

---

## 第49章 — Swing Trading Examples (波段交易实例)

### 核心概念
通过实例展示波段交易（Swing Trading）的具体应用。

### 关键规则

| 规则 | 说明 |
|------|------|
| 波段vs scalping | 波段持有更长时间，scalp快进快出 |
| 双时间框架 | 使用两个时间框架分析（HTF判断方向，LTF找入场） |
| 趋势中波段 | 在强趋势中swing part或all仓位 |
| TR中波段 | 在盘整区中只scalp，不swing |

---

## 第50章 — Scalping (剥头皮)

### 核心概念
快速进出市场获取小利润的交易方式。

### 关键规则

| 规则 | 说明 |
|------|------|
| 新手避免scalping | "Beginners should avoid scalping" |
| 双时间框架 | "Two time frames" — 用HTF确认方向，LTF找入场 |
| Emini最小scalp | 1 point |
| TR中scalp | 在盘整区中scalp是主要策略（BLSHS） |
| 紧窄通道不适合scalp | 回调太小，不够利润 |
| 宽幅通道可scalp | 波动足够大 |

---

## 第51章 — Losing Because of Mistakes (因错误而亏损)

### 核心概念
交易者常犯的错误和如何避免。心理与数学的结合。

### 关键规则

| 规则 | 说明 |
|------|------|
| 不忘目标 | "Never Lose Sight of Goal: Make Money" |
| 交易者方程 | Trader's Equation = Risk（止损距离）+ Reward（目标距离）+ Probability（止损前获利的概率） |
| 三要素协作 | "All 3 have to work together to create profit" |
| 避免风险不够 | "Avoiding risk is not enough" |
| 新手恐惧 | 新手把资金视为"新生命"，恐惧=早期死亡 |
| 新手只关注风险 | "Beginner focuses entirely on risk of losing money" |
| 概率思维 | 应该关注赚钱的概率，而不只是亏钱的风险 |

---

## 第52章 — Losing When Good Trade Goes Bad (好交易变坏时亏损)

### 核心概念
如何管理已经开始变坏的好交易。风险管理的高级技巧。

### 关键规则

| 规则 | 说明 |
|------|------|
| 强突破首回调必被买入 | "Strong BO: 1st PB Will Be Bought" |
| 强突破特征 | DB after DT + 2根大牛K线收在高点 + BO bar收在前高上方 + follow-through无阴线实体 |
| 强突破入场 | 不等回调，直接买在BO bar收盘或follow-through bar |
| 止损 | 放在突破形态最低点下方 |
| 失望的跟随 | "Disappointing Follow-Through: Scale In to Exit without Loss" |
| 分批出场 | 快速思考的交易者在反弹时加仓(scale in higher)以改善均价 |
| 出场策略 | 买回两个仓位：第一个breakeven，第二个scalper's profit |
| 强反转提前出场 | "Strong Reversal: Exit Early, before Stop Is Hit" |
| 反转信号 | Wedge Top + HH MTR + 大阴线收在低点 |
| 多头出场触发 | 在第2/3/4根连续大阴线收盘时出场 |
| 更看跌信号 | 连续阴线收在低点 |
| 中点规则 | 连续阴线收在前一根K线中点以下 = 趋势已反转 |

---

## 课程整体总结

### 三大市场状态完整框架

```
市场循环: BO → Channel → TR → BO → ...

BO (突破): 强动量，按突破交易
  ├─ 成功 → 新趋势/通道
  └─ 80%失败 → 返回TR

Channel (通道):
  ├─ Tight (紧窄): 只做趋势方向，pullback entry
  │   ├─ Tight Bull: Only buy
  │   └─ Tight Bear: Only sell
  └─ Broad (宽幅): 双向交易，BLSHS或swing
      ├─ Broad Bull: Buy for swings/scalps, sell for scalps
      └─ Broad Bear: Sell for swings/scalps, buy for scalps

TR (盘整区):
  ├─ 80%突破失败 → 逆突破交易
  ├─ Buy Low, Sell High, Scalp (BLSHS)
  ├─ 概率≈50%
  └─ 每个TR内的突破都可能是假突破
```

### 核心概率体系

| 场景 | 胜率 | 策略 |
|------|------|------|
| 紧窄通道顺趋势 | 60-70%+ | Swing |
| 宽幅通道顺趋势 | ~55-60% | Swing/Scalp |
| 宽幅通道逆趋势 | ~45% | Scalp only |
| 盘整区内 | ~50% | BLSHS |
| 突破成功 | 20-25% | 但成功后回报大 |
| 突破失败 | 75-80% | 逆突破交易更可靠 |
| 50%回调位做多(多头趋势) | ~60% | Limit order |
| 失败突破后二次信号 | >60% | 高质量入场 |

### 交易者方程 (Trader's Equation)

```
Profit = Risk × Reward × Probability

Risk = |entry - stop|
Reward = |target - entry|
Probability = odds of reaching target before stop

Positive Expectancy when: Probability × Reward > (1 - Probability) × Risk
```

### 10条核心交易原则

1. **永远知道市场在什么状态**（紧窄/宽幅/TR）→ 执行对应策略
2. **紧窄通道只做趋势方向**
3. **宽幅通道可双向交易但顺趋势优先**
4. **TR内80%突破失败 → 逆突破交易**
5. **不确定时假设是紧窄通道**（保守原则）
6. **HTF确认强度**（5分钟紧窄=HTF突破）
7. **50%回调是黄金入场点**（1:1风险回报，60%胜率）
8. **每次交易前明确：止损位、目标位、胜率估计**
9. **强反转时提前出场，不等止损被触发**
10. **分批止盈：部分scalp，部分swing**
