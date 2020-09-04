#dice game against the computer
import math
#enable math module
import random
#enable random module

#total player counts for the entire game
p1count = 0
c1count = 0

roll = input("Type 'yes' to roll: " )
while roll == 'yes':
    #total player counts for their turns
    playerturn = 0
    compturn = 0
    #my turn
    while True:
        ranum = random.randint(1,6)
        #if roll is 1 cancels count for the turn
        if ranum == 1:
            playerturn = 0
            print()
            print("You rolled a 1")
            print("Turn over")
            print()
            break

        else:
            #if count is equal or greater than 100, you win
            if (p1count + playerturn) >= 100:
                print("You win")
                print()
                break
            playerturn += ranum
            print("You rolled a", ranum)
            #asks if player would like to roll or hold
            turn = input("Do you want to roll again (r) or hold (h)? ")
            if turn == 'r':
                continue
            else:
                print()
                break


    #computers turn
    while True:
        if compturn >= 20:
            break
        ranum = random.randint(1,6)
        print("The computer rolled a: ", ranum)
        #if roll is 1 cancels count for the turn
        if ranum == 1:
            compturn = 0
            print()
            break
        else:
            compturn += ranum

            #if computer count is equal or greater than 100, computer wins
            if (c1count + compturn) >= 100:
                print("Computer wins")
                print()
                break
    print()
    #print statements that display totals after each round
    print("Computers turn total is: ", compturn)
    print("Your turn total is: ", playerturn)
    p1count += playerturn
    c1count += compturn
    print("Your total is: ", p1count)
    print("The computer's total is: ", c1count)
    print()

    #ends the program if anyone reaches 100 or exceeds it
    if (p1count >= 100 or c1count >= 100):
        print()
        break
