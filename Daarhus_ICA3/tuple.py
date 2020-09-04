#halloween tuples

#enable permutations module
from itertools import permutations
#enable random module
import random

#user total points
point_total = 0
#while loop count
round = 0
#Guessing count
failattempt = 0


print()
print("To exit the game type 'Quit'")
while round == 0:
    list = []
    tuple = ("afraid","autumn","blood","carve","candy","clown","creepy","coffin","death","devil","fright","ghost","grave","haunt","horrify","mummy","night","party","pirate","scare")
    #choses random tuple element
    selection = random.choice(tuple)
    #forloop that iterates through the selected tuple permutations
    for p in permutations(selection):
        temp = "".join(p)
        list.append(temp)

    #chooses a permutation from the list
    word = random.choice(list)
    print()
    print(word)
    #asks user for the correct word
    guess = input("What word is this? ")


    #whileloop that directs user when input is wrong
    while (guess != selection):
        #if user inputs Quit, program ends
        if guess == 'Quit':
            break

        else:
            #adds to failattempt count
            failattempt += 1
            #function that gives user 3 guesses before moving on to the next round
            if failattempt == 3:
                print()
                print("Fail, Next round")
                failattempt = 0
                round == 0
                break;


            else:
                #what the user sees if their input is incorrect
                print()
                print("Incorrect")
                print("Try again")
                print()
                print(word)
                guess = input("What word is this? ")



    #exits user from the program
    if guess == 'Quit':
        break
    #if user input is correct
    if guess == selection:
        print()
        print("Correct!")
        print()
        #adds to point total
        point_total += 1
        print("User total:", point_total)
        round == 0
