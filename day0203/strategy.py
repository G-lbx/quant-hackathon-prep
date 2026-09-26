import numpy as np

def moving_average_strategy(df, short_window, long_window):
    df["short_ma"] = df["price"].rolling(short_window).mean()
    df["long_ma"] = df["price"].rolling(long_window).mean()
    df["signal"] = np.where(df["short_ma"] > df["long_ma"], 1, np.where(df["short_ma"] < df["long_ma"], -1, 0))

    return df


def momentum_strategy(df, window=20):
    df = df.copy()

    df["momentum"] = (
        df["price"] / df["price"].shift(window) - 1
    )

    df["signal"] = 0

    df.loc[df["momentum"] > 0, "signal"] = 1
    df.loc[df["momentum"] < 0, "signal"] = -1

    return df

def mean_reversion_strategy(df, window=20, threshold=1.5):
    df = df.copy()
    df["rolling_mean"] = df["price"].rolling(window).mean()
    df["rolling_std"] = df["price"].rolling(window).std()
    df["z_score"] = (df["price"] - df["rolling_mean"]) / df["rolling_std"]
    df["signal"] = 0
    df.loc[df["z_score"] > threshold, "signal"] = -1
    df.loc[df["z_score"] < -threshold, "signal"] = 1
    return df

def breakout_strategy(df, window = 20):
    df = df.copy()
    df["rolling_high"] = df["price"].rolling(window).max().shift(1)
    df["rolling_low"] = df["price"].rolling(window).min().shift(1)
    df["signal"] = 0
    df.loc[df["price"] > df["rolling_high"], "signal"] = 1
    df.loc[df["price"] < df["rolling_low"], "signal"] = -1
    return df