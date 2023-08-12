import requests

url = "https://api.sheety.co/9106d6e6510d5f695763b42c92e513e9/workout/sheet1"
response = requests.get(url)
print(response.json())