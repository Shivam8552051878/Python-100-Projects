import requests
import itertools
import smtplib


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_URL = "https://www.alphavantage.co/query?&symbol=TSLA&"
STOCK_PARAM = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "apikey": "X94IL0MPRC8JIE27",
    "symbol": STOCK,
}
response = requests.get(STOCK_URL, params=STOCK_PARAM)
data = response.json()["Time Series (Daily)"]
imp_data = itertools.islice(data, 2)
date_list = [data[date] for date in imp_data]
yesterday_closing = float(date_list[0]["4. close"])
day_after_yesterday = float(date_list[1]["4. close"])
UP_DOWN = None
difference = yesterday_closing - day_after_yesterday
percentage = (difference/day_after_yesterday)*10
if difference > 0:
    UP_DOWN = "🔺"
else:
    UP_DOWN = "🔻"
if percentage > 5 or percentage < 5:
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    NEWS_API = "e27313691c024e12a96149bbe5454ded"
    NEWS_URL = "https://newsapi.org/v2/everything"
    NEWS_PARAM = {
        "qInTitle": COMPANY_NAME,
        "language": "en",
        "from_param": date_list[0],
        "to": date_list[1],
        "apikey":NEWS_API

    }
    response = requests.get(NEWS_URL, params=NEWS_PARAM)
    response.raise_for_status()
    articles = response.json()["articles"]
    three_articles = articles[:3]
    articles_list = [f"Heading: {info['title']}\n Brief: {info['description']}" for info in three_articles]
    print(articles_list)
    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    #
    MY_GMAIL = "demo8552051878@gmail.com"
    MY_PASSWORD = "xuarrpmbouuryspf"
    for i in range(3):
        with smtplib.SMTP("smtp.gmail.com", 587) as send_msg:
            send_msg.starttls()
            send_msg.login(user=MY_GMAIL, password=MY_PASSWORD)
            send_msg.sendmail(from_addr=MY_GMAIL, to_addrs=f"sg9967780426@gmail.com", msg=f"Subject:TSLA {UP_DOWN}5%\n\n{articles_list[i]}".encode('utf-8'))



# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


