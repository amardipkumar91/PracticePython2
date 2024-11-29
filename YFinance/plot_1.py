import yfinance as yf
import pandas as pd

# Define the stock ticker and date range
ticker = "AAPL"  # Replace with the desired stock ticker
start_date = "2020-11-23"  # Replace with the desired date
end_date = "2023-11-24"  # Same as start date for one day's data

# Download intraday data
data = yf.download(ticker, start=start_date, end=end_date, interval = '1d')  # 1-minute intervals

# Ensure the data is not empty
if data.empty:
    print("No data found for the given date range.")
else:
    # Format the data to include only OHLC
    ohlc_data = data[['Open', 'High', 'Low', 'Close']]
    ohlc_data.reset_index(inplace=True)
    print(ohlc_data)  # Display the first few rows
