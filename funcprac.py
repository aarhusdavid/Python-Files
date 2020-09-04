# 1)
#
# a 4
# b 3
# c my_list = [0,1,2,3,2,3,4,5,5,6,7]
#
# list = []
# for i in range(0,6,2):
#     for k in range(4):
#         list.append(i+k)
#
# print(list)
#
# 2) it would do the same thing, only have a return
# value that you would have to print




# def case(x):
#     alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     low = "abcdefghijklmnopqrstuvwxyz"
#     num = 0
#     nim = 0
#     for i in x:
#         if i in alph:
#             num += 1
#         if i in low:
#             nim += 1
#     return "upper case letters:", num, "lowercase letters:", nim
#
# number = str(input("Enter a word: "))
# answer = case(number)
# print(answer)




# def func(x):
#     total = 0
#     while x > 0:
#         total = total + x*(x-1)
#         x -= 1
#     return total
#
# num = int(input("Enter a number: "))
# answer = func(num)
# print(answer)

# def func(x):
#     total = 0
#     for i in range(x):
#         total += i * (i-1)
#     return total
#
# num = int(input("Enter a number: "))
# answer = func(num)
# print(answer)

# listA = [1,2,3,4,5]
# listB = []
#
# for num in listA:
#     listB.append(num)
# listA[2] = 10
#
# print(listB,listA)

# my_list =[]
# for i in range(3):
#     for k in range(5):
#         my_list.append(i+k)
#
# print(i)
# print(k)
# print(my_list)





# def letters(s):
#     import string
#     result = []
#     for letter in string.ascii_lowercase:
#         if s.count(letter) >= 1:
#             result+=letter
#     return result

# word = str(input("Enter a sentence: "))
# answer = letters(word)
# print(answer)
