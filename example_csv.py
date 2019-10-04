

'''
with open("deniro.csv", "r") as infile:
    rdr = csv.reader(infile)
    for row in rdr:
        print(row)
 '''



  
#csv writer

import csv

data = [
    ["Name","Address","Age"],
    ["Jane Smith", "123 Fake St", "23"],
    ["Slim Dusty","564 Cunnamulla Fella St","44"]
    ]
    
with open("people_CSV.csv","w") as outfile:
#    writer = csv.writer(outfile, delimiter=',')
    writer = csv.writer(outfile, delimiter=',')
    for row in data:
        writer.writerow(row)

