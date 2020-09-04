#calculating seconds to (hours,mintues,and seconds)
print("enter seconds,(range 1-86400)")
seconds = input("seconds:")
seconds_int = float(seconds)

import math

#calcute into minutes
hours = seconds_int//(3600)
minutes = (seconds_int//60)%60
seconds_2 = seconds_int%(60)
#computer displays seconds as (hours,minutes,and seconds)
print(hours,"Hours", minutes, "minutes", seconds_2, "seconds")
