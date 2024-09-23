# uloha 7

dolny_limit = 0
horny_limit = 20

ciselko = int(input(f"Zadaj cislo od {dolny_limit} po {horny_limit}: "))

if not dolny_limit <= ciselko <= horny_limit:
    print("Zly vstup")
    
else:
    for i in range(1, ciselko + 1):
        print(i*"*")
