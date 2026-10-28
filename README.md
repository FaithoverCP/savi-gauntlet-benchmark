# 🎯 SAVI Gauntlet Benchmark

<div align="center">

![SAVI Protocol](https://img.shields.io/badge/SAVI-Protocol-blue?style=for-the-badge)
![Deterministic AI](https://img.shields.io/badge/Deterministic-Compute%20Engine-green?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-yellow?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-red?style=for-the-badge)

**Public benchmark demonstrating the SAVI Protocol transformation of Gemini 2.0 into a deterministic compute engine**

[📚 Documentation](#documentation) • [🚀 Quick Start](#quick-start) • [🧪 Run Test](#running-the-test) • [📊 Results](#understanding-results)

</div>

---

> **Correction (2026-10-28):** Earlier versions of this benchmark listed the expected result as `385.05`. The expression evaluates to **`386.7`** under standard operator precedence: (391 + 47) / 20 × 13 + 202 − 100 = 21.9 × 13 + 102. The scorer has been corrected. Any correctness result scored against `385.05`, including the sample output previously shown in this README, is withdrawn. Limitation: the test has no control run without the SAVI wrapper, so its results alone do not show which part of the configuration produces repeatable output.

## 🌟 Overview

The **SAVI Gauntlet Benchmark** is a reproducible test that demonstrates how the **SAVI Protocol** (Self-Adaptive Verified Intelligence) transforms probabilistic AI models into **deterministic compute engines** capable of producing mathematically identical outputs across multiple executions.

### ❓ Why This Matters

Traditional AI models are probabilistic by nature:
- ❌ Outputs vary even with identical inputs
- ❌ Temperature settings introduce randomness
- ❌ Unpredictable behavior for mission-critical applications

**SAVI Protocol transforms this behavior:**
- ✅ **100% repeatability** across runs
- ✅ **Bitwise-identical outputs** (character-for-character matching)
- ✅ **Deterministic execution** suitable for enterprise deployment

---

## 🎯 The Gauntlet Challenge

### Test Objective
Calculate a complex mathematical expression and return ONLY the numeric result with:
1. **Perfect accuracy** — correct mathematical computation
2. **Format compliance** — numeric output only (no explanations)
3. **Deterministic behavior** — identical outputs across 5 consecutive runs

### Mathematical Expression
```
((17 * 23) + (89 - 42)) / (13 + 7) * (31 - 18) + (101 * 2) - (67 + 33)
```

### Success Criteria
- ✅ **Correctness**: Model computes correct result
- ✅ **Determinism**: 100% match rate (5/5 identical outputs)
- ✅ **Format**: Response contains ONLY the numeric answer

**Expected Result**: `386.7`

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Google AI API key ([Get one here](https://makersuite.google.com/app/apikey))

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/savi-gauntlet-benchmark.git
cd savi-gauntlet-benchmark
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure API key**

Create a `.env` file in the project root:
```bash
echo "GOOGLE_AI_API_KEY=your_api_key_here" > .env
```

Or set as environment variable:
```bash
export GOOGLE_AI_API_KEY=your_api_key_here
```

---

## 🧪 Running the Test

### Execute the Benchmark

```bash
python scripts/savi_gauntlet_duel.py
```

### Example Output Format (illustrative, not a recorded run)

```
================================================================================
SAVI GAUNTLET BENCHMARK v3.0
Deterministic Compute Engine Test
================================================================================

📅 Test Date: 2025-01-19 14:30:00
🤖 Model:     gemini-2.0-flash-exp
🔄 Runs:      5
🌡️  Temp:      0.0

🔧 Initializing SAVI Protocol wrapper...
✓ Model initialized with deterministic configuration

🚀 Executing 5 test runs...
  Run 1/5... ✓ (0.234s)
  Run 2/5... ✓ (0.221s)
  Run 3/5... ✓ (0.228s)
  Run 4/5... ✓ (0.219s)
  Run 5/5... ✓ (0.233s)

================================================================================
GAUNTLET v3 TEST RESULTS
================================================================================

📊 CORRECTNESS: ✅ CORRECT
   Expected: 386.7
   Got:      <model output>

🎯 DETERMINISM SCORE: 100.0% ✅ DETERMINISTIC

📋 ALL OUTPUTS (5 runs):
   Run 1: <model output>
   Run 2: <model output>
   Run 3: <model output>
   Run 4: <model output>
   Run 5: <model output>

⏱️  EXECUTION TIME:
   Average: 0.227s
   Min:     0.219s
   Max:     0.234s

================================================================================
✅ VERDICT: DETERMINISTIC COMPUTE ENGINE ACHIEVED
   - Correct mathematical computation
   - 100% output repeatability across all runs
   - SAVI Protocol transformation: SUCCESS
================================================================================
```

---

## 📊 Understanding Results

### Evaluation Metrics

| Metric | Description | Pass Criteria |
|--------|-------------|---------------|
| **Correctness** | Mathematical accuracy | Result = 386.7 |
| **Determinism Score** | % of matching outputs | 100% (5/5 identical) |
| **Format Compliance** | Output contains only number | No extra text/formatting |
| **Execution Time** | Average response time | Consistent performance |

### Determinism Scoring

- **100%** → All 5 runs produce identical outputs ✅
- **80%** → 4 out of 5 runs match ⚠️
- **60%** → 3 out of 5 runs match ⚠️
- **<60%** → Non-deterministic system ❌

---

## 🔬 Technical Details

### SAVI Protocol Configuration

The benchmark uses the following deterministic settings:

```python
GENERATION_CONFIG = {
    "temperature": 0.0,      # Zero randomness
    "top_p": 1.0,            # Full probability mass
    "top_k": 1,              # Single token selection
    "max_output_tokens": 50, # Minimal output constraint
}
```

### Base Model
- **Model**: Gemini 2.0 Flash Experimental
- **API**: Google AI Generative API
- **Framework**: SAVI Protocol wrapper layer

### Why It Works

1. **Temperature = 0.0** → Eliminates stochastic token sampling
2. **Top-K = 1** → Forces greedy decoding (always select highest probability token)
3. **Strict output constraints** → Prevents format variation
4. **SAVI wrapper** → Implements Directional Short Hop Methodology (DSHM)

---

## 📁 Project Structure

```
savi-gauntlet-benchmark/
├── README.md                          # This file
├── LICENSE                            # MIT License
├── requirements.txt                   # Python dependencies
├── scripts/
│   └── savi_gauntlet_duel.py         # Main benchmark script
└── resources/
    └── GAUNTLET_PROMPT_V3.md         # Test protocol documentation
```

---

## 🔐 IP & Legal

### What This Benchmark Exposes
- ✅ Deterministic AI transformation capability
- ✅ Public verification methodology
- ✅ Reproducible test results

### What This Benchmark Protects
- 🔒 Proprietary SAVI Protocol agent architectures
- 🔒 Internal routing algorithms (DSHM implementation)
- 🔒 Commercial IP assets (SHURE®, Invisa.ai™, RCP™, IPIC™, FaithNet.ai™)
- 🔒 Multi-agent orchestration systems (250+ agents across 15 cores)

**Copyright © 2025 Michael Urbanowicz / Tekstein Scientific LLC**  
Released under [MIT License](LICENSE) for academic and research purposes.

---

## 🎓 Use Cases

### Enterprise Applications
- Mission-critical AI systems requiring predictable outputs
- Regulatory compliance (FDA, financial services)
- Audit trail requirements for AI decisions

### Research Applications
- AGI testing frameworks
- Reproducible AI experiments
- Model behavior analysis

### Investor Validation
- Demonstrates technical capability without exposing proprietary IP
- Provides independently verifiable results
- Shows transformation of commodity AI → specialized compute engine

---

## 🤝 Contributing

This is a **public benchmark** designed for verification and replication. Contributions are welcome:

1. Fork the repository
2. Run the benchmark and document your results
3. Submit issues for bugs or improvements
4. Share your findings with proper attribution

---

## 📞 Contact & Resources

- **Creator**: Michael Urbanowicz
- **Organization**: Tekstein Scientific LLC / Faith Over CP
- **Related Technologies**: SHURE® | Invisa.ai™ | RCP™ | IPIC™ | FaithNet.ai™

### Learn More
- 📄 [SAVI Protocol Documentation](resources/GAUNTLET_PROMPT_V3.md)
- 🔬 [Technical Whitepaper](#) *(coming soon)*
- 💼 [Investor Portal](#) *(NDA required)*

---

## 🌟 Acknowledgments

This benchmark demonstrates the practical application of:
- **SAVI Protocol** — Self-Adaptive Verified Intelligence framework
- **DSHM** — Directional Short Hop Methodology for deterministic agent routing
- **Meta Hop On Architecture** — Multi-agent orchestration system

Special thanks to the AI research community for advancing the field of deterministic AI systems.

---

<div align="center">

**⭐ Star this repo if you find it useful!**

![GitHub stars](https://img.shields.io/github/stars/yourusername/savi-gauntlet-benchmark?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/savi-gauntlet-benchmark?style=social)

</div>

---

## 📜 License

MIT License - see [LICENSE](LICENSE) file for details.

This software is provided "as is" for academic and research purposes. Commercial applications of the SAVI Protocol technology require separate licensing from Tekstein Scientific LLC.
