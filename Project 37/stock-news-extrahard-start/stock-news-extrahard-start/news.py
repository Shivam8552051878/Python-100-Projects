import requests

TOP_THREE_NEWS = []
NEWS_API = "e27313691c024e12a96149bbe5454ded"
NEWS_URL = "https://newsapi.org/v2/everything"
NEWS_PARAM = {
    "q": "tesla",
    "language": "en",
    "from_param": '2023-05-15',
    "to": '2023-05-20',
    "apikey":NEWS_API

}

response = requests.get(NEWS_URL, params=NEWS_PARAM)
response.raise_for_status()
datas = response.json()["articles"]
if len(datas) < 3:
    datas = datas[:len(datas)]
else:
    datas = datas[:3]

for data in datas:
    TOP_THREE_NEWS.append({
        "Title":data["title"],
        "Description":data["description"],
        "Url":data["url"]
    })

