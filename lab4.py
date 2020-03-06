'''
Estimates pi using Monte Carlo simulation

Virtual Dartboard has area 2 X 2 to accommodate unit circle
Total area is 4
Therefore, since area of unit circle = pi * radius^2 (and radius of 1 squared
  is 1), ratio of area of unit circle to area of board should be pi/4
  Theoretically, if you fill the entire board with darts, counting
  the number of darts that fall within the circle divided by the
  total number of darts thrown should give us that ratio (i.e., 1/4 * pi)
  Therefore, multiplying that result by 4 should give us an approx. of pi

Output to monitor:
  approximation of pi (float)
Output to window:
  colored dots that simulate unit circle on 2x2 square
Functions you must implement:
  drawSquare(myturtle, width, top_left_x, top_left_y) - to outline dartboard
  drawLine(myturtle, x_start, y_start, x_end, y_end) - to draw axes
  drawCircle(myturtle, radius) - to draw the circle
  setUpDartboard(myscreen, myturtle) - to set up the board using the above functions
  isInCircle(myturtle, circle_center_x, circle_center_y, radius) - determine if dot is in circle
  throwDart(myturtle)
  playDarts(myturtle) - a simulated game of darts between two players
  montePi(myturtle, num_darts) - simulation algorithm returns the approximation of pi
'''
import turtle
import random
import time

#########################################################
#                   Your Code Goes Below                #
#########################################################

def drawSquare(myturtle, width, top_left_x, top_left_y):
    """ Draw a square with a turtle """

    myturtle.up()
    myturtle.goto(top_left_x, top_left_y)
    myturtle.down()

    for i in range(4):
        myturtle.forward(width)
        myturtle.right(90)
    

def drawLine(myturtle, x_start, y_start, x_end, y_end):
    """ Draw a line with a turtle """

    myturtle.up()
    myturtle.goto(x_start, y_start)
    myturtle.down()
    myturtle.goto(x_end, y_end)

def drawCircle(myturtle, radius):
    """ Draw a circle with a turtle """

    myturtle.up()
    myturtle.goto(0, -radius)
    myturtle.down()
    myturtle.circle(1, 360, 360)

def setUpDartboard(mywindow, myturtle):
    """ Create the dartboard in a window with a turtle """

    mywindow.setworldcoordinates(-1, -1, 1, 1)
    drawSquare(myturtle, 2, -1, 1)
    drawLine(myturtle, 0, 1, 0, -1)
    drawLine(myturtle, -1, 0, 1, 0)
    drawCircle(myturtle, 1)

def isInCircle(myturtle):
    """ Determine if a turtle is in the circle radius"""

    distance = myturtle.distance(0, 0)
    return distance <= 1

def throwDart(myturtle):
    """
    Mark a random position with a turtle, signifying 'throwing a dart'
    The dart is lime colored when in the circle. Dark red otherwise.
    """
    size_of_dart = 10
    dart_x = random.uniform(-1, 1)
    dart_y = random.uniform(-1, 1)

    myturtle.up()
    myturtle.goto(dart_x, dart_y)

    if isInCircle(myturtle):
        myturtle.dot(size_of_dart, "lime")   
    else:
        myturtle.dot(size_of_dart, "darkred")

def playDarts(myturtle):
    """
    Play a game with two players, taking turns each round
    Print the outcome of the game to the console
    """
    num_of_rounds = 10
    player1_score = 0
    player2_score = 0

    for i in range(num_of_rounds):
        # Player 1
        throwDart(myturtle)
        if isInCircle(myturtle):
            player1_score = player1_score + 1
        # Player 2
        throwDart(myturtle)
        if isInCircle(myturtle):
            player2_score = player2_score + 1
    
    # Print the score and the result of the game
    print("P1:", player1_score, "| P2:", player2_score)

    if player1_score > player2_score:
        print("Player 1 won the dart game!")
    elif player2_score > player1_score:
        print("Player 2 won the dart game!")
    else:
        print("The dart game ends with a tie!")

def montePi(myturtle, num_of_darts):
    """
    Estimate the value of PI by doing a Monte Carlo simulation
    """
    num_of_darts_in_circle = 0

    for i in range(num_of_darts):
        throwDart(myturtle)
        if isInCircle(myturtle):
            num_of_darts_in_circle = num_of_darts_in_circle + 1

    pi_approximation = (num_of_darts_in_circle / num_of_darts) * 4
    return pi_approximation
    


#########################################################
#         Do not alter any code below here              #
#       Your code must work with the main proivided     #
#########################################################
def main():
    # Get number of darts for simulation from user
    # Note continuation character <\> so we don't go over 78 columns:
    print("This is a program that simulates throwing darts at a dartboard\n" \
        "in order to approximate pi: The ratio of darts in a unit circle\n"\
        "to the total number of darts in a 2X2 square should be\n"\
        "approximately  equal to pi/4")
    print("=========== Part A ===========")

    #Create window, turtle, set up window as dartboard
    window = turtle.Screen()
    darty = turtle.Turtle()
    darty.speed(0) # as fast as it will go!
    setUpDartboard(window, darty)

    # Loop for 10 darts to test your code
    for i in range(10):
        throwDart(darty)
    print("\tPart A Complete...")
    print("=========== Part B ===========")
    darty.clear()
    setUpDartboard(window, darty)
    playDarts(darty)

    print("\tPart B Complete...")
    # Keep the window up until dismissed
    print("=========== Part C ===========")
    darty.clear()
    setUpDartboard(window, darty)
    # Includes the following code in order to update animation periodically
    # instead of for each throw (saves LOTS of time):
    BATCH_OF_DARTS = 5000
    window.tracer(BATCH_OF_DARTS)

    # Conduct simulation and print result
    number_darts = int(input("\nPlease input the number of darts to be thrown in the simulation:  "))
    approx_pi = montePi(darty, number_darts)
    print("\nThe estimation of pi using "+str(number_darts)+" virtual darts is " + str(approx_pi))
    print("\tPart C Complete...")
    # Don't hide or mess with window while it's 'working'
    window.exitonclick()

main()
