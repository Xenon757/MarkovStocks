"""
This script uses the Alpha Vantage API to get the market share data for Apple and Microsoft.
"""

import json
import requests
import pandas as pd
# import matplotlib.pyplot as plt
import alpha_vantage
from alpha_vantage.timeseries import TimeSeries

# Alpha Vantage API key
api_key = 'X72ASWYDPSHOAGBG'

# API endpoint
url = 'https://www.alphavantage.co/query'

# Function to get the market share data for a given symbol



def get_market_share(api_key, symbol1='AAPL', symbol2='MSFT'):
    """
    Returns the market share of two stocks as a percentage.
    """
    # Initialize the TimeSeries class with your API key
    ts = TimeSeries(key=api_key)

    # Get the stock data for the two symbols
    symbol1_data, _ = ts.get_quote_endpoint(symbol=symbol1)
    symbol2_data, _ = ts.get_quote_endpoint(symbol=symbol2)

    # Calculate the market share of the two symbols
    total_market_cap = float(symbol1_data['Global Quote'][f'{symbol1} Market Cap']) + float(symbol2_data['Global Quote'][f'{symbol2} Market Cap'])
    symbol1_market_share = (float(symbol1_data['Global Quote'][f'{symbol1} Market Cap']) / total_market_cap) * 100
    symbol2_market_share = (float(symbol2_data['Global Quote'][f'{symbol2} Market Cap']) / total_market_cap) * 100

    # Return the market share as a dictionary
    return {
        symbol1: symbol1_market_share,
        symbol2: symbol2_market_share,
    }


def get_stock_data(symbol):
    # API parameters
    params = {
        'function': 'TIME_SERIES_DAILY_ADJUSTED',
        'symbol': symbol,
        'apikey': api_key
    }

    # Make the API request
    response = requests.get(url, params=params)

    # Parse the JSON response
    data = json.loads(response.text)

    # Convert the data to a pandas DataFrame
    df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')

    # Convert the column data types to floats
    df = df.astype(float)

    return df


# Get the market share data for Apple and Microsoft
# apple_share = get_market_share('AAPL')
# microsoft_share = get_market_share('MSFT')

# apple_stock = get_stock_data('AAPL')
# microsoft_stock = get_stock_data('MSFT')

# # Print the market share data
# print(f"Apple market share: {apple_share}")
# print(f"Microsoft market share: {microsoft_share}")
# print(f"Apple stock data: {apple_stock.head()}")
# print(f"Apple stock data: {microsoft_stock.head()}")

market_share = get_market_share(api_key, 'AAPL', 'MSFT')


# # Plot a bar chart comparing the market share data
# labels = ['Apple', 'Microsoft']
# values = [apple_share, microsoft_share]

# plt.bar(labels, values)
# plt.title('Market Share Comparison')
# plt.ylabel('Market Share')
# plt.show()
