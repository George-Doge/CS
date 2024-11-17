# uloha 3
# file: login.txt

logins_dict = {}

with open("login.txt", "r") as file:
    data = file.read()
    # print(data)
    data = data.split("\n")

pocet_prihlaseni = 0

for person in data:
    prihlasenie = data.count(person)
    logins_dict[person] = prihlasenie
    pocet_prihlaseni += 1

pocet_loginov = len(logins_dict)

print(f"Pocet loginov: {pocet_loginov}\nPocet prihlaseni: {pocet_prihlaseni}")
for value, key in logins_dict.items():
    print(f"{value}: {key}")