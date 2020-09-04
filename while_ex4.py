#another while example

my_int = int(input("Enter a number:"))
count = 0

while count < my_int:
    print(count)
    count += 1
print()

count = 0
while count < my_int:
    print(my_int)
    my_int -= 1
