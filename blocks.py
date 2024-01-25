from turtle import Turtle


class Block(Turtle):

    def __init__(self, position, color, name):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(position)
        self.name = name

    def delete_block(self, x, y):
        self.clear()
        self.hideturtle()
