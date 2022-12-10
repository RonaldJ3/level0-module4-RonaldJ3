"""
Use boolean variables to control program logic between two different code
paths.
"""
import turtle

if __name__ == '__main__':
    # TODO)
    #  1. Use a boolean variable to indicate if it is the weekend.
    #     Display a different message to the user depending on whether it is
    #     the weekend or not.
    isWeekend = False

    if isWeekend == False :
        print("it's the weekend")
    if isWeekend == True :
        print("it's not the Weekend")


    #TODO)
    #  2. Use a boolean variable to indicate if a student passed an exam.
    #     Display a different message to the user depending on whether they
    #     passed or not.
    result = True

    if result == False:
        print("You failed")
    if result == True:
        print("You passed")


    # TODO)
    #  3. Use a boolean variable to indicate if a game is over. When the game
    #     is over, tell the user.
    game = True

    if game == False:
        print("The game is still going")
    if game == True:
        print("The game has ended")
    # TODO)
    #  4. Use two boolean variables, one to indicate if a shape should be red,
    #     the other to indicate if the shape is to be square. When both
    #     variables are true, use a turtle to draw a red square.
    shape = True
    color = True

    if shape and color == True :
        turtle.pencolor("red")
        turtle.pendown()
        turtle.forward(50)
        turtle.left(-90)
        turtle.forward(50)
        turtle.left(-90)
        turtle.forward(50)
        turtle.left(-90)
        turtle.forward(50)
        turtle.begin_fill()
    turtle.exitonclick()



    pass
