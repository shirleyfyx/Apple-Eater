from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 60
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Snake:
    pass

class Food:
    pass

def next_turn():
    pass

def change_direction(new_direction):
    pass

def check_collisions():
    pass

def game_over():
    pass

window = Tk()
window.title("APPLE EATER")
window.resizable(True, True)

score = 0
dirction = 'down'

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

Canvas = Canvas(window, bg=BACKGROUND_COLOR, height = GAME_HEIGHT, width = GAME_WIDTH)
Canvas.pack()

window.mainloop()   