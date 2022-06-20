from tkinter import *
import pandas as pd
import random
#FileNotFoundError
bg_color = "#2de0ce"
to_learn = {}
try:
    data = pd.read_csv("data/words_to_learn.csv")
except (FileNotFoundError, IndexError):
    orignal_data = pd.read_csv("data/Vocabulary.csv")
    to_learn = orignal_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
print(to_learn)

current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_tittle, text="German", fill="black")
    canvas.itemconfig(card_word, text=current_card["German"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_tittle, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img )


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    next_card()
    data.to_csv("data/words_to_learn.csv", index=False)



window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=bg_color)
flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=616)
card_front_img = PhotoImage(file="images/front - Copy.png")
card_back_img = PhotoImage(file="images/back.png")
card_background = canvas.create_image(400, 308, image=card_front_img)
card_tittle = canvas.create_text(400, 200, text="", font=("Ariel", 30, "italic"))
card_word = canvas.create_text(400, 308, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=bg_color, highlightthickness=0)
canvas.grid(row=0, rowspan=2, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)
next_card()
window.mainloop()