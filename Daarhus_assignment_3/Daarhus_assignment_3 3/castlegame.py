#create your own adventure

import random
#variable creation & setting loop control variable
next_room = 1
#initiates the random number generator for the adventure
death_die = random.randint(1,100)

print()
print("Welcome to the Chapman Castle. As you may know you are on an adventure to find a lost treasure. Some Chapman  alumni have left a huge amount of money hidden somewhere within the castle for some lucky soul to find. If youfind the treasure, it is yours, however if you chose to play and do not find the treasure you will be cursed  with student loans for the rest of your life.")
print()

#while loop that directs user to given room based on what they input
while next_room != 0:
    if next_room == 1:
        print("You start at the front door of the Castle. As you open the front door you notice a door to your 'left' and    your 'right'. Also straight ahead is a giant spiral 'staircase'.")
        print()
        #prompts user to enter where he/she would like to go
        choice = input("Where would you like to go? ")
        if choice == 'left':
        #where the if statement directs the user if they chose left
            if death_die > 98:
            #initiates random number generator
                print("You were mauled by a P-Safe officer.")
                print("GameOver")
                #ends game by making next_room = 0
                next_room = 0
            else:
                next_room = 2
        elif choice == 'right':
        #where the if statement directs the user if they chose right
            next_room = 3
        elif choice == 'staircase':
        #where the if statement directs the user if they chose staircase
            next_room = 4

        else:
        #where the if statement directs the user if they chose left and the second if statement proved false

            next_room = 2
    elif next_room == 2:
        print()
        print("You open the door to a nice library.")
        print("There are books all around, however you notice a hatch door in the middle of the room which looks like it     could lead to the basement.")
        print()
        choice = input("Do you want to enter the 'hatch' door or continue looking around the 'library' for the treasure? ")
        if choice == 'hatch':
        #where the if statement directs the user if they chose hatch
            print()
            print("I'm sorry to tell you that you have fallen into a trap and can no longer continue with the search.")
            print("GameOver")
            #ends game by making next_room = 0
            next_room = 0
        elif choice == 'library':
        #where the if statement directs the user if they chose library
            print()
            print("As you search around the library, you notice a small note tucked between two books on one of the bookshelves. It reads 'if you're looking for the treasure, go back the way you came'")
            print()
            #takes user back to the front of the castle
            next_room = 1

    elif next_room == 3:
        print()
        print("You open the door to a fully furnished kitchen, tiles floors, and wood cabinents. There is a side door that leads outside. ")
        print()
        choice = input("Would you like to contiune looking around the 'kitchen' for the treasure or exit through the 'side' door to see what lies behind it?  ")
        if choice == 'side':
        #where the if statement directs the user if they chose side
            print()
            print("You have opened the door to starbucks and will be in line forever")
            print("GameOver")
            #ends game by making next_room = 0
            next_room = 0
        if choice == 'kitchen':
        #where the if statement directs the user if they chose kitchen
            print()
            print("As you look around the kitchen you begin to hear a faint but small noise coming from the oven, you head over to investigate. As you open the oven door you see that it leads down into a secret tunnel, and down in the tunnel you realize the noise is a person who is trapped down there.")
            print()
            choice2 = input("Do you want to 'save' the person or go 'back' the way you came to the front of the castle? ")
            if choice2 == 'save':
            #where the if statement directs the user if they chose save
                if death_die > 50:
                #initiates random number generator
                    print()
                    print("You find a rope and lower it down into the tunnel, out comes another student who claims to had attempted to find the treasure before. He tells you you can find the treasure upstairs.")
                    print()
                    choice3 = input("Should you take his 'advice' or continue on your 'own'? ")
                    if choice3 == 'advice':
                    #directs user if they chose advice
                        print("You head back to the front of the castle and go upstairs")
                        next_room = 4
                        if choice3 == 'own':
                        #directs user if they chose own
                            choice4 = input("Would you like to try the 'side' door or go 'back' the way you came?  ")
                            if choice4 == 'side':
                            #directs user if they chose side
                                print("You have opened the door to starbucks and will be in line forever")
                                print("GameOver")
                                #ends game by making next_room = 0
                                next_room = 0
                            if choice4 == 'back':
                                next_room == 1
                else:
                    print()
                    print("As you attempt to save the person you fall into the hole ending you search.")
                    print("GameOver")
                    #ends game by making next_room = 0
                    next_room = 0
            if choice2 == 'back':
                print()
                next_room = 1

    elif next_room == 4:
        print()
        print("Now that you are upstairs you are faced with three doors")
        choice = input("Would you like to enter the 'left' door, 'right' door, or the 'middle' door? ")
        if choice == 'left':
        #directs user if they chose left
            if death_die > 85:
            #initiates random number generator
                print()
                print("You fall into a black hole")
                print("GameOver")
                #ends game by making next_room = 0
                next_room = 0
            else:
                    print()
                    print("You are in a windowless room with no doors.")
                    choice2 = input("Go 'back' the way you came or 'stay' for some weird reason? ")
                    if choice2 == 'back':
                    #directs user if they chose back
                        next_room = 4
                    if choice2 == 'stay':
                    #directs user if they chose stay
                        print()
                        print("You fall into a black hole")
                        print("GameOver")
                        #ends game by making next_room = 0
                        next_room = 0
        if choice == 'right':
        #directs user if they chose right
                    print()
                    print("You open the door to find another door and a ladder that leads to the attic.")
                    choice3 = input("Do you want to enter the other 'door' or climb up the 'ladder'? ")
                    if choice3 == 'door':
                    #directs user if they chose door
                        print()
                        print("You have stepped into a portal that has brought you back to the front of the castle.")
                        print()
                        next_room = 1
                    if choice3 == 'ladder':
                    #directs user if they chose ladder
                        print()
                        print("Congratulations!! You have found the treasure! Thanks for playing.")
                        #ends game by making next_room = 0
                        next_room = 0

        if choice == 'middle':
        #directs user if they chose middle
                    print()
                    print("You open the door to a long hall way. At the end of the hall stands a door.")
                    choice4 = input("Would you like to walk down the hall way to the 'door' or go 'back' the way you came? ")
                    if choice4 == 'back':
                    #directs user if they chose back
                        next_room = 4
                    elif choice4 == 'door':
                    #directs user if they chose door
                        print()
                        print("You walk down the hallway, as you approach the door you feel the room getting oddly colder and colder. You open the door to another hallway, much like the one you just walked down.")
                        print()
                        print("I'm sorry to inform you that you have entered a never ending loop.")
                        print("The only way to get out is to guess a number 1-100. If you guess the right number you will be put back at the top of the staircase, if not you will be stuck in the loop forever.")
                        print()
                        num = input("enter a number 1-100: ")
                        if death_die == num:
                        #initiates random number generator
                                next_room = 4

                        else:

                            print("Welcome to the never ending loop")
                            print("GameOver")
                            #ends game by making next_room = 0
                            next_room = 0
