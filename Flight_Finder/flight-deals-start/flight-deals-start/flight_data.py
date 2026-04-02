class FlightData:
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date


def find_cheapest_flight(data):
    if data is None or not data['data']:
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    first_flight = data['data'][0]
    price = float(first_flight['price']['grandTotal'])
    origin = first_flight['itineraries'][0]['segments'][0]['departure']['iataCode']
    destination = first_flight['itineraries'][0]['segments'][0]['arrival']['iataCode']
    out_date = first_flight['itineraries'][0]['segments'][0]['departure']['at'].split("T")[0]

    # Simple logic for this part assumes direct flights.
    # Logic for return date would be added in Part 2.
    return FlightData(price, origin, destination, out_date, "N/A")