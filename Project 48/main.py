import os
import smtplib

import requests
import bs4

URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
header = {
    "Accept-Language":"en-US,en-GB;q=0.9,en;q=0.8",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

response = requests.get(url=URL, headers=header)
response.raise_for_status()
print(response)
html_data = response.text

soup = bs4.BeautifulSoup(html_data, "html.parser")
# print(soup.prettify())
row_data_price_int = soup.find("span", class_="a-price-whole").getText()
row_data_price_decimal = soup.find("span", class_="a-price-fraction").getText()
shipment_charge = soup.find("span", class_="a-size-base a-color-secondary").getText().split()[0]
# print(row_data_price_int.getText(), row_data_price_decimal.getText(), shipment_charge.getText().split()[0])

price = float(row_data_price_int + row_data_price_decimal)
if price < 100:
    GMAIL = "demo8552051878@gmail.com"
    recever = "sg9967780426@gmail.com"
    password = os.environ.get("PASSWORD")
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=GMAIL, password=password)
        connection.sendmail(from_addr=GMAIL, to_addrs=recever, msg=f"Subject:Instanp pot price is less\n\nHi\nThe instant port price is {price} Hurry up and buy it\nlink: {URL}")