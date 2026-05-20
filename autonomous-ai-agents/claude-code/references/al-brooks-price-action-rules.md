# Al Brooks Price Action — Quantifiable Rules

Extracted from HTT PA Course (Ch37-52) via Claude Code multimodal analysis.

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
