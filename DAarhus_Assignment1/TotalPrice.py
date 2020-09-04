#finding total price of an item and including the sales tax

import math

#have computer ask for price and salestax
price_str = input("enter purchase price:")
price_int = float(price_str)

salestax_str = input("enter sales_tax (percent):")
salestax_int = float(salestax_str)


#calculate total price
sumprice_int = price_int * (salestax_int/100)
total_price = sumprice_int + price_int


#have computer the total price to the user
print("Your total price is:", round(total_price,2))
