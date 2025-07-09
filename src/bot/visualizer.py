import matplotlib.pyplot as plt
import io
from fastapi.responses import StreamingResponse
import pandas as pd


def generate_stock_chart(df, symbol):
    fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=True)
    fig.suptitle(f"{symbol} Technical Analysis")

    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Plot close price
    axs[0].plot(df['timestamp'], df['close'], label='Close Price')
    axs[0].legend()
    axs[0].set_ylabel("Price")

    # Plot RSI
    axs[1].plot(df['timestamp'], df['RSI'], color='purple', label='RSI')
    axs[1].axhline(70, color='red', linestyle='--', alpha=0.5)
    axs[1].axhline(30, color='green', linestyle='--', alpha=0.5)
    axs[1].legend()
    axs[1].set_ylabel("RSI")

    # Plot MACD
    axs[2].plot(df['timestamp'], df['MACD'], color='blue', label='MACD')
    axs[2].plot(df['timestamp'], df['Signal'], color='orange', label='Signal')
    axs[2].legend()
    axs[2].set_ylabel("MACD")
    axs[2].set_xlabel("Time")

    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    return StreamingResponse(buf, media_type="image/png")
