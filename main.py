"""
This script will get the market share of Apple and Microsoft
"""
import yfinance as yf


def get_market_shares():
    """
    This function will get the market share of a stock
    """
    # Get the data for the stock AAPL and MSFT
    aapl_stock = yf.Ticker("AAPL")
    msft_stock = yf.Ticker("MSFT")
    # Get the market shares
    aapl_market_share = aapl_stock.info['marketShare']
    msft_market_share = msft_stock.info['marketShare']
    return aapl_market_share, msft_market_share

