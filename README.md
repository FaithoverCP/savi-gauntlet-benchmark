# SAVI Gauntlet (repeatability check)

> **Correction (2026-10-28).** Earlier versions listed the expected result as `385.05`. The expression evaluates to **`386.7`** under standard operator precedence: (391 + 47) / 20 × 13 + 202 − 100 = 21.9 × 13 + 102. The scorer is corrected, and any result scored against `385.05` is withdrawn. Earlier descriptions of this repository as showing that the SAVI Protocol makes a model deterministic were not supported and have been removed.

## What it does
`savi_gauntlet_duel.py` sends one arithmetic prompt to Google's Gemini (`gemini-2.0-flash-exp`) five times with greedy decoding (temperature 0, top_k 1, top_p 1, at most 50 output tokens). It reports:
- whether the first answer equals 386.7 (within 0.01);
- whether the five outputs are character-for-character identical;
- response times.

## What it does not show
The prompt contains no SAVI instructions, routing or DSHM logic. Repeatable output here comes from the greedy-decoding settings, which any Gemini caller can set, and there is no comparison run. The result therefore says nothing about what the SAVI Protocol contributes.

## Run it
```bash
pip install -r requirements.txt
export GOOGLE_AI_API_KEY=your_key_here   # or put it in a .env file
python savi_gauntlet_duel.py
```

Expression: `((17 * 23) + (89 - 42)) / (13 + 7) * (31 - 18) + (101 * 2) - (67 + 33)` — expected answer `386.7`.

## License
MIT. See [LICENSE](LICENSE).
