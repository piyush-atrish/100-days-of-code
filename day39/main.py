#============================================Day39=======================================================

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
data = data_manager.get_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

if data[0]['iataCode'] == '' :
    for row in data :
        row['iataCode'] = flight_search.get_code(row['city'])
    data_manager.destination_data=data
    data_manager.update("iataCode")

for  cities in data :
    flight = flight_search.search(cities['iataCode'])
    if flight is not None:
        if float(flight.price) < float(cities['lowestPrice']):
            cities['lowestPrice'] = float(flight.price)
            notification_manager.send_message(flight)

