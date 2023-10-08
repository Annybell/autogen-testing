# filename: stock_analysis.py

import datetime
import yfinance as yf
import requests

# Get the current date
today = datetime.date.today()

# Define the start date as January 1 of the current year
start_date = datetime.date(today.year, 1, 1)

# Get the stock prices for Nvidia, Microsoft, and Okta on the start date and today
nvidia = yf.Ticker("NVDA")
microsoft = yf.Ticker("MSFT")
okta = yf.Ticker("OKTA")

nvidia_price_start = nvidia.history(start=start_date.isoformat(), end=start_date.isoformat()).iloc[0]['Close']
nvidia_price_today = nvidia.history(start=today.isoformat(), end=today.isoformat()).iloc[0]['Close']

microsoft_price_start = microsoft.history(start=start_date.isoformat(), end=start_date.isoformat()).iloc[0]['Close']
microsoft_price_today = microsoft.history(start=today.isoformat(), end=today.isoformat()).iloc[0]['Close']

okta_price_start = okta.history(start=start_date.isoformat(), end=start_date.isoformat()).iloc[0]['Close']
okta_price_today = okta.history(start=today.isoformat(), end=today.isoformat()).iloc[0]['Close']

# Calculate the year-to-date gain for each stock
nvidia_gain = (nvidia_price_today - nvidia_price_start) / nvidia_price_start * 100
microsoft_gain = (microsoft_price_today - microsoft_price_start) / microsoft_price_start * 100
okta_gain = (okta_price_today - okta_price_start) / okta_price_start * 100

# Prepare the data to be sent
data = {
    'date': today.isoformat(),
    'nvidia_gain': nvidia_gain,
    'microsoft_gain': microsoft_gain,
    'okta_gain': okta_gain
}

# Send the data as a POST request to the specified webhook URL
response = requests.post('webhook_url', json=data)

# Print the response
print(response.text)