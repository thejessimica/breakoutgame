from turtle import Screen
from blocks import Block
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)


number_of_squares = 10


def create_row(num, height, color, offset):
    spacer = -600 + offset
    all_blocks = []
    for _ in range(num):
        # time.sleep(0.1)
        screen.update()
        block_name = f"Block_{color}_{_}"
        block = Block((spacer, height), color, block_name)
        all_blocks.append(block)
        spacer += 120
        screen.update()
        print(block_name)


def refresh_blocks():
    create_row(10, 280, "red", 0)
    create_row(10, 250, "orange", 10)
    create_row(10, 220, "yellow", 40)
    create_row(10, 190, "green", 80)
    create_row(10, 160, "blue", 120)
    create_row(10, 130, "purple", 160)


def get_mouse_click_coor(x, y):
    x_coord = x
    y_coord = y
    print(x_coord, y_coord)
    screen.update()


screen.onscreenclick(get_mouse_click_coor)


refresh_blocks()

screen.update()


screen.listen()


# screen.onclick(delete_block)

screen.mainloop()
# screen.exitonclick()