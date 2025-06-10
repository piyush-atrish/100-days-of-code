#=====================================day33=============================================
from logging import exception

#                         A P I

#API stands for Application Programming Interface,
# which is a set of rules and protocols that allow software applications
# to communicate with each other

#-----------------------------------------------------------------------------------------

# import requests
#
# response = requests.get('http://api.open-notify.org/iss-now.json')

# print(response)

# HTTP response status codes (or simply status codes) are three-digit codes
# issued by a server in response to a browser-side request from a client.
# These status codes serve as a means of quick and concise communication
# on how the server worked on and responded to the client's request.

# 1xx informational response – the request was received, continuing process
# 2xx successful – the request was successfully received, understood, and accepted
# 3xx redirection – further action needs to be taken in order to complete the request
# 4xx client error – the request contains bad syntax or cannot be fulfilled
# 5xx server error – the server failed to fulfil an apparently valid request


# import requests
#
# response = requests.get('http://api.open-notify.org/iss-now.json')
# response.raise_for_status()
# returns an HTTPError object if an error has occurred during the process.
# It is used for debugging the requests

# data=response.json()
# print(data)
# data=response.json()['iss_position']
# print(data)
#
# latitude = response.json()['iss_position']['latitude']
# longitude = response.json()['iss_position']['longitude']
#
# position=(latitude,longitude)
# print(position)


import requests,smtplib,time
import datetime as dt

# API Parameters are options that can be passed with the endpoint to influence the response
#https://api.sunrisesunset.io/json?lat=38.907192&lng=-77.036873
#in browser we can give arguments by separating api end point with arguments by a ? symbol
#then provide keywords following with = and separate different arguments through a & symbol

my_lat= 'your latitude'
my_long= 'your longitude'

my_email = 'your.email@gmail.com'
password = 'your password'

parameters={
    'lat': my_lat,
    'lng': my_long,
    'time_format' : 24
}

def is_dark():
    response = requests.get('https://api.sunrisesunset.io/json',params=parameters)
    response.raise_for_status()
    data = response.json()
    sunset = int(data['results']['sunset'].split(':')[0])
    sunrise = int(data['results']['sunrise'].split(':')[0])

    now = dt.datetime.now()
    hour = now.hour
    if hour < sunrise or hour > sunset:
        return True
def is_above():
    response = requests.get('http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    latitude = float(response.json()['iss_position']['latitude'])
    longitude = float(response.json()['iss_position']['longitude'])
    if my_lat+5>latitude>my_lat-5 and my_long+5>longitude>my_long-5 :
        return True

while True:
    time.sleep(60) #check for the ISS every 60 seconds until the device is on
    if is_dark() and is_above():
            try:
                with smtplib.SMTP('smtp.gmail.com',587) as connection:
                    connection.starttls()
                    connection.login(user=my_email,password=password)
                    connection.sendmail(from_addr=my_email
                                        ,to_addrs=my_email,
                                        msg="subject:LOOK UP\n\n"
                                            "the ISS is in the sky above you")
            except exception as e:
                print('error in sending the email',e)