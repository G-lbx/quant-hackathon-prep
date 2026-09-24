def run_backtest(df, initial_capital):
    df = df.copy()
    df["return"] = df["price"].pct_change()

    df["position"] = df["signal"]

    df["strategy_return"] = df["return"] * df["position"].shift(1)

    df["portfolio"] = initial_capital * (1 + df["strategy_return"]).cumprod()

    return df