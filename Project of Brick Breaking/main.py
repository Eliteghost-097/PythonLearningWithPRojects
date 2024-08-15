from ball import Ball
from brick import BrickMaker
from rod import omarrod
import turtle


turtle.tracer(0)


b = BrickMaker()
bricks = b.new_design()


rod = omarrod()
turtle.listen() 
turtle.onkeypress(rod.move_right, "Right")
turtle.onkeypress(rod.move_left, "Left")


ball = Ball(-300,0,1)
while True:
    ball.move()
    if ball.y_pos <-300 :
        turtle.write("Game Over", align="center", font=("Arial", 30, "normal"))
    if ball.distance(rod) < 50:
        ball.bounce()


    for brick in bricks:
        if ball.distance(brick) < 50:
            ball.bounce()
            brick.hideturtle()
            bricks.remove(brick)



    turtle.update()
    



turtle.mainloop()

