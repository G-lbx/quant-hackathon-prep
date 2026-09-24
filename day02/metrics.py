import numpy as np


def annual_return(portfolio):
    clean_portfolio = portfolio.dropna()
    trading_days = clean_portfolio.shape[0]
    initial_value = clean_portfolio.iloc[0]
    final_value = clean_portfolio.iloc[-1]

    years = trading_days / 252

    cagr = (final_value / initial_value) ** (1 / years) - 1
    return cagr


def annual_volatility(strategy_return):
    daily_volatility = strategy_return.std()
    return daily_volatility * np.sqrt(252)
    


def max_drawdown(portfolio):
    running_max = portfolio.cummax()
    drawdown = (portfolio - running_max) / running_max
    return drawdown.min()


def sharpe_ratio(strategy_return):
    mean_return = strategy_return.mean()
    daily_volatility = strategy_return.std()
    if daily_volatility == 0:
        return np.nan
    return mean_return / daily_volatility * np.sqrt(252)


def sortino_ratio(strategy_return):
    returns = strategy_return.dropna()
    if returns.empty:
        return np.nan
    
    downside_returns = returns.clip(upper=0)
    downside_deviation = np.sqrt(np.mean(downside_returns**2))
    if downside_deviation == 0:
        return np.nan
    return returns.mean() / downside_deviation * np.sqrt(252)


def calmar_ratio(portfolio):
    return annual_return(portfolio) / abs(max_drawdown(portfolio))