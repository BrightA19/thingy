import pdb
import random

def showDice(value):
    if value == 1:
        return("---------\n|       |\n|   *   |\n|       |\n---------")
    elif value == 2:
        return("---------\n|*      |\n|       |\n|      *|\n---------")
    elif value == 3:
        return("---------\n|*      |\n|   *   |\n|      *|\n---------")
    elif value == 4:
        return("---------\n|*     *|\n|       |\n|*     *|\n---------")
    elif value == 5:
        return("---------\n|*     *|\n|   *   |\n|*     *|\n---------")
    else:
        return("---------\n|*     *|\n|*     *|\n|*     *|\n---------")

def answer(dice):
    total = 0
    for die in dice:
        total += die
    return total

def keepPlaying(prompt):
    ans = input(prompt)
    if ans == 'y' or ans == '':
        return True
    else:
        return False

def run():
    # Probably counts wins or something.
    # Great variable name, 10/10.
    # pdb.set_trace()
    num_dice = 5
    wins = 0
    losses = 0
    count = 0
    msg = "Would you like to play a dice game? [Y/n]"
    while keepPlaying(msg):
        dice = []
        for i in range(num_dice):
            dice.append(random.randrange(1, 7))

        for die in dice:
            print(showDice(die))

        guess = int(input("Sigh. What is your guess?: "))
        result = answer(dice)
        if guess == result:
            print("Congrats, you can add like a 5 year old...")
            wins = wins + 1
            count = count + 1
        else:
            print("Sorry that's wrong")
            print("The answer is:", answer(dice))
            print("Like seriously, how could you mess that up")
            losses += 1
            count = 0
        print("Wins:", wins," Losses: ", losses)

        if count == 6:
            print("You won... Congrats...")
            print("The fact it took you so long is pretty sad")
            break
        else:
            msg = "Would you like to continue playing? [Y/n]: "

def main():
    print("Add the values of the dice. Get it right 6 times in a row,", end=" ")
    print("and you are a winnner! (You want to be a winner, DON'T YOU?)")
    print("It's really that easy. Seriously, what else are you doing with your life?")
    run()
main()
