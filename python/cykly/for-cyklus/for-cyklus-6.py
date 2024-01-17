# vypise delitele
pojde = []
x = int(input("zadaj číslo: "))
for i in range(1, x + 1):
    if x % i == 0:
        pojde.append(i)
        
print(f"Delitele tohto čísla sú: {pojde}")
    