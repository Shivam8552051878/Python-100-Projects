##################### Extra Hard Starting Project #####################
import pandas
import random
import smtplib
import datetime

MY_MAIL = "demo8552051878@gmail.com"
MY_PASSWORD = "xuarrpmbouuryspf"
HOST = "smtp.gmail.com"
PORT = 587

# 1. Update the birthdays.csv
datas = pandas.read_csv("birthdays.csv").to_dict(orient='records')


# 2. Check if today matches a birthday in the birthdays.csv
def is_today_birthday():
    current_month = datetime.datetime.today().month
    current_day = datetime.datetime.today().day
    for data in datas:
        if current_month == data["month"] and current_day == data["day"]:
            return data


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv

template_list = ["./letter_templates/letter_1.txt", "./letter_templates/letter_2.txt",
                 "./letter_templates/letter_3.txt"]

if is_today_birthday() != None:
    file = random.choice(template_list)
    try:
        with open(file) as temp:
            template = temp.read()
    except FileNotFoundError:
        print("Not Found")
    sender_data = is_today_birthday()
    message = template.replace("[NAME]", sender_data["name"])
    with smtplib.SMTP(HOST, PORT) as connection:
        connection.starttls()
        connection.login(user=MY_MAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_MAIL, to_addrs=sender_data["email"],
                            msg="Subject:Happy Birthday\n\n" + message)


# 4. Send the letter generated in step 3 to that person's email address.
