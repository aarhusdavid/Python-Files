#complement module

#function for computing a DNA sequence's complement
def complement(dna_input):
    #stores complement in list
    list = []
    #forloop that iterates through input by user
    for i in dna_input:
        if i == 'A':
            list.append('t')
        elif i == 'T':
            list.append('a')
        elif i == 'G':
            list.append('c')
        elif i == 'C':
            list.append('g')

    #combines list into string
    str1 = "".join(list)
    #capitalizes string
    up_str1 = str1.upper()
    return(up_str1)

#function that reverses the DNA sequence's complement
def revcomplement(dna_input):
    #complement function
    list1 = complement(dna_input)
    #reverses complement
    revlist = list1[ : :-1]
    return(revlist)


condition = True
#while loop that checks for invalid input
while condition:
    condition = True
    dna_input = str.upper(input("Enter a DNA strand: "))
    #iterates through input for error
    for i in dna_input:
        #checks input to see if it is a DNA squence
        if (i == 'A') or (i == 'T') or (i == 'G') or (i == 'C'):
            condition = False
            continue
        #tells user input is an invalid DNA sequence
        else:
            condition = True
            print("Error, invalid DNA sequence")
            break

#displays Complement
comp_dna = complement(dna_input)
print("Complement is", comp_dna)
#displays reverse complement
rev_dna = revcomplement(dna_input)
print("Reverse Complement is", rev_dna)
