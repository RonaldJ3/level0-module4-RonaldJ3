"""
The player of the game has to click the mouse where the donkey's
tail will go. The problem is, the picture keeps disappearing!
"""

def setup():
    size(800, 600)
    
    global donkey
    donkey = loadImage('donkey.jpg')
    donkey.resize(width, height)
    
    global tail
    tail = loadImage('tail.png')
    
    global x
    global y
    x = mouseX
    y = mouseY
    global b
    b = False
    noStroke()



def draw():
    global x
    global y
    global b
    # 1. Use the background() function to draw the donkey
    background(donkey)
    # 2. Use the rect() function to draw a box in the upper left
    # corner of the screen:
    # rect(0, 0, 30, 30)
    rect(0,0,30,30)
    # 3. Now find the x and y coordinates where the tail attaches
    # to the donkey and draw another box with a side of 50
    #print(mouseX,mouseY)
    rect(686,129,30,50)
    # 4. Change your code so the donkey is only shown when the
    # mouse is inside the corner bounding box.
    #
    # Hint: check if mouseX is greater than 0 and less than 30
    # and y is greater than 0 and less than 30
    if mouseX > 30:
        background(0)
    if mouseX < 0:
        background(0)
    if mouseY > 30:
        background(0)
    if mouseY < 0:
        background(0)

    # 5. Check that when the mouse is outside the corner box,
    # you should show a solid color background.

    # 6. Use the image() method to draw the tail at the mouseX
    # and mouseY location. For example,
    # image(tail, mouseX, mouseY)

    # 7. Now, adjust your code so the tail sticks when you click the
    # mouse (this means it will no longer move when the mouse moves)
    #
    # Hint: you will need to use the mousePressed variable and set the
    # x and y variables declared in setup()
    if mousePressed == 0 and not b:
        x = mouseX
        y = mouseY
    if mousePressed == 1:
        b = True
    image(tail, x, y)
    # 8. When the tail has been pinned, write code to check if the
    # tail was pinned inside the target bounding box.
    if x >= 686 and x <= 686 + 50 and y >= 129 and y <= 129 + 50 and mousePressed == 1:
        print("you pinned the tail on the donkey")
    elif mousePressed == 1:
        print("You pinned the tail ")