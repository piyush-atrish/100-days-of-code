#============================================Day38===============================================

# Natural language processing (NLP) is a machine learning technology that gives computers
# the ability to interpret, manipulate, and comprehend human language.

import requests
import datetime as dt


API_KEY = 'your key'
API_ID = 'your id'
SHEET_BASIC_AUTH = ''
url = ''
sheet_url=''

headers = {"x-app-id" : API_ID,
           "x-app-key" : API_KEY,
           "Content-Type": "application/json"}

today = dt.datetime.today()
date = today.strftime('%d/%m/%y')
time = today.strftime('%H:%M:%S')

query = input('Enter what exercise you did?\n')

parameters = {'query' : query,
              'weight_kg' : 70,
              'height_cm' : 179,
              'age' : 21}

try:
    response = requests.post(url, json=parameters, headers=headers)
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")
    print("Response Text:", response.text)
except Exception as e:
    print(f"An error occurred: {e}")

data = response.json()['exercises']

headers_sheet = {
    "Content-Type": "application/json",
    "Authorization": SHEET_BASIC_AUTH
}
for data in data:
    sheet_json = { 'workout' : {
        'date' : date,                  #the server camel cased the keys
        'time' : time,
        'exercise' : data['name'],
        'duration' : f'{data['duration_min']} min',
        'calories' : data['nf_calories']
    }}

    response = requests.post(sheet_url, json=sheet_json, headers=headers_sheet)
    response.raise_for_status()
    print(response.text)