# Crypto Economics Simulation Model

[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB.svg)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.26-013243.svg)](https://numpy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A **tokenomics modeling engine** for simulating crypto-economic systems. This repository implements bonding curve mathematics (Bancor formula) and agent-based simulation to analyze token price discovery, supply dynamics, and market depth.

## 🚀 Features

- **Bonding Curves**: Implementation of Linear and Exponential bonding curves.
- **Agent Simulation**: Simulates trader behavior (Buy/Sell) based on price signals.
- **Slippage Calculation**: accurate price impact modeling for large orders.
- **Supply Dynamics**: Tracks total supply, reserve balance, and market cap over time.
- **Data Visualization**: Exports simulation data for analysis.

## 📁 Project Structure

```
crypto-economics-simulation-model/
├── src/
│   ├── bonding_curve.py  # Math logic
│   ├── simulation.py     # Agent loop
│   └── main.py           # CLI Entrypoint
├── requirements.txt
└── Dockerfile
```

## 🛠️ Quick Start

```bash
# Clone
git clone https://github.com/Shivay00001/crypto-economics-simulation-model.git

# Install
pip install -r requirements.txt

# Run Simulation
python src/main.py --steps 100 --curve linear
```

## 📄 License

MIT License
