## Project Overview
This project aims to develop a statistical arbitrage strategy for cryptocurrencies using Python. The primary goal is to leverage mean-reversion trading and portfolio optimization techniques to generate alpha and minimize risk in cryptocurrency trading. The project involves:

- Retrieving Historical Price Data: Collecting data for Bitcoin (BTC) and Ethereum (ETH) from the <a href="https://www.coingecko.com/api/documentations/v3" target="_new">CoinGecko API</a>.
- Data Manipulation: Using the pandas library to process and analyze the data.
- Trading Strategy Implementation: Executing trades based on calculated daily returns.
- Portfolio Optimization: Employing functions to balance risk and return.
- Results Visualization: Plotting and saving the outcomes in the `results` directory.
- The project can be expanded by incorporating additional cryptocurrencies or adopting more advanced trading strategies.

The project can be expanded by incorporating additional cryptocurrencies or adopting more advanced trading strategies.

## Data
We will use historical price data for Bitcoin (BTC) and Ethereum (ETH) obtained from the <a href="https://www.coingecko.com/api/documentations/v3" target="_new">CoinGecko API</a>. We will use the `requests` library to make API requests and the `pandas` library to manipulate the data.

## Requirements
This project requires Python 3.7 or later.

## Usage

1. Clone the repository:
```bash
git clone https://github.com/notabombe/statistical-arbitrage-cryptocurrencies.git

```
2. Navigate to the project directory:

```bash
cd statistical-arbitrage-cryptocurrencies

```
3. Install Dependencies:

```
pip install -r requirements.txt
```

4. Open the `config.py` file and enter your CoinGecko API key:
   
```makefile
COINGECKO_API_KEY = "your-api-key"

```
5. Run the `main.py` file:
   
```css
python main.py

```
This will retrieve the price data, calculate the daily returns, and execute the statistical arbitrage strategy. The results will be plotted and saved in the `results` directory.

## Files
* `config.py`: Configuration file for the project.
* `data.py`: Data retrieval and manipulation functions.
* `portfolio.py`: Portfolio optimization functions.
* `trading.py`: Trading strategy functions.
* `main.py`: Main script to run the project.
* `results/`: Directory to store the results of the project.

## Example Results
<img src="https://i.imgur.com/vYbhF22.png" alt="BTC-ETH Prices">
<img src="https://i.imgur.com/iwpZiKw.png" alt="Portfolio Positions">

## License
This project is licensed under the terms of the MIT license. See the [LICENSE](https://github.com/notabombe/Statistical-Arbitrage-in-Cryptocurrencies/blob/master/LICENSE) file for details.

## Conclusion
This project demonstrates how to develop a statistical arbitrage strategy for cryptocurrencies using Python. By combining mean-reversion trading and portfolio optimization, we were able to generate alpha and minimize risk. This project can be extended by adding more cryptocurrencies to the portfolio or by using more sophisticated trading strategies.

