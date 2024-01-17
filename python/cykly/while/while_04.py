a = ""
znamky = []
priemer = 0
sucet = 0
i = 0
while a != 0:
    a = int(input("zadaj známky: "))
    if 1 <= a <= 5:
        znamky.append(a)
      
while i < len(znamky):
    sucet += znamky[i]
    i += 1
      
priemer = sucet/len(znamky)
print(f"Priemer znamok je {priemer}")
