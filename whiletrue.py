#example of while True program
#program should give sum of positive numbers
pos_num = True
the_sum = 0
while pos_num:
    num = int(input("enter a number: "))
    if num > 0:
        the_sum += num
    else: #the case when the number is negative
        pos_num = False
print("The sum is: ", the_sum)
