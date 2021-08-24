from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

'''Create a black screen for snake to run'''
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game BY Jaydip")
screen.tracer(0)

'''make snake appear on board'''

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

'''move snake'''
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.07)
    snake.move()
    # detacts collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detacts collison with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        scoreboard.reset_score()
        snake.reset()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset()
    # if head head collides anywhere to the body then game over

screen.exitonclick()
