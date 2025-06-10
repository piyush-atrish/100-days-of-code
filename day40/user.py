#===================================day40=========================================

import requests

url = 'https://api.sheety.co/KEY/users/sheet1'

def details():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    email = input('\nEnter your email: ')
    email_2 = input('Enter your email again: ')
    if email_2 == email :
        return {'sheet1':{'firstName':first_name,'lastName':last_name,'email':email}}
    else:
        print('Emails dont match!!\n\n')
        details()

print('Welcome to the Flight project registration\n\n')
data = details()

response = requests.post(url, json=data)
response.raise_for_status()

print('\n\nyou are successfully registered!\nThanks for registering!!!')