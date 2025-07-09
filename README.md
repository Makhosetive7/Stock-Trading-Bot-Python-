# Automated Stock Trading Bot

A Python-based stock analysis bot that uses RSI and MACD indicators to generate actionable BUY/SELL/HOLD signals. Built with **FastAPI**, **Celery**, and **Redis**, this bot fetches real-time stock data.

---

## 🌟 Features

-  Fetch intraday stock data using Alpha Vantage
-  Calculate technical indicators: RSI and MACD
-  Generate BUY/SELL/HOLD signals with strategy logic
-  Scheduled analysis using **Celery Beat**
-  Async task processing with **Celery + Redis**
-  Visualize indicators via chart endpoint (matplotlib)
-  Built with modern async stack (FastAPI + Uvicorn)

---
## Tech Stack

| Tool           | Purpose                        |
|----------------|---------------------------------|
| Python         | Core programming language       |
| FastAPI        | API framework                   |
| Celery         | Background task queue           |
| Redis          | Message broker for Celery       |
| Matplotlib     | Plot stock + indicator charts   |
| Alpha Vantage  | Financial data provider         |

---

## Quick Start
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Add Alpha Vantage API key

# Start bot
celery -A bot worker --loglevel=info
