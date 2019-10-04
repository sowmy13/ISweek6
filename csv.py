

import csv
'''
with open("deniro.csv", "r") as infile:
    rdr = csv.reader(infile)
    for row in rdr:
        print(row)
 '''




data = [
            ["Name", "Address", "Age"],
            ["Jane Smith", 23, "123 Fake St"],
            ["Slim Dusty", "564 Cunnamulla Fella St", 44],
            ["Albus Dumbledore", 100, "Hogwarts"]
            ]
with open("people.csv", "w") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(data[0])
 

