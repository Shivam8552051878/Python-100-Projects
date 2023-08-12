import requests

url = "https://qrcode-monkey.p.rapidapi.com/qr/uploadImage"

payload = {
	"key1": "value",
	"key2": "value"
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "f56ee5f54bmshca1d5bd7747ccf8p1c0941jsnf30fcd7728bc",
	"X-RapidAPI-Host": "qrcode-monkey.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json()[""])