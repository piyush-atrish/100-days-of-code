#=========================================day28===============================================

from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep=0
work_sessions=''
time=None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global rep,work_sessions
    window.after_cancel(time)
    label1.config(text='Timer',fg=GREEN)
    rep=0
    work_sessions=''
    canvas.itemconfig(timer,text="00:00")
    done.config(text=work_sessions)

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global rep, work_sessions
    rep += 1
    work=WORK_MIN * 60
    shortBreak=SHORT_BREAK_MIN * 60
    longBreak=LONG_BREAK_MIN * 60

    if rep%8==0:
        label1.config(text="Break", fg=RED)
        countdown(longBreak)
    elif rep%2==0:
        label1.config(text="Break", fg=PINK)
        countdown(shortBreak)
    else:
        label1.config(text="Work",fg=GREEN)
        work_sessions+='✔'
        countdown(work)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(n):
    minutes = math.floor(n / 60)
    seconds = n % 60
    if seconds < 10:
        seconds = f'0{seconds}' #------------------> Dynamic typing : Dynamic typing is a programming language feature that
                                                                         # assigns variables a type based on the variable's value at runtime.
                                                                         # This is different from static typing, where type checking occurs at compile time
    canvas.itemconfig(timer, text=f"{minutes}:{seconds}")
    if n>=0:
        global time
        time=window.after(1000, countdown, n-1)
    else:
        done.config(text=work_sessions)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato=PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer=canvas.create_text(100,130,text='00:00',fill='white',font=(FONT_NAME,35,'bold'))
canvas.grid(column=1, row=1)

label1=Label(text='Timer',font=(FONT_NAME,40),bg=YELLOW,fg=GREEN)
label1.grid(column=1, row=0)

start=Button(text='Start',command=start_timer)
start.grid(column=0, row=2)

reset=Button(text='Reset',command=reset_timer)
reset.grid(column=2, row=2)

done=Label(bg=YELLOW,fg=GREEN,highlightthickness=0)
done.grid(column=1, row=3)


window.mainloop()
