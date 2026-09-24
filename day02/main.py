import os
import pandas as pd
from data import get_test_data
from strategy import moving_average_strategy
from backtest import run_backtest
from metrics import (
    annual_volatility,
    max_drawdown,
    sharpe_ratio,
    sortino_ratio,
    calmar_ratio
)

df = get_test_data()

df = moving_average_strategy(df, 3, 7)

df = run_backtest(df, 100000)

summary = pd.DataFrame({
    "Metric": [
        "Final Portfolio Value",
        "Annual Return",
        "Annual Volatility", 
        "Max Drawdown", 
        "Sharpe Ratio", 
        "Sortino Ratio", 
        "Calmar Ratio"
    ],
    "Value": [
        df["portfolio"].iloc[-1],  # get the last value of the portfolio, iloc means index location
        df["strategy_return"].mean() * 252,
        annual_volatility(df["strategy_return"]),
        max_drawdown(df["portfolio"]),
        sharpe_ratio(df["strategy_return"]),
        sortino_ratio(df["strategy_return"]),
        calmar_ratio(df["portfolio"])
    ]
})


os.makedirs("results", exist_ok=True)

summary.to_csv(
    "results/summary.csv",
    index=False
)

df.to_csv(
    "results/backtest_detail.csv",
    index=False
)