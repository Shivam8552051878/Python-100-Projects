import datetime

import requests
USERNAME = "shivamgupta2003"
url = "https://pixe.la/v1/users"
TOKEN = "adc4d5cd1dc5d2dds2s1swsw"

user_param = {
    "token":TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

graph_endpoint = f"{url}/{USERNAME}/graphs"
graph_config = {
    "id":"graph1",
    "name":"PYTHON 100 PROJECT",
    "unit":"day",
    "type":"int",
    "color":"momiji"
}

headers = {
    "X-USER-TOKEN":TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.json())


data = {
    f"{datetime.date.today()}":"Today i have completed 38 project"
}

today = datetime.datetime.now()
pixel_endpoint = f"{graph_endpoint}/{graph_config['id']}"
pixel_config = {
    "date": today.strftime("20%y%m%d"),
    "quantity": "38",
}
#
# response = requests.post(pixel_endpoint, headers=headers, json= pixel_config)
# print(response.json())

# print(str(datetime.date.today()))

update_endpoint = f"{pixel_endpoint}/{pixel_config['date']}"
update_param = {
    "quantity":"38 "
}

response = requests.post(pixel_endpoint, json=pixel_config, headers=headers)
response.raise_for_status()
print(response.json())