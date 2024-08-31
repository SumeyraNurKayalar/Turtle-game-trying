import turtle
import random


drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("turtle going brrrr")


turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")
turtle_instance.penup()


score_turtle = turtle.Turtle()
score_turtle.penup()
score_turtle.hideturtle()
score_turtle.goto(0, 260)
score = 0
score_turtle.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))


timer_turtle = turtle.Turtle()
timer_turtle.penup()
timer_turtle.hideturtle()
timer_turtle.goto(0, 230)
time_left = 20
timer_turtle.write(f"Time left: {time_left}", align="center", font=("Arial", 18, "normal"))


drawing_board.setup(width=600, height=600)

# Generate random coordinates
random_x = random.randint(-300, 300)
random_y = random.randint(-300, 300)


turtle_instance.goto(random_x, random_y)


def update_score_and_move(x, y):
    global score
    score += 1
    score_turtle.clear()
    score_turtle.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))
    random_x = random.randint(-300, 300)
    random_y = random.randint(-300, 300)
    turtle_instance.goto(random_x, random_y)


def update_timer():
    global time_left
    if time_left > 0:
        time_left -= 1
        timer_turtle.clear()
        timer_turtle.write(f"Time left: {time_left}", align="center", font=("Arial", 18, "normal"))
        drawing_board.ontimer(update_timer, 1000)
    else:
        end_game()


def end_game():
    turtle_instance.hideturtle()
    timer_turtle.clear()
    timer_turtle.write(f"Time's up! Final Score: {score}", align="center", font=("Arial", 24, "normal"))
    drawing_board.ontimer(turtle.bye, 3000)


drawing_board.ontimer(update_timer, 1000)

turtle_instance.onclick(update_score_and_move)

turtle.done()
