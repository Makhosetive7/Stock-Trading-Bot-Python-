import os
import httpx
import pandas as pd
from dotenv import load_dotenv

load_dotenv()


def get_stock_data(symbol: str): 
    API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=15min&apikey={API_KEY}&outputsize=compact"
    
    response = httpx.get(url).json()
    time_series = response.get("Time Series (15min)", {})
    
    
    #convert to dataframe
    df = pd.DataFrame([
         {
            "timestamp": k,
            "open": float(v["1. open"]),
            "high": float(v["2. high"]),
            "low": float(v["3. low"]),
            "close": float(v["4. close"]),
            "volume": int(v["5. volume"])
        }
         for k, v in time_series.items()
    ])
    
    df.sort_values("timestamp", inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df