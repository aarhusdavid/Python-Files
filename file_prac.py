#function practice,Write a function that takes in two file names as parameters and writes every other line from one file to the other file.





def files (input_file,output_file):
    line_num = 1
    for line in input_file:
        line = line.strip()
        if line_num % 2 == 1:
            print(line, file = output_file)
        line_num += 1
    #no return since output is going to a file

file = open("file1.txt","r")
file2 = open("file2.txt","w")

files(file, file2)
file.close()
file2.close()
