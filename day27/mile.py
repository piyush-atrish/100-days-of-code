from tkinter import *

def mile_to_km():
    output = 1.60934 * float(input.get())
    km.config(text=round(output, 2))

window = Tk()
window.minsize(400,300)
window.title('Mile To Km converter')
window.configure(padx=50, pady=50)

input=Entry(width=20)
input.grid(row=0, column=1)

label=Label(text="Mile")
label.config(padx=10, pady=10)
label.grid(row=0, column=2)

label2=Label(text="is equal to")
label2.grid(row=1, column=0)

km=Label(text=0)
km.grid(row=1, column=1)

label3=Label(text="km")
label3.grid(row=1, column=2)

convert=Button(text="Convert",command=mile_to_km)
convert.grid(row=2, column=1)

window.mainloop()