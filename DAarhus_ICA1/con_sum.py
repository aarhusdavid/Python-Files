#program prompts user for number then adds all its consecutive integers

x = int(input("Enter a number: "))

count = 0
sum = 0

#create loop that adds each integer
while count < x:
    print(x)
    sum += x
    x -= 1

#computer displays number
print("The sum is:",sum)
