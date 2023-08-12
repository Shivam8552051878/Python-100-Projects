import smtplib

person_to_mail = "sg9967780426@yahoo.com"
MY_MAIL = "demo8552051878@gmail.com"
MY_PASSWORD = "jmakedkbdtzvxjhc"
HOST = "smtp.gmail.com"
PORT = 587
with smtplib.SMTP(HOST, PORT) as connection:
    connection.starttls()
    connection.login(user=MY_MAIL, password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_MAIL, to_addrs=person_to_mail, msg="Subject:Happy Birthday\n\nHappy birthday shivam")
