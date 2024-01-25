from turtle import Screen
from blocks import Block
from paddle import Paddle
from ball import Ball
import pygame
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)
screen.listen()

tolerance_x = 66
tolerance_y = 21

number_of_squares = 10

all_blocks = []

ball = Ball()
paddle = Paddle()

screen.onkeypress(paddle.go_left, "Left")
screen.onkeypress(paddle.go_right, "Right")
screen.onkeypress(paddle.go_left, "a")
screen.onkeypress(paddle.go_right, "d")

# Initialize Pygame and mixer
pygame.init()
pygame.mixer.init()

boop_sfx = pygame.mixer.Sound("sounds/Boop.wav")


def play_boop():
    # Play the sound
    channel = pygame.mixer.find_channel()
    channel.play(boop_sfx)


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


game_on = True

refresh_blocks()

while game_on:
    # screen.onscreenclick(delete_block)
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    # Detect collision with wall
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    if ball.ycor() > 280:
        ball.bounce_y()

    if ball.ycor() < -290:
        ball.reset_position()
        refresh_blocks()

    # Detect collision with paddles
    if ball.distance(paddle) < 70 and ball.ycor() < -250:
        ball.bounce_y()

    for block in all_blocks:
        ball_coords = ball.pos()
        block_coords = tuple(block.pos())
        # print(block_coords)

        # Check if the differences between corresponding coordinates are within the tolerances
        if abs(block_coords[0] - ball_coords[0]) < tolerance_x and abs(block_coords[1] - ball_coords[1]) < tolerance_y:
            play_boop()
            block.goto(-1000, 1000)
            # ball.move_speed = ball.move_speed * 0.9
            ball.bounce_y()


screen.mainloop()