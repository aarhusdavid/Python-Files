def read_file(file):
    str = ""
    for line in file: #itterates through file converting it to a string
        line = line.strip()
        str += line
    str = ''.join(str.split()) #removes whitespace
    return str

def write_file(str, file):
    file.write(str)

def encrypt(contents, shift):
    new = ""
    for i in contents: #iterates through each letter of the string
        new_char = chr(ord(i) + shift) #shifts each character
        new = new_char + new #adds new character to new string
    return new

def build_dictionary(str):
    dictionary = {}
    list = []
    str.split()
    for i in str:
        list.append(i)
    for word in str:
        oneset = set(word)
        for letter in oneset:
            dictionary[letter] = list.count(letter) #adds each letter to dictionary
    max = 0
    for v in dictionary.values(): #finds most frequent value in dictionary
        if v > max:
            max = v
    for k, v in dictionary.items(): #will return letter that has the highest value
        if v == max:
            return k

def find_shift(character):
    char = ord(character) #ASCII value of the most common letter
    e = ord('e') #ASCII value of e
    shift = char - e #finds shift distance by subtracting two in the order
    return shift

def decrypt(contents, shift):
    word = ""
    for i in contents:
        char = chr(ord(i) - shift) #subtracts the shift from every characters ASCII value
        word = char + word
    return word

input_file = open("hp.txt","r") #opens harry potter text file
encrypted_file = open("encrypted.txt", "w")
decrypted_file = open("decrypted.txt", "w")

file = read_file(input_file)

encrypted_text = encrypt(file, 4)
write_file(encrypted_text, encrypted_file)

dictionary = build_dictionary(encrypted_text)

shift = find_shift(dictionary)

decrypted_text = decrypt(encrypted_text, shift)
write_file(decrypted_text, decrypted_file)
