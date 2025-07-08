import pandas as pd


def calculate_rsi(df: pd.DataFrame, period: int = 14) -> pd.DataFrame:
    delta = df["close"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    
    
    average_gain = gain.rolling(window=period).mean()
    average_loss = loss.rolling(window=period).mean()
    
    rs = average_gain / average_loss
    df["RSI"] = 100 - (100 / (1 + rs))
    
    return df

def calculate_macd(df: pd.DataFrame) -> pd.DataFrame:
    df["EMA12"] = df["close"].ewm(span=12, adjust=False).mean()
    df["EMA26"] = df["close"].ewm(span=26, adjust=False).mean()
    df["MACD"] = df["EMA12"] - df["EMA26"]
    df["Signal"] = df["MACD"].ewm(span=9, adjust=False).mean()
    
    
    return df
    