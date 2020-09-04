def unique(s):
    s = s.lower()
    s_set = set(s)
    s_list = list(s_set)
    return s_list


string = "Enter a word"
print(unique(string))
