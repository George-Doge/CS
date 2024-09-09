data = {}
with open("names.txt", "r") as file:
    information = file.read().splitlines()

    pocet_riadkov = len(information)
    
    for i in range(0, pocet_riadkov, 2):
        data[information[i]] = information[i+1]

print("Meno\tPriemer")
for key, value in data.items():
    print(f"{key}\t{value}")