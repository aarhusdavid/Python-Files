#prompts user for alternade and breaks it up into two different words

prompt = str(input("Enter 'destruct' or 'construct': "))

if prompt == 'destruct':
    alternade = str(input("Enter an alternade: "))
    #while loop that makes sure input is a real word
    while(alternade.isalpha() == False):
        alternade = str(input("Please enter a valid word: "))
    #seperating the alternade by combining its alternate index's
    alternade_1 = alternade[0: :2]
    alternade_2 = alternade[1: :2]
    print(alternade_1, alternade_2)
if prompt == 'construct':
    #ask user for two words to make alternade
    str1 = str(input("Enter the first world of your alternade: "))
    #while loop that makes sure input is a real word
    while (str1.isalpha() == False):
        str1 = str(input("Please enter a valid word: "))
    str2 = str(input("Enter the second word of your alternade: "))
    #while loop that makes sure input is a real word
    while (str2.isalpha() == False):
        str2 = str(input("Please enter a valid word: "))
    #finding length of each word
    length1 = len(str1)
    length2 = len(str2)
    length3 = length1 + length2
    idx = 0
    word = ""
    #forloop that combines both strings
    for idx in range(length3):
        if (idx < length1):
            word += str1[idx]
        if (idx < length2):
            word += str2[idx]
        #moves on to the next index
        idx += 1
    print(word)
