#mean/stdev program with positive int values

#need this for calculations
import math

#total amount of numbers inputed by user
numbercount = 0
#count for while loop
value = 0
#list for numbers inputed by user
my_list = []
while value >= 0:
    #asks user for positive numbers
    num = int(input("Enter a positive value, to stop enter a negative value: "))
    #stores numbers in my_list while adding to numbercount
    if num > 0:
        value += 1
        numbercount += 1
        my_list.append(num)
    #if user inputs negative number, stops while loop
    elif num < 0:
        value == -1
        break
#sorts my_list lowest to highest
my_list.sort()
print(my_list)
#computes the average
mu = sum(my_list)/numbercount
print("Average:", mu )

#count for variance forloop
variance = 0
#calculates variance
for num in my_list:
    variance += (num - mu)**2
#calculates variance
variance = variance/numbercount
#calculates stdev
stdev = math.sqrt(variance)

print("Standard Deviation:", stdev)
