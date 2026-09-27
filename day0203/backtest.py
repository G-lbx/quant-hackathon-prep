from position_sizing import volatility_position_sizing



def run_backtest(df, initial_capital = 100000, transaction_cost = 0.001, target_volatility=0.02):
    df = df.copy()
    df["return"] = df["price"].pct_change().fillna(0)

    df["volatility"] = df["return"].rolling(20).std().fillna(0)

    df["position_pct"] = df["volatility"].apply(lambda x: volatility_position_sizing(x, target_volatility))

    df["position"] = df["signal"].shift(1).fillna(0) * df["position_pct"]

    df["Gross_return"] = df["return"] * df["position"]

    df["Turnover"] = df["position"].diff().abs().fillna(0)

    df["Trading_Cost"] = df["Turnover"] * transaction_cost

    df["Net_return"] = df["Gross_return"] - df["Trading_Cost"]

    df["portfolio"] = initial_capital * (1 + df["Net_return"]).cumprod()

    return df

def run_backtest_fixed_position(df, initial_capital = 100000, transaction_cost = 0.001, position_pct = 0.5):
    df = df.copy()
    df["return"] = df["price"].pct_change().fillna(0)

    df["volatility"] = df["return"].rolling(20).std().fillna(0)

    df["position"] = df["signal"].shift(1).fillna(0) * position_pct

    df["Gross_return"] = df["return"] * df["position"]

    df["Turnover"] = df["position"].diff().abs().fillna(0)

    df["Trading_Cost"] = df["Turnover"] * transaction_cost

    df["Net_return"] = df["Gross_return"] - df["Trading_Cost"]

    df["portfolio"] = initial_capital * (1 + df["Net_return"]).cumprod()
    return df