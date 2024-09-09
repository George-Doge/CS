import random

one = 0
two = 0
three = 0
four = 0
five = 0
six = 0

for i in range(101):
    print(i)
    vysledok = random.randint(1, 6)
    
    if vysledok == 1:
        one += 1
        
    elif vysledok == 2:
        two += 1
        
    elif vysledok == 3:
        three += 1
        
    elif vysledok == 4:
        four += 1
        
    elif vysledok == 5:
        five += 1
        
    elif vysledok == 6:
        six += 1
        
print(f"Jednotka bola vybratá {one}-krát, dvojka {two}-krát, trojka {three}-krát, štvorka {four}-krát, päťka {five}-krát a šestka {six}-krát")