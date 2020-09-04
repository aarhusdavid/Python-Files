#finals practice

wc = "red blue red blue yellow green"
t = ('c','h','a','p','m','a','n')
l = ['c','h','a','p','m','a','n']
sub_l = ['c','h','a',]
s = "chapman"
n = ['1','2','3','3','4','5','5']
d = {'bill':'123-4577','jerry':'333-3333','picklerick':'231-6969'}
a_set = {'1','2','3','3'}
b_set = {'3','4','5','6'}

#slicing
# a = s[0: :2]
# print(a)

# for i in range(2,11,2):
#     print(i)

# for i in range(len(s)):
#     print(s[i])


#tuples

# t = ('a','b','fuck','penis')
# print(t.index('fuck'))
# print(t.count('fuck'))
# print(n.index('3'))


# dictionaries

# d['emily'] = '714-2232'
# print(d.items())
# for key in d:
#     print(key,d[key])
# def wordcount(str):
#     word_list = str.split()
#     count_dict = {}
#     for word in word_list:
#         if word in count_dict:
#             count_dict[word] += 1
#
#         else:
#
#             count_dict[word] = 1
#     return count_dict
#
# print(wordcount(wc))


#sets
# set1 = set(l)
# print(set(set1))

# print(a_set&b_set) #intersection
# print(a_set|b_set) #union
# print(a_set-b_set) #difference
 #why? you need unique elements


#files

# def files(input_file,output_file):
#     line_number = 1
#     for line in input_file:
#         line = line.strip()
#         if line_number % 2 == 1:
#             print(line, file = output_file)
#         line_number += 1

#
# input_file = input("Enter a file name: ")
# write_file = input("Enter a file you'd like to write to: ")
# try:
#     file1 = open("input_file", "r")
#     file3 = open("write_file", "w")
# except FileNotFoundError:
#     print("Invalid file name")

# files(file1,file3)
#
# file1.close()
# file3.close()







#practice problems

#1
# def files(x,y,w,z):
#     for line in x:
#         print(line, file = y)
#     for line in w:
#         print(line, file = y)
#
# input1 = input("Enter a file name: ")
# input2 = input("Enter another file name: ")
#
# try:
#     file1input = open(input1, "r")
#     file2input = open(input2, "r")
# except FileNotFoundError:
#     print("Invalid file entry, try again")
#
# file1output = open(input1, "w")
# file2output = open(input2, "w")
# files(file1input, file2output, file2input, file1output)
#
# file1input.close()
# file2input.close()
# #

# #2
#b
def dictionary(x):
    letter_list = x.strip()
    diction = {}
    for i in letter_list:
        if i in diction:
            diction[i] += 1

        else:

            diction[i] = 1
    return diction

# ans = dictionary(s)
# print(ans)

#a
def letter(x):
    diction = dictionary(x)
    letters = diction.keys()
    numbers = diction.values()
    for v in numbers:
        if v == max(numbers):
            v = max
    for k,t in diction.items():
        if t == max:
            print(k)
    return k

ans = letter(s)
print(ans)








#3
# def upperlower(x):
#     letter_list = x.strip()
#     diction = {}
#     uppercount = 0
#     lowercount = 0
#     for i in letter_list:
#         if i == i.upper():
#             uppercount += 1
#         else:
#             lowercount += 1
#     diction["upper"] = uppercount
#     diction["lower"] = lowercount
#     return diction
#
# print(upperlower(s))

#4
# def subset(r,s):
#     setr = set(r)
#     sets = set(s)
#     newset = setr&sets
#     count = 0
#     subset_count = 0
#     for i in newset:
#         count += 1
#     for i in setr:
#         subset_count += 1
#     if count == subset_count:
#         print("r is a subset of s")
#     else:
#         print("r is not a subset of s")
#
# print(subset(sub_l,l))
