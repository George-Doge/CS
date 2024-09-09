slovo = input("Napis slovo: ")
string="IÍiíYÝyý"
nove_slovo = ""

for pismeno in slovo:
    if pismeno in string:
        nove_slovo += "_"
    else:
        nove_slovo += pismeno

print(nove_slovo)