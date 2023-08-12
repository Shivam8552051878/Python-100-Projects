import time

from bs4 import BeautifulSoup
import requests

URL = "https://www.zillow.com/homes/for_sale/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-86.50900840759277%2C%22east%22%3A-86.37408256530762%2C%22south%22%3A39.728049365821484%2C%22north%22%3A39.80444800460356%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A787854%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A4000%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%7D"

class Zillow:
    def __init__(self):
        self.my_list = []
        self.get_data()

    def get_data(self):
        header = {
            "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en-GB;q=0.9,en;q=0.8"
        }
        response = requests.get(url=URL, headers=header)
        response.raise_for_status()
        time.sleep(10)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        url = soup.find_all(name="a", class_="Anchor-c11n-8-85-1__sc-hn4bge-0 jPLqmy carousel-photo")
        url_list = [url[i].get("href") for i in
                    range(len(url)) if i % 3 == 0]
        address = [add.getText() for add in soup.find_all(name="address")]
        price_list = [price.getText() for price in soup.find_all(name="span", class_="srp__sc-16e8gqd-1 jLQjry")]

        # print(url_list)
        # print(url)
        print(len(url_list), len(address), len(price_list))
        if len(url_list) != 0 and len(price_list) != 0:
            for i in range(len(url_list)):
                self.my_list.append({
                    "url": url_list[i],
                    "address": address[i],
                    "price": price_list[i]
                })
        print(self.my_list)

#
# xp = Zillow()
# print(xp.my_list)
