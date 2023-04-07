import pandas as pd
import matplotlib.pyplot as plt
import data
import trading
import portfolio

# Retrieve the data
prices = data.get_prices(['bitcoin', 'ethereum'])

# Calculate the daily returns
returns = prices.pct_change().dropna()

# Calculate the trading signals
btc_mean_reversion = trading.mean_reversion(prices['bitcoin'], window=10)
eth_mean_reversion = trading.mean_reversion(prices['ethereum'], window=10)
btc_momentum = trading.momentum(prices['bitcoin'], window=30)
eth_momentum = trading.momentum(prices['ethereum'], window=30)

# Combine the trading signals
signals = [btc_mean_reversion, eth_mean_reversion, btc_momentum, eth_momentum]
combined_signal = trading.combine_signals(signals)

# Backtest the portfolio
positions = portfolio.get_positions(combined_signal)
cumulative_returns, sharpe_ratio, max_drawdown = trading.backtest_portfolio(returns, positions, transaction_cost=0.001)

# Optimize the portfolio
optimized_weights = trading.optimize_portfolio(returns)
optimized_positions = portfolio.get_positions(optimized_weights)

