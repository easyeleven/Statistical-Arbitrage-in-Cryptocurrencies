import requests
import pandas as pd
from datetime import datetime, timedelta


def get_price_data(api_key, coin_id, days):
    """
    Retrieves historical price data from the CoinGecko API.

    Args:
        api_key (str): Your CoinGecko API key.
        coin_id (str): The ID of the cryptocurrency to retrieve data for.
        days (int): The number of days of historical data to retrieve.

    Returns:
        pandas.DataFrame: A DataFrame containing the historical price data.
    """
    today = datetime.now()
    start_date = (today - timedelta(days=days)).strftime('%d-%m-%Y')
    end_date = today.strftime('%d-%m-%Y')

    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart/range?vs_currency=usd&from={start_date}&to={end_date}"

    response = requests.get(url, headers={"Accept": "application/json", "X-CoinGecko-API-Key": api_key})

    data = response.json()
    prices = data['prices']
    df = pd.DataFrame(prices, columns=['time', 'price'])

    df['time'] = pd.to_datetime(df['time'], unit='ms')
    df['price'] = pd.to_numeric(df['price'])

    df.set_index('time', inplace=True)

    return df


def calculate_returns(prices):
    """
    Calculates daily returns from a DataFrame of prices.

    Args:
        prices (pandas.DataFrame): A DataFrame of prices.

    Returns:
        pandas.DataFrame: A DataFrame of daily returns.
    """
    returns = prices.pct_change(1)
    returns.iloc[0] = 0

    return returns
