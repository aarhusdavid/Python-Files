# contacts = {'bill':'123-1235','rich':'777-3345','Jane':'454-2222'}
# contacts['jane'] = '333-0124'
#
# print(contacts)
#
# for element in contacts:
#     print(element)
#
# for key in contacts:
#     print(key,contacts[key])
#
# print(contacts.keys())
# print(contacts.values())
# print(contacts.items())


#word count example
def word_count(str):
    word_list = str.split()
    count_dict = {}
    for word in word_list:
        if word in count_dict:
            count_dict[word] += 1

        else:

            count_dict[word] = 1
    return count_dict

s = 'one fish two fish red fish blue fish'
ans = word_count(s)
print(ans)
