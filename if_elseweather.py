#computer recomends appropriate clothing for weather

#ask for weather
temp = int(input("What is the temperature outside?:"))
if temp > 90:
    print("wear shorts!")
#calculates if temp is greater than 70
elif 70 < temp <=90:
#prints "wear shorts" if temp is greater than 70
    print("t shirt weather")
#if temp is less than 70 but greater than 60
else:
#prints "wear pants" if temp is less than 70
        print("bring a jacket.")
        rain = int(input("Is it raining? 0 for no, 1 for yes:"))
        if rain == 0:
            print("Looks like a clear day")
        else:
            print("Take an umbrella")
