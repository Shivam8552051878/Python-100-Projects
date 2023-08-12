from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/newest")
y_web_page = response.text

soup = BeautifulSoup(y_web_page, 'html.parser')


vote = soup.find_all(name="span", class_="score")
titleline = soup.find_all(name="span", class_="titleline")
title = titleline[0].find(name="a").string
link = titleline[0].find(name="a").get("href")
# print(len(vote), len(titleline))
# print(vote[1].text)

list_dic = []
for i in range(len(vote)):
    list_dic.append({
        "title":titleline[i].find(name="a").string,
    "link":titleline[i].find(name="a").get("href"),
    "vote":int(vote[i].text.split(" ")[0])
    })

largest = {}
temp = 0
for data in list_dic:
    if data["vote"] > temp:
        temp = data["vote"]
        largest = data
        # print(data["vote"])


print(largest)



# print(soup.prettify())
# titleline = soup.select(selector=".titleline")
# for title in titleline[6:]:
#     print(title.select(selector="span a")[0].get("href"))
#     print(title.text)
#     print("\n\n\n\n")
#     print(title)
# a = titleline[0].select(selector="span a")
# print(a[0].get("href"))
# print(a[0].string)




















# import lxml
# with open("./website.html", encoding="utf8") as file:
#     data = file.read()
#     # print(data)
#
# soup = BeautifulSoup(data, 'html.parser')
# # print(soup.prettify())
# # print(soup.getText())
# # for a in soup.find_all('a'):
# #     print(a.get("href"))
#
# selector = soup.select_one(selector="#name")
# print(selector.string)