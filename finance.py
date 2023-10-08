# python code
import yfinance as yf
from datetime import date

# Get today's date
today = date.today()

# Get data for the current year
start_date = date(today.year, 1, 1)
end_date = today

# Fetch data for META and TESLA
meta_data = yf.download('META', start=start_date, end=end_date)
tesla_data = yf.download('TSLA', start=start_date, end=end_date)

# Calculate year-to-date gain for META and TESLA
meta_gain = ((meta_data['Close'][-1] - meta_data['Close'][0]) / meta_data['Close'][0]) * 100
tesla_gain = ((tesla_data['Close'][-1] - tesla_data['Close'][0]) / tesla_data['Close'][0]) * 100

print(f"Year-to-date gain for META: {meta_gain}%")
print(f"Year-to-date gain for TESLA: {tesla_gain}%")