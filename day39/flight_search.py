import datetime as dt
import requests
from flight_data import FlightData

API_TOKEN = 'token'
origin = 'DEL'

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.url='https://api.travelpayouts.com/'
        self.headers = {"X-Access-Token": API_TOKEN,}
        self.date= dt.datetime.now()

    def search(self,destination):

        params = {
            "origin": origin,  # Departure airport IATA code
            "destination": destination,  # Destination airport IATA code
            "currency": "GBP",  # Set your preferred currency
            "depart_date": f"{self.date.strftime('%Y-%m')}:6",  # Start month for 6 months
        }

        response = requests.get(self.url, params=params, headers=self.headers)
        if response.status_code == 200:
            data = response.json().get("data", [])
            if data != {}:
                data = sorted(data.items(), key=lambda item: item[1].get('price', float('inf')))
                data = data[0][1]
                flight = FlightData(data['origin'],data['destination'],
                                    data['airline'],data['departure_at'],
                                    data['return_at'],data['expires_at'],
                                    data['price'],data['flight_number'])
                return flight

        else :
            return None


    @staticmethod
    def get_code(city):

        url =  "https://api.travelpayouts.com/data/en/cities.json"

        response = requests.get(url)
        if response.status_code == 200:
            locations = response.json()
            for location in locations:
                if city.lower() in location["name"].lower():
                    return location["code"]  # Return the IATA code
        else:
            print(f"Error {response.status_code}: {response.text}")

        return None
