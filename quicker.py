
data = []
with open("fruits.txt") as infile:
    line = infile.readline() # read everything into a line
    data_dict = {}
    
    while line:
        print("line {} ".format(line))
        
        #line = read.inline
        #print(word)
    
        if line in data_dict:
            data_dict[line] += 1
        else:
            data_dict[line] = 1
        line = infile.readline()
print(data_dict)

