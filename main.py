from turtle import Turtle, Screen

ori = Turtle()
screen = Screen()

# def move_forward():
#     ori.forward(10)
#
# screen.listen()
# screen.onkey(move_forward,"space")
# screen.exitonclick()

# Make an Etch-A-Sketch App
# def move_forward():
#     ori.forward(10)
#
# def move_backward():
#     ori.backward(10)
#
# def clear_screen():
#     ori.clear()
#
# def turn_left():
#     ori.left(10)
#
# def turn_right():
#     ori.right(10)
#
# screen.listen()
# screen.onkey(move_forward, "w")
# screen.onkey(move_backward, "s")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")
# screen.onkey(clear_screen, "c")


screen.setup(width=500, height=400)

user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")



screen.exitonclick()