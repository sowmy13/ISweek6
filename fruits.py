
data = []
with open("fruits.txt") as infile:
    data = infile.readlines()
    
print(data)

data_dict = {}

for word in data:
    print(word)
    print(data_dict)
    if word in data_dict:
        data_dict[word] += 1
    else:
        data_dict[word] = 1
   
print(word)