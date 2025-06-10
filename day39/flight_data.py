class FlightData:
    """This class is responsible for structuring the flight data."""
    def __init__(self,origin,destination,airline,depart_at,return_at,expire_at,price,flight_number):
        self.origin = origin
        self.destination = destination
        self.airline = airline
        self.depart_at = depart_at
        self.return_at = return_at
        self.expire_at = expire_at
        self.price = price
        self.flight_number = flight_number
        self.depart_date,self.depart_time = self.depart_at.split('T')
        self.return_date,self.return_time = self.return_at.split('T')