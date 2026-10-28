# Gauntlet v3 — task and scoring

## Task
Calculate the following expression and return ONLY the numeric result:

```
((17 * 23) + (89 - 42)) / (13 + 7) * (31 - 18) + (101 * 2) - (67 + 33)
```

Expected answer: **386.7** (corrected 2026-10-28; earlier versions said 385.05).

## Scoring
1. **Correct answer:** the first output equals 386.7 within 0.01.
2. **Format:** the response contains only the number.
3. **Repeatability:** across 5 consecutive runs with identical inputs, the share of outputs identical to the first run (100%, 80%, 60%, or less).

## Settings
Gemini `gemini-2.0-flash-exp`, temperature 0, top_p 1, top_k 1, at most 50 output tokens. The prompt contains no SAVI instructions, so this check measures the model under greedy decoding, not the SAVI Protocol.

Copyright © 2025 Michael Urbanowicz / Tekstein Scientific Inc. Released under the MIT License.
