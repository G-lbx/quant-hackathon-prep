def fixed_position_sizing(portfolio_value, position_pct, price):
    position_value = portfolio_value * position_pct
    shares = position_value / price
    return shares


def volatility_position_sizing(volatility, target_volatility):
    if volatility == 0:
        return 0
    position_pct = target_volatility / volatility

    position_pct = min(position_pct, 1.0)

    return position_pct


    



