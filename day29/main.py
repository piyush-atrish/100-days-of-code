#=====================================day29=========================================
from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
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

    if len(website_name) == 0 or len(email_name) == 0 or len(password_name) == 0:
        messagebox.showerror(title="Error", message="Please fill all fields")
        return

    is_ok=messagebox.askyesno(title=website_name,message=f"these are the details entered:\n"
                                                         f"Email:{email_name}\nPassword:{password_name}\n"
                                                         f"is it ok to save?")
    if is_ok:
        with open('data.txt','a') as data:
            data.write(f'{website_name} | {email_name} | {password_name}\n')
            website.delete(0, END)
            email.delete(0, END)
            password.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title('Password Manager')
window.config(padx=50,pady=50)

canvas=Canvas(window,width=200,height=200,highlightthickness=0)
logo=PhotoImage(file='../day30/logo.png')
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
website=Entry(width=36)
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
window.mainloop()
