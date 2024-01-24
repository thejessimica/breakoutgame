from turtle import Screen
from blocks import Block
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)


number_of_squares = 10
spacer = -400


for _ in range(number_of_squares):
    time.sleep(1)
    screen.update()
    block = Block((spacer, 280))
    spacer += 120
    screen.update()



screen.listen()

screen.exitonclick()