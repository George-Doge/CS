import random

písmena=["A", "Á", "Ä", "B", "C", "Č","D","Ď","DZ","DŽ","E","É","F","G","H","CH","I","Í","J","K","L","Ĺ","Ľ","M","N","Ň","O","Ó","Ô","P","Q","R","Ŕ","S","Š","T","Ť","U","Ú","V","W","X","Y","Ý","Z","Ž"]
heslo=""
for i in range(5):
    čísla= str(random.randrange(10))
    heslo+=random.choice(písmena)
    heslo+=čísla
    
print(f"Tvoje heslo je {heslo}")



