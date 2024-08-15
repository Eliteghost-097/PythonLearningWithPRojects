import turtle

class Ball(turtle.Turtle):
    def __init__(self,x_pos,y_pos,speed):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(0)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.goto(self.x_pos, self.y_pos)
        self.speedx = speed
        self.speedy = speed

    def move(self):
        self.x_pos += self.speedx
        self.y_pos += self.speedy
        self.goto(self.x_pos, self.y_pos)

        if self.y_pos > 290:
            self.bounce()

        if self.x_pos > 350 or self.x_pos < -350:
            self.bounce_x()
        print('speedx',self.speedx,'speedy',self.speedy)
        print('x_pos',self.x_pos,'y_pos',self.y_pos)

    def bounce(self):
        self.speedy = -1 * self.speedy
    def bounce_x(self):
        self.speedx = -1 * self.speedx


    
