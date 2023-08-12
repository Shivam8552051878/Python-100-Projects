import requests
api_key = "X94IL0MPRC8JIE27"
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=TSLA&outputsize=full&apikey=X94IL0MPRC8JIE27'

r = requests.get(url)
data = r.json()

print(data)