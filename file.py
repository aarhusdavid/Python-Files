#read from one file and write to another file

# input_file = open("file1.txt", "r")
# output_file = open("file2.txt", "w")
#
# #append file to the original file
# #output_file = open("file2.txt", "a")
#
# for line in input_file:
#     new_str = ""
#     line = line.strip()
#     for char in line:
#         new_str = char + new_str
#     print("The reversed line is:", new_str, file = output_file)
#
# input_file.close()
# output_file.close()









# #writing to a file
# # #
# file1 = open("file1.txt","w")
# print("apple orange pear", file = file1)
# # # print("yay, files are so cool", file = file1)
# file1.close()


#reading ro a file
#
# temp_file = open("file1.txt","r")
# for line in temp_file:
#     print(line)
# temp_file.close()

def read (input_file):
    contents = ""
    for line in input_file:
        line = line.strip()
        contents += line
    return contents

input_file = open("file1.txt", "r")
file = read(input_file)
print(file)
