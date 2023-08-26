import numpy as np
import pandas as pd
import scipy.optimize as sco

def mean_reversion(df, window):
    """Calculate the mean reversion signal for a given window."""
    zscore = (df - df.rolling(window).mean()) / df.rolling(window).std()
    return -zscore

def momentum(df, window):
    """Calculate the momentum signal for a given window."""
    returns = df.pct_change()
    return returns.rolling(window).sum()

def combine_signals(signals):
    """Combine multiple trading signals by taking their average."""
    combined_signal = sum(signals) / len(signals)
    return np.sign(combined_signal)

def backtest_portfolio(returns, positions, transaction_cost):
    """Backtest a portfolio of positions."""
    # Calculate the portfolio returns
    portfolio_returns = (positions.shift(1) * returns) - (np.abs(positions - positions.shift(1)) * transaction_cost)

    # Calculate the cumulative returns
    cumulative_returns = (1 + portfolio_returns).cumprod()

    # Calculate the drawdowns
    previous_peaks = np.maximum.accumulate(cumulative_returns)
    drawdowns = (cumulative_returns - previous_peaks) / previous_peaks

    # Calculate the statistics
    sharpe_ratio = np.sqrt(252) * portfolio_returns.mean() / portfolio_returns.std()
    max_drawdown = drawdowns.min()

    return cumulative_returns, sharpe_ratio, max_drawdown

def optimize_portfolio(returns):
    """Optimize the portfolio weights to maximize the Sharpe ratio."""
    # Define the objective function
    def objective_function(weights, returns):
        portfolio_returns = np.dot(returns, weights)
        sharpe_ratio = np.sqrt(252) * portfolio_returns.mean() / portfolio_returns.std()
        return -sharpe_ratio

    # Define the constraints
    constraints = [{'type': 'eq', 'fun': lambda x: np.sum(x) - 1}]

    # Define the bounds
    bounds = [(0, 1) for i in range(len(returns.columns))]

    # Initialize the weights
    weights = np.ones(len(returns.columns)) / len(returns.columns)

    # Optimize the weights
    optimized_weights = sco.minimize(objective_function, weights, args=(returns,), method='SLSQP', bounds=bounds, constraints=constraints)

    return optimized_weights.x
