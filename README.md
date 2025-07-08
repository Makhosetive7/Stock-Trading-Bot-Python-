# Automated Stock Trading Bot

A rule-based trading bot using Python, FastAPI, and Alpha Vantage API.

## Features
- Real-time price monitoring
- Technical indicator calculations (RSI, MACD)
- Paper trading simulation
- Telegram alert integration

## Tech Stack
- **Backend:** Python + FastAPI
- **Data:** Alpha Vantage API
- **Scheduling:** Celery + Redis
- **Alerts:** Telegram Bot API

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
