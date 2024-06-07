with open("login.txt", "r") as file:
    data = file.read()
    data = data.split("\n")

pocet_prihlaseni = len(data)
dict_prihlaseni = {}

for entry in data:
    dict_prihlaseni[entry] = data.count(entry)

pocet_loginov = len(dict_prihlaseni)

print(f"Pocet loginov: {pocet_loginov}\nPocet prihlaseni: {pocet_prihlaseni}")
for key, value in dict_prihlaseni.items():
    print(f"{key}: {value}")