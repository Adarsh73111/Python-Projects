import requests

# SHEETY_PRICES_ENDPOINT = "YOUR_SHEETY_ENDPOINT"
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/f390ca3e1fe4ef8fdaf0c4340a41f933/flightTracker/sheet1"

class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()

        if "prices" not in data or not data["prices"]:
            print("Warning: Google Sheet is empty. Please add some cities!")
            return []

        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)