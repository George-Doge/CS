with open("meno_mesto.txt", "r") as file:
    data = file.read()

data = data.split("\n")

for person in data:
    
    person_length = len(person)

    city = person[person_length-6:]
    
    if city == "Kosice":
        print(person)

        with open("mena.txt", "a") as file:
            file.write(person + "\n")