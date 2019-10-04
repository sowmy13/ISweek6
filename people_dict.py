


peopleD = {
            "Jane Smith":
                {"Age":23,
                "Address":"123 Fake St"},
            "Slim Dusty":
            {"age":44}

}
           
#print(peopleD)

         
peopleL = {
            "people" :[
                {"Name": "Jane Smith",
                "Age":23,
                "Address":"123 Fake St"},
         
                {"Name":"Slim Dusty",
                "age":44}
            ]
}
         
print(peopleD)

for person in peopleD.keys():
    print(person)
       