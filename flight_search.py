import requests
from flight_data import FlightData
import os

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = ""

class FlightSearch:


    # get the IATA code for each city from TEQUILA API
    def get_destination_code(self,city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": os.environ["TEQUILA_API_KEY"]}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint,headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    # get the information for cheaper flight tickets from TEQUILA API
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": os.environ["TEQUILA_API_KEY"]}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "data_from": from_time.strftime("%d/%m/%Y"),
            "data_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 30,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "CAD"
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=headers,params=query)
        try:
            data = response.json()["data"][0]

        # if no direct flight is found
        except IndexError:
            query["max_stopovers"] = 1
            response=requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search",headers=headers,params=query)
            data = response.json()["data"][0]
            flight_data=FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["flyTo"],
                destination_airport=data["route"][1]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            return flight_data

        # direct flight is found
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["flyTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            return flight_data