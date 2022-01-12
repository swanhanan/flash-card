
from tkinter import *
from random import choice
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn={}

# read csv file
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    current_card = choice(to_learn)
    window.after_cancel(flip_timer)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=f"{current_card['French']}", fill="black")
    canvas.itemconfig(im, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)

# remove known names of current file
def is_known():
    to_learn.remove(current_card)
    next_card()
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    # words_unknown = pandas.to_csv(wtl, index=False)


# flip the card
def flip_card():
    canvas.itemconfig(im, image=card_back_image)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=f"{current_card['English']}", fill="white")



window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)


canvas = Canvas(width=800, height=526, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
im = canvas.create_image(400, 263, image=card_front_image)
word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(command=is_known, image=right_image, highlightthickness=0)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(command=next_card, image=wrong_image, highlightthickness=0)
wrong_button.grid(row=1, column=0)
next_card()






window.mainloop()
