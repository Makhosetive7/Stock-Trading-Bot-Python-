from ..celery import celery_app
from ..bot.indicators import calculate_macd, calculate_rsi
from ..bot.stategy import should_buy, should_sell
from ..services.alphaVantage import get_stock_data



@celery_app.task
def analyze_stock(symbol: str):
    try:
        df = get_stock_data(symbol)
        df = calculate_rsi(df)
        df = calculate_macd(df)
        df.dropna(inplace=True)
        
        if df.empty:
            print(f"{symbol}: Not enough data")
            return
        
        last = df.iloc[-1]
        
        action = "HOLD"
        if should_buy(df):
            action = "BUY"
        elif should_sell(df):
            action = "SELL"
            
        print(f"{symbol} | Price: {round(last['close'], 2)} | RSI: {round(last['RSI'], 2)} | MACD: {round(last['MACD'], 2)} | Signal: {round(last['Signal'], 2)} | Action: {action}")
           
    except Exception as e: 
        print(f"Error analyzing {symbol}: {str(e)}")