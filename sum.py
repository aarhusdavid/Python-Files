#ask user for three numbers then display the sum of those three numbers to the user

#how many numbers
num = int(input("How many numbers would you like to sum? "))

count = 0
sum = 0
#create loop that adds each number
while num > count:
    num_1 = int(input("What number would you like:"))
    sum += num_1
    num -= 1
#computer displays answer
print ("The sum is:",sum)
