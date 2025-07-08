import pandas as pd

def should_buy(df: pd.DataFrame) -> bool:
    last = df.iloc[-1]
    return last["RSI"] < 30 and last ["MACD"] > last["Signal"]


def should_sell(df: pd.DataFrame) -> bool:
    last = df.iloc[-1]
    return last["RSI"] > 70 and last["MACD"] < last["Signal"]