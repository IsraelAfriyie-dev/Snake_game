from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.colormode(255)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

easy_or_hard = screen.textinput(title="Select Difficulty Level",
                                prompt="Do you want an easy game or a hard game? Type 'Hard' or 'Easy': ").lower()

while easy_or_hard != "easy" and easy_or_hard != "hard":
    print("UNEXPECTED INPUT")
    easy_or_hard = screen.textinput(title="Select Difficulty Level",
                                    prompt="Do you want an easy game or a hard game? Type 'Hard' or 'Easy': ").lower()

print(easy_or_hard)

snake = Snake()

screen.listen()

food = Food()

score = 0

display = Scoreboard()

screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 16:
        score += 1
        print(f"Score: {score}")
        snake.extend()
        display.increase_score()
        food.refresh()

    #Detect collision with wall
    if easy_or_hard == "hard":
        snake.draw_wall()
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            display.game_over()
            game_is_on = False
            print("GAME OVER")
    else:
        if snake.head.xcor() > 290:
            snake.head.goto(-290, snake.head.ycor())

        if snake.head.xcor() < -290:
            snake.head.goto(290, snake.head.ycor())

        if snake.head.ycor() > 290:
            snake.head.goto(snake.head.xcor(), -290)

        if snake.head.ycor() < -290:
            snake.head.goto(snake.head.xcor(), 290)

    # Detect collision with tail.
    # if head collides with any segment in the tail, trigger game over.
    if snake.collision_with_tail():
        display.game_over()
        game_is_on = False
        print("GAME OVER")







screen.exitonclick()
