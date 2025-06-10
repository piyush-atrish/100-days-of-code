##################### Extra Hard Starting Project ######################

import pandas,smtplib
import datetime as dt
from random import randint

my_email = 'youremail@gmail.com'
password = 'your password'

# 1. Update the birthdays.csv

data=pandas.read_csv('birthdays.csv')

# 2. Check if today matches a birthday in the birthdays.csv

now=dt.datetime.now()
day=now.day
month=now.month
is_birthday=False
email=''
name=''

birthday=data[data['day']==day & data['month']==month]
if birthday.month.iloc[0]==month:
     email=birthday.email.iloc[0]
     name=birthday.name.iloc[0]
     is_birthday=True

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

letter=f'letter_templates/letter_{randint(1,3)}.txt'
with open(letter,'r') as f:
    wish=f.read()
    wish=wish.replace('[NAME]',name)

# 4. Send the letter generated in step 3 to that person's email address.

with smtplib.SMTP('smtp.gmail.com',587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=email,
                            msg=f"Subject:Happy birthday\n\n{wish}")


#------------------------------ Anjela's approach -----------------------------------

# today = datetime.now()
# today_tuple = (today.month, today.day)
#
# data = pandas.read_csv("birthdays.csv")
# birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# if today_tuple in birthdays_dict:
#     birthday_person = birthdays_dict[today_tuple]
#     file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
#     with open(file_path) as letter_file:
#         contents = letter_file.read()
#         contents = contents.replace("[NAME]", birthday_person["name"])
#
#     with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=birthday_person["email"],
#             msg=f"Subject:Happy Birthday!\n\n{contents}"

