
def func1(a_str):
    a_int = int(a_str)
    b_int = a_int * a_int + 2
    return b_int

try:
    a = input("Enter a number: ")
    b = func1(a)
    print(b)
except ValueError:
    print("Incorrect input.")
