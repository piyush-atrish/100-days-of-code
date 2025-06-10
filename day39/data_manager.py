import requests

class DataManager:
    """This class is responsible for talking to the Google Sheet."""
    def __init__(self):
        self.url='sheety url'
        self.destination_data=[]

    def get_data(self):

        response = requests.get(self.url)
        response.raise_for_status()

        return response.json()['prices']

    def update(self,text):
        for city in self.destination_data:
            new_data = {
                "price": {
                    text: city[text]
                }
            }
            response = requests.put(
                url=f"{self.url}/{city['id']}",
                json=new_data
            )
            print(response.text)
