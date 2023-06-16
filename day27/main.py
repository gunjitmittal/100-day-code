from tkinter import *


def convert():
    miles = float(entry.get())
    km = round(1.61 * miles, 3)
    label2 = Label(text=f"{km}")
    label2.grid(column=1, row=1)


window = Tk()
window.title("Mile to Km converter")
window.minsize(width=250, height=100)
window.config(padx=20, pady=20)

label = Label(text="is equal to")
label.grid(column=0, row=1)

label1 = Label(text="Miles")
label1.grid(column=2, row=0)

label2 = Label(text="Km")
label2.grid(column=2, row=1)

entry = Entry(width=10)
entry.grid(column=1, row=0)

button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

window.mainloop()
