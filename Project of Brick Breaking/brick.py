import turtle

class OmarBrick(turtle.Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)
        self.shapesize(1, 3)
        self.goto(x, y)

class BrickMaker():
    def __init__(self):
        pass 
    def simple_distribution(self, x_list=[], y_list=[]):
        x_list = [-300, -200, -100, 0, 100, 200, 300]
        y_list = [0,50,100,150,200,250,300]
        all_bricks = []
        for a in x_list:
            for b in y_list:
                all_bricks.append( OmarBrick(a, b))

        return all_bricks
    
    def new_design(self):
        x_list = [-300, -200,  0, 100, 200, 300]
        y_list = [100,150,175,200,300]
        all_bricks = []
        for a in x_list:
            for b in y_list:
                all_bricks.append( OmarBrick(a, b))

        return all_bricks


