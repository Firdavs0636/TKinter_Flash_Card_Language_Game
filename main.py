from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

font = ('Ariel', 40, 'bold')

# ---------------------------- UI SETUP ------------------------------- #
# Window Setup
window = Tk()
window.title("Flash Card Game")
window.config(padx=50, pady=50)

# Canvas, Photo Setup
canvas = Canvas(width=800, height=626, highlightthickness=0)
image1 = PhotoImage(file='./images/card_front.png')
canvas.create_image(400, 312, image=image1)
canvas.grid(column=1, row=0)




window.mainloop()

