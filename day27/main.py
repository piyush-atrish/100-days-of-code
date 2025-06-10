#===================================day27======================================
#advanced python arguments

# def functions(a=1,b=2,c=3): #default arguments
#     pass
# functions()
# functions(a=3)
# functions(a=2,c=5)
# functions(5,6,7)
#
#
# def f2(*args):    #*args (arguments) allows you to pass a variable number
#     pass          # of positional arguments to a function
# f2()
# f2(1,2,3)
# f2("hello",1,2,3,4)

# #=============================Graphical user interphase==========================
# from tkinter import *
#
# window = Tk()
# window.title('My first GUI')
# window.minsize(500,300)
#
# label = Label(text='I am a Label',font=('Arial',20,'bold'))
# label.pack(expand=True)
#
# def new_text():
#     word = input.get()
#     label['text']='Hello World!'
#     label.config(text=f'Hello {word}!!')
#
# input=Entry(width=15)
# input.pack(expand=True)
#
# button=Button(text='click me',command=new_text)
# button.pack(expand=True)
#
# window.mainloop()


#=======================pack,place,grid====================================


# from tkinter import *
#
# def new_text():
#     word = input.get()
#     label.config(text=f'Hello {word}!!')
#
# window = Tk()
# window.title('My first GUI')
# window.minsize(500,300)
# window.config(padx=20, pady=20)      #add padding
#
# label = Label(text='I am a Label',font=('Arial',20,'bold'))
# label.grid(column=0,row=0)
# label.config(padx=50, pady=50)
#
# input=Entry(width=15)
# input.grid(column=3,row=2)
#
# button=Button(text='click me',command=new_text)
# button.grid(column=1,row=1)
#
# button2=Button(text='click me')
# button2.grid(column=2,row=0)
# window.mainloop()


from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

#Buttons
def action():
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()

