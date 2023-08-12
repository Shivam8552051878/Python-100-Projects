import requests

response = requests.get(url="https://qrco.de/be325n")
print(response.text)