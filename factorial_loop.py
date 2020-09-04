#factorial forloop

value = int(input("Enter a number: "))

product = 1

for x in range(1, value + 1):
    product *= x

print(product)
