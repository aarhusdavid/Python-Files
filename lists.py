#lists

s_list = [['Name', 'Age', 'GPA',],['Bill', 25, 3.55],['Rich', 26, 4.00]]
n_list = [1,2,3,4]

# b_info = s_list[1] #row
# print(b_info)
#
# b_gpa = b_info[2] #column
# print(b_gpa)
#
# b_gpa1 = s_list[1][2]
# print(b_gpa1)

s_list[0][0] = "David"
print(s_list)

print(max(n_list))
print(min(n_list))
print(sum(n_list))

n_list.append(34)
print(n_list)
