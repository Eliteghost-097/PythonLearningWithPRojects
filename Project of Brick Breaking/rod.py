#hitn impor tturlte make a class Rod and then defien it as quare with some leigth and width
import turtle
class  omarrod(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)
        self.shapesize(1, 6)
        self.goto(0, -270)

    def move_right(self):
        self.forward(20)

    def move_left(self):
        self.backward(20)
