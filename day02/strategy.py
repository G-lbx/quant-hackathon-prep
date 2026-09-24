import numpy as np

def moving_average_strategy(df, short_window, long_window):
    df["short_ma"] = df["price"].rolling(short_window).mean()
    df["long_ma"] = df["price"].rolling(long_window).mean()
    df["signal"] = np.where(df["short_ma"] > df["long_ma"], 1, np.where(df["short_ma"] < df["long_ma"], -1, 0))

    return df



    