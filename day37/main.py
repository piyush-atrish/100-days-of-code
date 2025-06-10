#===================================day37============================================

import requests
import datetime as dt

pixela='https://your_pixela_id'
TOKEN= 'Pixela@your_token'
USERNAME = 'username'
GRAPH_ID = 'id'

today = dt.datetime.now()
date = today.strftime('%Y%m%d')

details={'token' : TOKEN ,
         'username' : USERNAME,
         'agreeTermsOfService' : 'yes',
         'notMinor' : 'yes'}

# response = requests.post(url=pixela, json=details)
# print(response.text)

graph_url = f'{pixela}/{USERNAME}/graphs'
pixel_url = f"{pixela}/{USERNAME}/graphs/{GRAPH_ID}"
update_url = f'{pixel_url}/{date}'
#Header:
# A request header is an HTTP header that can be used in an HTTP request to provide information about the request context,
# so that the server can tailor the response. For example, the Accept-* headers indicate the allowed and preferred formats
# of the response. Other headers can be used to supply authentication credentials (e.g. Authorization), to control caching,
# or to get information about the user agent or referrer, etc.

graph_params={'id' : GRAPH_ID,
              'name' : 'coding graph',
              'unit' : 'hours',
              'type' : 'float',
              'color' : 'ajisai'}

headers = {'X-USER-TOKEN' : TOKEN}

pixel_params={ "date" : date,
              'quantity' : input('how many hours you code today?\n')}

response = requests.post(url=pixel_url, json=pixel_params, headers=headers)
print(response.text)