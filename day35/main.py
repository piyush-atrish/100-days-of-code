#=======================================DAY35==================================================
import os

#API Key: An API key is a unique identifier that authenticates and authorizes a user,
# developer, or program to access an API (application programming interface).
# API keys are typically alphanumeric strings that are generated on the project that is making the call

import  requests

API_KEY='your api key comes here'
MY_LAT= 'enterr your latitude'
MY_LONG= 'enter your longitude'
parameters={'lat' : MY_LAT,
            'lon' : MY_LONG,
            'appid' : API_KEY
            }

response= requests.get('https://api.openweathermap.org/data/2.5/weather', params=parameters)
response.raise_for_status()
data = response.json()
print(data)


# Environment variables
# are key-value pairs that can be configured outside of source code to affect how a computer's running processes behave:
# Purpose
# Environment variables can be used to:
# Customize a service's runtime behavior for different environments
# Protect secret credentials from being committed to an application's source

# we can export any valur to environment variable by writing this in terminal:
# export variable_name=value [enter] and in next line of terminal type
# env [enter]
#
# you can access the variable by importing os and
# typing os.environ['variable_name']