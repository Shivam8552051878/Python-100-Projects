import smtplib
import datetime
import random
import json

person_to_mail = "sg9967780426@yahoo.com"
MY_MAIL = "demo8552051878@gmail.com"
MY_PASSWORD = "pjkdcyimliyhxvtl"
HOST = "smtp.gmail.com"
PORT = 587


def send_mail(user_mail,message):
    with smtplib.SMTP(HOST, PORT) as connection:
        connection.starttls()
        connection.login(user=MY_MAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_MAIL, to_addrs=user_mail, msg=message)


def get_dic():
    with open("data.json") as file:
        data = json.load(file)
        return data[str(random.randint(0, len(data)))]


day = datetime.datetime.today().weekday()
print(day)
if day == 0:
    massage = get_dic()
    print(massage)
    send_massage = f"Subject:Monday Motivation\n\n{massage['quets']}\nBy\n{massage['writter']}"
    send_mail(person_to_mail, send_massage)
