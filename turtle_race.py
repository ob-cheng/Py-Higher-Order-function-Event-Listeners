from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
game_on = False

# tim = Turtle(shape="turtle")
# tim.penup()
# tim.goto(-230, -100)

# Create six turtles
initial_y = -100
ini_color = 0
for item in colors:
    item = Turtle(shape='turtle')
    item.color(colors[ini_color])
    ini_color += 1
    item.penup()
    item.goto(x = -230, y = initial_y)
    initial_y += 33.3
    all_turtles.append(item)

print(all_turtles)
if user_input:
    game_on = True

while game_on:
    for obj in all_turtles:
        move_distance = random.randint(0,10)
        obj.forward(move_distance)
        # print(obj.xcor())

        if obj.xcor() >= 230:
            game_on = False
            winner = obj.pencolor()

if user_input == winner:
    print("You won")
else:
    print("you lose")

# screen.exitonclick()