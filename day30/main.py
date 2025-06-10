#==================================day30=====================================

#Exception Handling

# try:                                        # TRY: something that might show error
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:                   # EXCEPT: do this if error occurred
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:            #grab the error message
#     print(f"The key {error_message} does not exist.")
# else:                                       # ELSE: do this only if no error is found
#     content = file.read()
#     print(content)
# finally:                                    # FINALLY:  do this no matter what
#     raise TypeError("This is an error that I made up.")   # RAISE: raise our own error
#
# #BMI Example
#
# height = float(input("Height: "))
# weight = int(input("Weight: "))
# if height > 3:
#     raise ValueError("Human Height should not be over 3 meters.")
#
# bmi = weight / height ** 2
# print(bmi)

#-----------------------------------------------------------------------------------------------
# JavaScript Object Notation (JSON) is a text-based format
# for storing and exchanging data that's both human-readable and machine-parsable
#------------------------------------------------------------------------------------------------


#=====================================day29=========================================
from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    generated_password=password_letters + password_symbols + password_numbers
    shuffle(generated_password)
    generated_password = ''.join(generated_password)
    password.delete(0, END)
    password.insert(0, generated_password)
    pyperclip.copy(generated_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name=website.get()
    email_name=email.get()
    password_name=password.get()
    data = {website_name : {'email':email_name,'password': password_name}}
    if len(website_name) == 0 or len(email_name) == 0 or len(password_name) == 0:
        messagebox.showerror(title="Error", message="Please fill all fields")
        return

    is_ok=messagebox.askyesno(title=website_name,message=f"these are the details entered:\n"
                                                         f"Email:{email_name}\nPassword:{password_name}\n"
                                                         f"is it ok to save?")
    if is_ok:
        try:
            with open('data.json','r') as file_data:
                    old_data = json.load(file_data)
        except FileNotFoundError:
            with open('data.json', 'w') as new_file:
                json.dump(data,fp=new_file,indent=4)
        else:
             old_data.update(data)
             with open('data.json', 'w') as file_data:
                    json.dump(old_data,fp=file_data,indent=4)
        finally:
                website.delete(0, END)
                email.delete(0, END)
                password.delete(0, END)

#------------------------ SEARCH ---------------------------------------#
def search():
    website_name=website.get()
    try:
        with open('data.json', 'r') as file_data:
            data = json.load(file_data)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
    #     try:
    #         details=data[website_name]
    #         messagebox.showinfo(title=website_name,message=f'Email:{details['email']}\nPassword:{details['password']}\n')
    #     except KeyError:
    #         messagebox.showerror(title="Error", message="No Data Found")

    #if we can use if-else in a situation we should prefer using it over exception handling

        if website_name in data:
            email=data[website_name]['email']
            password=data[website_name]['password']
            messagebox.showinfo(title=website_name,message=f'Email:{email}\nPassword:{password}\n')
        else:
            messagebox.showerror(title="Error", message=f"No Details about {website_name} Found")
# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title('Password Manager')
window.config(padx=50,pady=50)

canvas=Canvas(window,width=200,height=200,highlightthickness=0)
logo=PhotoImage(file='logo.png')
canvas.create_image(100,100,image=logo)
canvas.grid(row=0,column=1)

#labels
label1=Label(text="Website:")
label1.grid(row=1,column=0)
label2=Label(text="Email/Username:")
label2.grid(row=2,column=0)
label3=Label(text="Password:")
label3.grid(row=3,column=0)

#entries
website=Entry(width=21)
website.grid(row=1,column=1,columnspan=2,sticky='w')
website.focus()
email=Entry(width=36)
email.grid(row=2,column=1,columnspan=2,sticky='w')
email.insert(END,'@gmail.com')
password=Entry(width=21)
password.grid(row=3,column=1,sticky='w')

#buttonns
generate_button=Button(text="Generate Password",width=14,command=generate_password)
generate_button.grid(row=3,column=1,sticky='e')
add_button=Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)
search_button=Button(text="Search",width=12,command=search)
search_button.grid(row=1,column=1,sticky='e')

window.mainloop()
