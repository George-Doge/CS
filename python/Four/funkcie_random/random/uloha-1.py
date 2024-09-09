import random

samohlasky = ['a', 'ä', 'e', 'i', 'y', 'o', 'u','á', 'é', 'í', 'ý', 'ó', 'ú']
spoluhlasky = ['d', 't', 'n', 'l', 'h', 'ch', 'k', 'g', 'ď', 'ť', 'ň', 'ľ', 'ž', 'š', 'č', 'dž', 'c', 'dz', 'j', 'b' , 'm', 'p', 'r', 's', 'v', 'z', 'f']

heslo = ""
for i in range(4):
    heslo += random.choice(samohlasky)
    heslo += random.choice(spoluhlasky)
    
print(f"Heslo je {heslo}")