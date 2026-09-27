import os
import pandas as pd
from data import get_test_data
from strategy import moving_average_strategy, momentum_strategy, mean_reversion_strategy, breakout_strategy
from backtest import run_backtest, run_backtest_fixed_position
from metrics import (
    annual_volatility,
    max_drawdown,
    sharpe_ratio,
    sortino_ratio,
    calmar_ratio
)

df = get_test_data()

# Moving Average Strategy
df = moving_average_strategy(df, 3, 7)
'''
# Momentum Strategy
momentum_df = momentum_strategy(df, 20)

# Mean Reversion Strategy
mean_reversion_df = mean_reversion_strategy(df, 20, 1.5)

# Breakout Strategy
breakout_df = breakout_strategy(df, 20)

momentum_df = run_backtest(momentum_df, 100000)
mean_reversion_df = run_backtest(mean_reversion_df, 100000)
breakout_df = run_backtest(breakout_df, 100000)
'''
fixed_position_df = run_backtest_fixed_position(df, 100000, 0.001, 0.5)
volatility_position_df = run_backtest(df, 100000, 0.001, 0.02)
def get_summary(df, strategy_name):
    return {
        "Strategy": strategy_name,
        "Final Portfolio Value": df["portfolio"].iloc[-1],
        "Annual Return": df["Net_return"].mean() * 252,
        "Annual Volatility": annual_volatility(df["Net_return"]),
        "Max Drawdown": max_drawdown(df["portfolio"]),
        "Sharpe Ratio": sharpe_ratio(df["Net_return"]),
        "Sortino Ratio": sortino_ratio(df["Net_return"]),
        "Calmar Ratio": calmar_ratio(df["portfolio"]),
        "Total Trading Cost": df["Trading_Cost"].sum(),
        "Number of Trades": (df["Turnover"] > 0).sum()
    }

fixed_position_summary = get_summary(fixed_position_df, "Fixed Position Strategy")
volatility_position_summary = get_summary(volatility_position_df, "Volatility Position Strategy")


"""
summary = pd.DataFrame({
    "Metric": [
        "Final Portfolio Value",
        "Annual Return",
        "Annual Volatility", 
        "Max Drawdown", 
        "Sharpe Ratio", 
        "Sortino Ratio", 
        "Calmar Ratio",
        "Total Trading Cost",
        "Number of Trades"
    ],
    "Value": [
        df["portfolio"].iloc[-1],  # get the last value of the portfolio, iloc means index location
        df["Net_return"].mean() * 252,
        annual_volatility(df["Net_return"]),
        max_drawdown(df["portfolio"]),
        sharpe_ratio(df["Net_return"]),
        sortino_ratio(df["Net_return"]),
        calmar_ratio(df["portfolio"]),
        df["Trading_Cost"].sum(),
        (df["Turnover"] > 0).sum()
    ]
})
"""
# momentum_summary = get_summary(momentum_df, "Momentum Strategy")
# mean_reversion_summary = get_summary(mean_reversion_df, "Mean Reversion Strategy")
# breakout_summary = get_summary(breakout_df, "Breakout Strategy")

results = [fixed_position_summary, volatility_position_summary]
comparison = pd.DataFrame(results)  
comparison.to_csv("results/comparison.csv", index=False)