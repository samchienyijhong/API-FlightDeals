import os
import requests
import dotenv

dotenv.load_dotenv()
SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/xxxxxxxxxxxxxxxxxxxxxx/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.destination_data = {}
        self.headers = {
                "Authorization": f"Bearer {SHEETY_TOKEN}"
            }

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self.headers
            )
            print(response.text)
