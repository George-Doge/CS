samohlasky = "aeiouäáéíóúAEIOU"
slovo = input("Zadaj text ")
samohlasky_pocet = 0

for pismeno in slovo:
    if pismeno in samohlasky:
        samohlasky_pocet +=1

print(f"V texte je {samohlasky_pocet} samohlasok.")