import tkinter
from PIL import Image, ImageTk
import random


root = tkinter.Tk()
root.title("Dice Rolling")
root.geometry("400x400")

BlankLine = tkinter.Label(root, text="")
BlankLine.pack()

HeadeingLabel = tkinter.Label(root, text="Dice Rolling", font="araial 20 bold", fg="green", bg="black")
HeadeingLabel.pack()

dice = ["die1.png", "die2.png", "die3.png", "die4.png", "die5.png", "die6.png"]
DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

ImageLabel = tkinter.Label(root, image=DiceImage)
ImageLabel.image = DiceImage

ImageLabel.pack(expand=True)


def rolling_dice():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    ImageLabel.configure(image=DiceImage)
    ImageLabel.image = DiceImage


Button = tkinter.Button(root, text="Roll the Dice", font="araial 15 bold", bg="black", fg="red", command=rolling_dice)
Button.pack(expand=True)





root.mainloop()
