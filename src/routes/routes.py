from fastapi import APIRouter
from ..services.alphaVantage import get_stock_data
from ..bot.indicators import calculate_rsi, calculate_macd
from ..bot.strategy import should_buy, should_sell
from ..bot.visualizer import generate_stock_chart


router = APIRouter()


@router.get("/ping")
def health_check():
    return {"status": "ok"}


@router.get("/chart/{symbol}")
def chart(symbol: str):
    df = get_stock_data(symbol)
    df = calculate_rsi(df)
    df = calculate_macd(df)
    df.dropna(inplace=True)
    return generate_stock_chart(df, symbol)



@router.get("/analyze/{symbol}")
def analyze(symbol: str):
    try:
        df = get_stock_data(symbol)
        df = calculate_rsi(df)
        df = calculate_macd(df)
        df.dropna(inplace=True)

        if df.empty:
            return {"error": "Not enough data to compute indicators. Try another symbol or wait for more intervals."}

        action = "HOLD"
        if should_buy(df):
            action = "BUY"
        elif should_sell(df):
            action = "SELL"

        last = df.iloc[-1]

        return {
            "symbol": symbol.upper(),
            "last_price": round(last["close"], 2),
            "RSI": round(last["RSI"], 2),
            "MACD": round(last["MACD"], 4),
            "Signal": round(last["Signal"], 4),
            "action": action
        }

    except Exception as e:
        return {"error": str(e)}
    
    
    