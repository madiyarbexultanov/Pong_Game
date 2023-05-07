from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position)
        self.setheading(90)
        self.shapesize(1, 5)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)





