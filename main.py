from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- UI SETUP ------------------------------- #
# Window Setup
window = Tk()
window.title("Flash Card Game")
window.config(padx=50, pady=50)

# Canvas, Photo Setup
canvas = Canvas(width=800, height=550, highlightthickness=0)
image1 = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 312, image=image1)
canvas.grid(column=1, row=0)

# Buttons
correct_image = PhotoImage(file='./images/right.png')
correct_bt = Button(image=correct_image, highlightthickness=0).grid(column=0, row=1)

wrong_image = PhotoImage(file='./images/wrong.png')
wrong_bt = Button(image=wrong_image, highlightthickness=0).grid(column=1, row=1)

# Labels
title_label = Label(text="English", font=("Ariel", 40, "italic"))
title_label.place(x=400, y=150)

word_label = Label(text="Espaniola", font=("Ariel", 60, "bold"))
word_label.place(x=400, y=263)



window.mainloop()

