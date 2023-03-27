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
    
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0,0])

        for x, y in self.coordinates:
            square = Canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food:
    
    def __init__(self):

        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE
    
        self.coordinates = [x, y]

        Canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = FOOD_COLOR, tag = "food")

def next_turn(snake, food):
    
    x , y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0,(x, y))
    #adding the snake head to the coordinate list.

    square = Canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR)

    snake.squares.insert(0, square)

    del snake.coordinates[-1]

    Canvas.delete(snake.squares[-1])

    del snake.squares[-1]

    #delete the last element of the snake from the list and canvas. 

    window.after(SPEED, next_turn, snake,food)

def change_direction(new_direction):
    
    global direction 
    # old direction


def check_collisions():
    pass

def game_over():
    pass

window = Tk()
window.title("APPLE EATER")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

Canvas = Canvas(window, bg=BACKGROUND_COLOR, height = GAME_HEIGHT, width = GAME_WIDTH)
Canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()

next_turn (snake, food)

window.mainloop()   