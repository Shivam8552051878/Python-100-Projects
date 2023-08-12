from pprint import pprint
import requests
import flight_search
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/9106d6e6510d5f695763b42c92e513e9/clubMember"
class DataManager:

    def __init__(self):
        self.club_member = []
        self.get_club_member_data()
        self.destination_data = {}


    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT + "/prices")
        data = response.json()
        self.destination_data = data["prices"]
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data


    # 6. In the DataManager Class ma    ke a PUT request and use the row id  from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            code = flight_search.FlightSearch().get_destination_code(city["city"])
            new_data = {
                "price": {
                    "iataCode": code
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            # print(response.text)



    def get_club_member_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT + "/clubMembers")
        data = response.json()
        self.club_member = data["clubMembers"]
        # print(self.club_member)

    def add_club_member_data(self):
        print("Welcome to Shivam's Flight Club\nWe find the best flight deals and email you")

        firstname  = input("What is your first name?\n")
        lastname = input("What is your last name?\n")
        email = input("What is your email?\n")
        param = {
            "clubmember":
                {
                 "firstName": firstname.title(),
                 "lastName": lastname.title(),
                 "email": email
                }
        }
        response = requests.post(url=SHEETY_PRICES_ENDPOINT + "/clubMembers", json=param)
        # response.raise_for_status()
        print(response.json())
        self.get_club_member_data()


