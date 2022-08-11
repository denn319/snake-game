import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# params init
scr = t.Screen()
scr.setup(width=600, height=600)
scr.listen()
scr.bgcolor("black")
scr.title("Nokia 3210 Snake Game")
scr.tracer(0)

snake = Snake()
food = Food()
board = ScoreBoard()

# listen for key press to move the snake
scr.onkey(fun=snake.up, key="Up")
scr.onkey(fun=snake.down, key="Down")
scr.onkey(fun=snake.left, key="Left")
scr.onkey(fun=snake.right, key="Right")
scr.onkey(fun=scr.bye, key="Escape")

game_on = True
while game_on:
    scr.update()
    time.sleep(snake.speed)
    snake.move()

    # detect collision between the snake and the food
    if snake.head.distance(food) < 15:
        food.new_food()
        snake.extend_body()
        board.update_score()

    # detect collision with tail
    for body_block in snake.snake_body[1:]:
        if snake.head.distance(body_block) < 10:
            # game_on = False
            # board.game_over()
            snake.reset()

# hold the screen until click exit
scr.exitonclick()
