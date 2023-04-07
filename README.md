## Project Overview
The goal of this project is to develop a statistical arbitrage strategy for cryptocurrencies using Python. We will use mean-reversion trading and portfolio optimization to generate alpha and minimize risk.
## Data
We will use historical price data for Bitcoin (BTC) and Ethereum (ETH) obtained from the [CoinGecko API] (https://www.coingecko.com/api/documentations/v3" target="_new). We will use the `requests` library to make API requests and the `pandas` library to manipulate the data.
## Requirements
This project requires Python 3.7 or later, as well as the following Python packages:
* `requests`
* `pandas`
* `numpy`
* `matplotlib`
* `scipy`
* `datetime`
* `json`

To install these packages, run the following command:
```
pip install requests pandas numpy matplotlib scipy datetime json

```
## Usage
1. Clone the repository:
```bash
git clone https://github.com/yourusername/statistical-arbitrage-cryptocurrencies.git

```
1. Navigate to the project directory:
```bash
cd statistical-arbitrage-cryptocurrencies

```
1. Open the `config.py` file and enter your CoinGecko API key:
```makefile
COINGECKO_API_KEY = "your-api-key"

```
1. Run the `main.py` file:
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
This project is licensed under the terms of the MIT license. See the [LICENSE](LICENSE" target="_new) file for details.

## Conclusion
This project demonstrates how to develop a statistical arbitrage strategy for cryptocurrencies using Python. By combining mean-reversion trading and portfolio optimization, we were able to generate alpha and minimize risk. This project can be extended by adding more cryptocurrencies to the portfolio or by using more sophisticated trading strategies.

