#finding total price of an item and including the sales tax

import math

#have computer ask for price and salestax
price_str = input("enter purchase price:")
price_int = float(price_str)

#tell user that inputs are invalid if price is negative
if price_int < 0:
    print("Price has to be > $0.00")
    
else:

    #ask for sales tax (percentage)
    salestax_str = input("enter sales_tax (percent):")
    salestax_int = float(salestax_str)
    if salestax_int < 0:
        print("Sales tax has to be > 0%")

    else:

        #calculate total price
        sumprice_int = price_int * (salestax_int/100)
        total_price = sumprice_int + price_int
        #have computer the total price to the user
        print("Your total price is:", round(total_price,2))
