#piglatin module

#function that converts word to piglatin
def wordToPig(word):
    #stores word in list
    list = []
    vowels = "AEIOU"
    #checks to see if the first letter is a vowel
    if word[0] in vowels:
        #if first letter in word is a vowel, adds yay to the end
        final_str = word + "yay"
        final_str = final_str.title()
    else:
        #forloop that creates word as a list
        for i in word:
            list.append(i)
        str1 = "".join(list)
        #adds first letter to the end
        str2 = str1[0]
        #pops the first letter off
        list.pop(0)
        #places first letter on the end
        list.append(str2)
        #addes "ay" to the end
        list.append('a')
        list.append('y')
        #converts list to string
        final_str = "".join(list)
        #capitalizes first letter
        final_str = final_str.title()
    return final_str

#function that converts first name and last name to pig latin
def nameToPig(firstName,lastName):
    #piglatin functions that convert names to piglatin
    pigfname = wordToPig(firstName)
    piglname = wordToPig(lastName)
    return(pigfname,piglname)

#gets name input from user
firstName = str(input("Enter your first name: "))
lastName = str(input("Enter your Last name: "))

#displays first and last names in pig latin
pigname = nameToPig(firstName,lastName)
print(pigname[0], pigname[1])
