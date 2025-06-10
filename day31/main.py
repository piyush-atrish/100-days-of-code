#==========================================day31======================================

from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
data_dict={}
card={}
try:
    data=pandas.read_csv("data/to_learn.csv")
except FileNotFoundError:
    OGdata=pandas.read_csv("data/Book1.csv")
    data_dict = OGdata.to_dict(orient="records")
else:
    data_dict=data.to_dict(orient="records")

#----------------------------remove words-------------------------------------------
def know_this_word():
    data_dict.remove(card)
    to_lear=pandas.DataFrame(data_dict)
    to_lear.to_csv('data/to_learn.csv', index=False)
    next_card()
#---------------------------- flip card----------------------------------------------
def flip_card():
    canvas.itemconfig(image,image=back)
    canvas.itemconfig(word,text=card['ENGLISH'],fill='white')
    canvas.itemconfig(title,text='English',fill='white')

#--------------------------next card--------------------------------------------------
def next_card():
    global card,time
    window.after_cancel(time)
    canvas.itemconfig(image, image=front)
    card=random.choice(data_dict)
    canvas.itemconfig(word,text=card["GERMAN"],fill='black')
    canvas.itemconfig(title,text='German',fill='black')
    time=window.after(3000,flip_card)

#---------------------------- UI -------------------------------------------------------

window = Tk()
window.title('Flashy')
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
time=window.after(3000,flip_card)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR,highlightthickness=0)
front=PhotoImage(file="./images/card_front.png")
back=PhotoImage(file="./images/card_back.png")
image=canvas.create_image(400,263, image=front)
word=canvas.create_text(400,263,text='WORD',font=('Ariel',60,'bold'))
title=canvas.create_text(400,150,text='title',font=('Ariel',40,'italic'))
canvas.grid(row=0, column=0,columnspan=2)

wrong_image=PhotoImage(file="./images/wrong.png")
wrong_button=Button(image=wrong_image,highlightthickness=0,bg=BACKGROUND_COLOR,command=next_card)
wrong_button.grid(row=1, column=0)

right_image=PhotoImage(file="./images/right.png")
right_button=Button(image=right_image,highlightthickness=0,bg=BACKGROUND_COLOR,command=know_this_word)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()