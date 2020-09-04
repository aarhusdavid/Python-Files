#turning celsius into fahrenheit

import math

#computer asks for temperature in celsius
tempc_str = input("enter temperature in Celsius: ")
tempc_int = float(tempc_str)

#converts celsius into fahrenheit
tempf = tempc_int * (9/5) + 32

#displays fahrenheit temperature to the user
print ("Temperature in Fahrenheit:",tempf)
