#calculating the quadratic formula

import math

#computer asks for coefficients a,b,and c
print("Enter coefficients a,b,and c for the quadratic formula")
a_str = input("a:")
b_str = input("b:")
c_str = input("c:")

a_int = float(a_str)
b_int = float(b_str)
c_int = float(c_str)

#calculte whether the given coefficients make the quadratic formula invalid
if (b_int**2) > (4 * a_int * c_int):
    rootbase = math.sqrt(b_int**2 - 4 * a_int * c_int)
    root_1 = ((-b_int + (rootbase)) / (2 * a_int))
    root_2 = ((-b_int - (rootbase)) / (2 * a_int))

#computer displays the roots to the user
    print("roots are:," ,root_1, root_2)

else:
#computer tells the user("ValueError: math domain error")
    print("math domain error")
