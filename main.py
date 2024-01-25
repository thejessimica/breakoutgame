from turtle import Screen
from blocks import Block
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

tolerance_x = 51
tolerance_y = 11

number_of_squares = 10
all_blocks = []


def create_row(num, height, color, offset):
    spacer = -600 + offset
    for _ in range(num):
        # time.sleep(0.2)
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


def delete_block(x, y):
    x_coord = x
    y_coord = y
    click_coords = (x_coord, y_coord)
    # print(click_coords)

    for block in all_blocks:
        block_coords = tuple(block.pos())
        # print(block_coords)

        # Check if the differences between corresponding coordinates are within the tolerances
        if abs(block_coords[0] - click_coords[0]) < tolerance_x and abs(block_coords[1] - click_coords[1]) < tolerance_y:
            block.goto(-1000, 1000)

    screen.update()


screen.onscreenclick(delete_block)


refresh_blocks()

screen.update()

print(all_blocks)
print(all_blocks[0].pos())
all_blocks[0].goto(-1000, 1000)
screen.update()

screen.listen()


# screen.onclick(delete_block)

screen.mainloop()
# screen.exitonclick()