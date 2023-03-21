"""
This script uses the Alpha Vantage API to get the market share data for Apple and Microsoft.
"""

import json
import requests
import matplotlib.pyplot as plt

# Alpha Vantage API key
api_key = 'X72ASWYDPSHOAGBG'

# API endpoint
url = 'https://www.alphavantage.co/query'

# Function to get the market share data for a given symbol

def get_market_share(symbol):
    # API parameters
    params = {
        'function': 'GLOBAL_QUOTE',
        'symbol': symbol,
        'apikey': api_key
    }

    # Make the API request
    response = requests.get(url, params=params)

    # Parse the JSON response
    data = json.loads(response.text)

    # Extract the market share data
    market_share = float(data['Global Quote']['05. price'])

    return market_share

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
apple_share = get_market_share('AAPL')
microsoft_share = get_market_share('MSFT')

apple_stock = get_stock_data('APPL')
microsoft_stock = get_stock_data('MSFT')

# Print the market share data
print(f"Apple market share: {apple_share}")
print(f"Microsoft market share: {microsoft_share}")
print(f"Apple stock data: {apple_stock.head()}")
print(f"Apple stock data: {microsoft_stock.head()}")


# # Plot a bar chart comparing the market share data
# labels = ['Apple', 'Microsoft']
# values = [apple_share, microsoft_share]

# plt.bar(labels, values)
# plt.title('Market Share Comparison')
# plt.ylabel('Market Share')
# plt.show()