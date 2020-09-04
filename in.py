a_str = input("enter a word")
vowels = "aeiou"
for char in a_str:
    if char in vowels:
        print(char, "is a vowel")
