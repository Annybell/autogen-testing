# filename: stock_comparison.py

import datetime
import yfinance as yf
import requests

# Get the current date
today = datetime.date.today()

# Get the start date of the current year
start_date = datetime.date(today.year, 1, 1)

# Get the stock prices for Microsoft and Okta on the start date and today
msft = yf.Ticker("MSFT")
okta = yf.Ticker("OKTA")

# Get the stock price on the first trading day of the year
msft_history = msft.history(start=start_date, end=today)
okta_history = okta.history(start=start_date, end=today)

msft_price_start = msft_history['Close'][0]
msft_price_today = msft_history['Close'][-1]

okta_price_start = okta_history['Close'][0]
okta_price_today = okta_history['Close'][-1]

# Calculate the year-to-date gain for both stocks
msft_gain = (msft_price_today - msft_price_start) / msft_price_start * 100
okta_gain = (okta_price_today - okta_price_start) / okta_price_start * 100

# Compare the year-to-date gain for both stocks
comparison = "Microsoft" if msft_gain > okta_gain else "Okta"

# Send the outcome as a POST request to the provided webhook URL
data = {
    "date": str(today),
    "msft_gain": msft_gain,
    "okta_gain": okta_gain,
    "comparison": comparison
}

response = requests.post("https://falling-fire-5834.tines.com/webhook/838cf4b997f58f02354604972dae8875/b3884ec74bf13e2933695619cc44034a", json=data)

print(response.status_code)