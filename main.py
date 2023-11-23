from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Bet on a Turtle",
                            prompt="Type the color of the turtle that you think will win.").lower()

color = ["red", "blue", "purple", "orange", "yellow", "green"]

turtle_1 = Turtle(shape="turtle")
turtle_1.color("red")
turtle_1.penup()
turtle_1.goto(x=-230, y=75)

turtle_2 = Turtle(shape="turtle")
turtle_2.color("blue")
turtle_2.penup()
turtle_2.goto(x=-230, y=45)

turtle_3 = Turtle(shape="turtle")
turtle_3.color("purple")
turtle_3.penup()
turtle_3.goto(x=-230, y=15)

turtle_4 = Turtle(shape="turtle")
turtle_4.color("orange")
turtle_4.penup()
turtle_4.goto(x=-230, y=-15)

turtle_5 = Turtle(shape="turtle")
turtle_5.color("yellow")
turtle_5.penup()
turtle_5.goto(x=-230, y=-45)

turtle_6 = Turtle(shape="turtle")
turtle_6.color("green")
turtle_6.penup()
turtle_6.goto(x=-230, y=-75)

competitors = [turtle_1, turtle_2, turtle_3, turtle_4, turtle_5, turtle_6]
is_race_on = True

while is_race_on:
    turtle_1.forward(random.randint(0, 10))
    turtle_2.forward(random.randint(0, 10))
    turtle_3.forward(random.randint(0, 10))
    turtle_4.forward(random.randint(0, 10))
    turtle_5.forward(random.randint(0, 10))
    turtle_6.forward(random.randint(0, 10))

    for turtle in competitors:
        if turtle.xcor() >= 230:
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"Congratulations! {winning_color} is the winner.")
            else:
                print(f"You lose! {winning_color} is the winner.")
            is_race_on = False
            break

screen.exitonclick()
