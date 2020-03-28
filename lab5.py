import turtle

def seq3np1(n):
    """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: count (int) number of iterations it takes to for n to reach 1
    """
    count = 0
    while(n != 1):
        count = count + 1

        if(n % 2) == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1

    return count


def drawSequenceGraph(upperBound):
    """
        For each number between 1 through uppperBound, inclusive, calculates how many
        iterations are required to reach 1 using the seq3np1 function. Then it draw
        a graph, also writing the number having the most iterations.
        args: upperBound (int) the inclusive number to go up to from 1
        return: None
    """
    wn = turtle.Screen()
    wn.setworldcoordinates(0, 0, 10, 10)

    grapher = turtle.Turtle()
    writer = turtle.Turtle()
    writer.up()

    max_so_far = 0
    
    for start in range(1, upperBound + 1):
        result = seq3np1(start)

        if result > max_so_far:
            max_so_far = result

            writer.clear()
            writer.goto(0, max_so_far)
            writer.write("Maximum so far: " + str(start) + ", " + str(max_so_far))

        wn.setworldcoordinates(0, 0, start + 10, max_so_far + 10)
        grapher.goto(start, result)

    wn.exitonclick()


def main():
    upperBound = int(input("Enter the upper bound: "))
    while upperBound <= 0:
        upperBound = int(input("Value must be positive. Enter the upper bound: "))

    drawSequenceGraph(upperBound)

main()

