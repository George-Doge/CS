# nahradi samohlasky v texte s '*'
samohlasky = "aeiuoAEIOUyY"
slovo = input("zadaj slovo: ")
nove_slovo = ""
for pismena in slovo:
    if pismena in samohlasky:
        nove_slovo += "*"
        
    else:
        nove_slovo += pismena
        
print(nove_slovo)
