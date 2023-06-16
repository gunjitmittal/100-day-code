from random import choice
from tkinter import *
import pandas
BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv("filename.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}
timer = NONE


def flip_card(word):
    canvas_main.itemconfig(title_text, text="English", fill="white")
    canvas_main.itemconfig(word_text, text=word, fill="white")
    canvas_main.itemconfig(canvas_image, image=back)


def wrong_button_pressed():
    global timer
    window.after_cancel(timer)
    word = choice(to_learn)
    canvas_main.itemconfig(canvas_image, image=front)
    canvas_main.itemconfig(title_text, text="French", fill="black")
    canvas_main.itemconfig(word_text, text=word["French"], fill="black")
    timer = window.after(3000, flip_card, word["English"])


def right_button_pressed():
    global timer
    window.after_cancel(timer)
    word = choice(to_learn)
    canvas_main.itemconfig(canvas_image, image=front)
    canvas_main.itemconfig(title_text, text="French", fill="black")
    canvas_main.itemconfig(word_text, text=word["French"], fill="black")
    timer = window.after(3000, flip_card, word["English"])
    to_learn.remove(word)


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas_main = Canvas(width=800, height=526, bg=BACKGROUND_COLOR,
                     highlightthickness=0)
front = PhotoImage(file="images/card_front.png")
back = PhotoImage(file="images/card_back.png")
canvas_image = canvas_main.create_image(400, 264, image=front)
title_text = canvas_main.create_text(400, 150, text="Title",
                                     font=("Ariel", 40, "italic"),
                                     fill="black")
word_text = canvas_main.create_text(400, 263, text="Word",
                                    font=("Ariel", 60, "bold"), fill="black")
canvas_main.grid(column=0, row=0, columnspan=2)

right = PhotoImage(file="images/right.png")
button_right = Button(image=right, highlightbackground=BACKGROUND_COLOR,
                      command=right_button_pressed)
button_right.grid(column=0, row=1)

wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong, highlightbackground=BACKGROUND_COLOR,
                      command=wrong_button_pressed)
button_wrong.grid(column=1, row=1)

wrong_button_pressed()

window.mainloop()
new_data = pandas.DataFrame(to_learn)
new_data.to_csv("data/words_to_learn.csv", index=False)
