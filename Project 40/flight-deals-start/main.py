import os
import smtplib
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch


ORIGIN_CITY_IATA = "LON"
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

data_manager = DataManager()
data_sheet = data_manager.get_destination_data()
flight = FlightSearch()

for data in data_sheet:
    if data["iataCode"] == "":
        data_manager.update_destination_codes()


for data in data_sheet:
    flight_data = flight.check_flight(origin_city_code=ORIGIN_CITY_IATA, destination_city_code=data["iataCode"], from_time=tomorrow, to_time=six_month_from_today)
    if flight_data.price < data["lowestPrice"]:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            sender_mail = "demo8552051878@gmail.com"
            reciver_mail = "sg9967780426@gmail.com"
            connection.login(sender_mail, os.environ.get("EMAIL_PASSWORD"))
            connection.sendmail(from_addr=sender_mail, to_addrs=reciver_mail, msg=f"Subject:Low price alert\n\nOnly ${flight_data.price} from {flight_data.origin_city}-{flight_data.origin_airport} to {flight_data.destination_city}-{flight_data.destination_airport} for {flight_data.out_date} to {flight_data.return_date}")