import pandas as pd
import numpy as np

prices = [
    100, 101, 103, 102, 104,
    106, 108, 107, 105, 103,
    101, 100, 102, 104, 107,
    109, 111, 110, 108, 106
]

df = pd.DataFrame({"price": prices})

df["return"] = df["price"].pct_change()

df["ma_short"] =  df["price"].rolling(3).mean()
df["ma_long"] =  df["price"].rolling(7).mean()

df["signal"] = np.where(df["ma_short"] > df["ma_long"], 1, np.where(df["ma_short"] < df["ma_long"], -1, 0))

df["position"] = df["signal"]

df["strategy_return"] = df["return"] * df["position"].shift(1)

initial_capital = 100000
df["portfolio"] =initial_capital * (1 + df["strategy_return"]).cumprod()

print(df)