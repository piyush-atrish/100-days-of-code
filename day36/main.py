#===========================================Day36===================================

import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "your API key"
API_KEY_NEWS = 'your API key'
# recovery code = your recovery code

ACOUNT_SID= 'your sid'
AUTH_TOKEN = 'your token'
NUMBER='your number'
client = Client(ACOUNT_SID, AUTH_TOKEN)

parameters={'function' : 'TIME_SERIES_DAILY',
            'symbol' : STOCK,
            'apikey' : API_KEY,}

parameters_news = {'qInTitle' : COMPANY_NAME,
                   'apikey' : API_KEY_NEWS,
                   'language' : 'en',
                   'pageSize' : 3}

response = requests.get('https://www.alphavantage.co/query', params=parameters)
response.raise_for_status()
data=response.json()['Time Series (Daily)']
data=[float(value['4. close']) for (date,value) in data.items()]

percent = round(((data[0]-data[1])/data[1])*100)
logo='🔺'
if percent < 0:
    logo= '🔻'
if percent > 3 or percent < -3:
    response = requests.get('https://newsapi.org/v2/everything',params=parameters_news)
    response.raise_for_status()
    article=response.json()['articles']
    article=[f'\nTSLA:{percent}{logo}\nHeadline: {value['title']}\nBrief: {value['description']}' for value in article]
    for text in article:
        client.messages.create(from_=NUMBER,to='your number',body=text)


