from twilio.rest import Client
from flight_data import FlightData

account_sid = 'sid'
auth_token = 'token'

class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_message(self,flight:FlightData):
        message = (f'\nLow price alert!!\n'
                   f'fly from {flight.origin} to {flight.destination}\n'
                   f'at price of only {flight.price}\n'
                   f'by airline: {flight.airline},departing on {flight.depart_date} at {flight.depart_time}'
                   f'returning on {flight.return_date} at {flight.return_time}'
                   f'expiring on {flight.expire_at}')

        self.client.messages.create(
            from_='number',
            to='your number',
            body = message
        )