import numpy as np
import pandas as pd
from scipy.optimize import minimize


def objective(weights, returns, cov_matrix, target_return):
    """
    Objective function to minimize for portfolio optimization.

    Args:
        weights (numpy.ndarray): An array of portfolio weights.
        returns (pandas.DataFrame): A DataFrame of daily returns.
        cov_matrix (numpy.ndarray): The covariance matrix of the returns.
        target_return (float): The target daily return.

    Returns:
        float: The portfolio variance.
    """
    portfolio_return = np.sum(returns.mean() * weights)
    portfolio_variance = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

    # Penalize for not meeting target return
    penalty = abs(portfolio_return - target_return)

    return portfolio_variance + penalty


def optimize_portfolio(returns, target_return, risk_free_rate=0.0):
    """
    Optimize the portfolio weights to maximize the Sharpe ratio.

    Args:
        returns (pandas.DataFrame): A DataFrame of daily returns.
        target_return (float): The target daily return.
        risk_free_rate (float): The daily risk-free rate.

    Returns:
        dict: A dictionary containing the optimal portfolio weights and Sharpe ratio.
    """
    cov_matrix = returns.cov()

    num_assets = len(returns.columns)

    constraints = [{'type': 'eq', 'fun': lambda x: np.sum(x) - 1}]

    bounds = tuple((0, 1) for i in range(num_assets))

    initial_weights = num_assets * [1.0 / num_assets]

    optimized = minimize(objective, initial_weights, args=(returns, cov_matrix, target_return),
                         method='SLSQP', bounds=bounds, constraints=constraints)

    weights = optimized.x

    portfolio_return = np.sum(returns.mean() * weights
