from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE = 35
BODY_PARTS = 5
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

    if x == food.coordinates[0] and y == food.coordinates[1]:
        # snake has touched the apple. 
        global score
        score += 1
        label.config(text="Score: Eating {} Apple!".format(score))

        Canvas.delete("food")

        food = Food()

    else:
        del snake.coordinates[-1]

        Canvas.delete(snake.squares[-1])

        del snake.squares[-1]

        #delete the last element of the snake from the list and canvas. 

    if check_collisions(snake):
        game_over()
        

    else:
    
        window.after(SPEED, next_turn, snake,food)

def change_direction(new_direction):
    
    global direction 
    # old direction

    if new_direction == "left":
        if direction != 'right':
            direction = new_direction
    
    elif new_direction == "right":
        if direction != 'left':
            direction = new_direction
    
    elif new_direction == "up":
        if direction != 'down':
            direction = new_direction
    
    elif new_direction == "down":
        if direction != 'up':
            direction = new_direction


def check_collisions(snake):
    
    x, y = snake.coordinates[0]
    #index 0 represents the snake head. 

    if x < 0 or x >= GAME_WIDTH:
        print("GAME OVER")
        return True
    
    elif y < 0 or y >= GAME_HEIGHT:
        print("GAME OVER")
        return True
    
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            print("GAME OVER")
            return True    
        
    return False

def game_over():
    Canvas.delete(ALL)
    Canvas.create_text(Canvas.winfo_width()/2, Canvas.winfo_height()/2, font=('Verdana',70), text="NO APPLES!", anchor = CENTER, fill="red", tag="gameover")
    
    restart_button = Button(window, text="Restart Game", font=('Georgia', 20), command=restart_game)
    Canvas.create_window(Canvas.winfo_width()/2, Canvas.winfo_height()/2+100, anchor = CENTER, window=restart_button,tag="startover")


def restart_game():
    global score, direction, snake, food
    
    # Reset game variables
    score = 0
    direction = 'down'
    snake = Snake()
    food = Food()
    label.config(text="Score:{}".format(score))

    if Canvas.find_withtag("gameover"):
        Canvas.delete("gameover")
        Canvas.delete("startover")
    
    next_turn(snake,food)

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
