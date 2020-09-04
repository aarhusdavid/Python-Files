#perfect square
import math

x = int(input("Enter a number: "))
#defince what a square root is
sroot = math.sqrt(x)
while x > 0:
    if x%sroot > 0:
        print("Not a perfect square")
        x = 0

    else:

        print(sroot)
        x = 0



#did not finish
