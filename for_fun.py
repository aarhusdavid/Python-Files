#calculates resturants forcast for one week
#user inputs data from previous week

import math
print("Enter data from previous week")
bus = int(input("How many bussers:"))
bushour = int(input("How many hours:"))
serve = int(input("How many servers:"))
servehour = int(input("How many hours:"))
cook = int(input("How many cooks:"))
cookhour = int(input("How many hours:"))
expo = int(input("How many expos:"))
expohour = int(input("How many hours:"))
food = int(input("How much money spent on food supply:"))
util = int(input("Total utility bill:"))
Mon = int(input("Monday Revenue:"))
Tues = int(input("Tuesday Revenue:"))
Wed = int(input("Wedsnday Revenue:"))
Thur = int(input("Thursday Revenue:"))
Fri = int(input("Friday Revenue:"))
Sat = int(input("Saturday Revenue:"))
Sun = int(input("Sunday Revenue:"))

if bushour > 200:
    print("Too many bussers")
else:

    print("")

if servehour > 600:
    print("Too many servers")
else:

    print("")


if cookhour > 400:
    print("Too many cooks")
else:

    print("")

if expohour > 200:
    print("Too many expos")
else:

    print("")


#employee wages
bus_w = 10.25 * bushour
serve_w = 15 * servehour
cook_w = 25 * cookhour
expo_w = 15 * expohour


if food + bus_w + serve_w + cook_w + expo_w + util  > Mon + Tues + Wed + Thur + Fri + Sat + Sun:
    print("No Profit")
else:

    print("Profit")
