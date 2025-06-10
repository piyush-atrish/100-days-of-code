#========================================day32=============================================

# SMTP:
# SMTP stands for Simple Mail Transfer Protocol, which is a communication protocol used
# to send and receive emails over the internet. It's a technical standard that allows computers
# and servers to exchange data, regardless of their hardware or software
#----------------------------------------------------------------------------------------------

# import smtplib
#
# my_email = 'youremail@gmail.com'
# password = 'your password'
#
# connection = smtplib.SMTP('smtp.gmail.com')
# connection.starttls()
# #TLS, or Transport Layer Security,
# # is a protocol that encrypts data sent over the internet to prevent unauthorized access:
#
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs='', msg='hello!!')
# connection.close()
#
# #other way to avoid closing connection and adding subject:
#
# with smtplib.SMTP('smtp.gmail.com') as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email
#                         ,to_addrs='some.email@yahoo.com',
#                         msg='Subject:hey\n\n'
#                         'how are you?')


# import datetime as dt
#
# now=dt.datetime.now()
# year=now.year
# month=now.month
# day=now.day
# weekday=now.weekday()+1 #starts from 0
# print(now)
# print(year)
# print(month)
# print(day)
# print(weekday)
# print('')
#
# date_of_birth=dt.datetime(year=2003,month=3,day=19)
# print(date_of_birth)

import smtplib
import datetime as dt
import random

my_email = 'your.email@gmail.com'
password = 'your password'
now = dt.datetime.now()
day=now.weekday()

if day == 0:
    with open('quotes.txt','r') as file:
            quotes = file.readlines()
            print(quotes)
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="email@yahoo.com",
                            msg=f"Subject:Quotes\n\n{random.choice(quotes)}")