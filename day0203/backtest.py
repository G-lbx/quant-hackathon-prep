def run_backtest(df, initial_capital = 100000, transaction_cost = 0.001):
    df = df.copy()
    df["return"] = df["price"].pct_change().fillna(0)

    df["position"] = df["signal"]

    df["Gross_return"] = df["return"] * df["position"].shift(1).fillna(0)

    df["Turnover"] = df["position"].diff().abs().fillna(0)

    df["Trading_Cost"] = df["Turnover"] * transaction_cost

    df["Net_return"] = df["Gross_return"] - df["Turnover"] * transaction_cost

    df["portfolio"] = initial_capital * (1 + df["Net_return"]).cumprod()

    return df