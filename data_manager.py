import requests

SHEETY_PRICES_ENDPOINT = ""
SHEETY_USER_ENDPOINT = ""

class DataManager:

    def __init__(self):
        self.destination_data = {}

    # use the Sheety API to get all the data in google sheet which is linked to Sheety
    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    # update IATA code in google sheet using put method
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {"price": {"iataCode": city["iataCode"]}}
            response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",json=new_data)

    # get customer emails from google sheet
    def get_customer_emails(self):
        customers_endpoint = SHEETY_USER_ENDPOINT
        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
