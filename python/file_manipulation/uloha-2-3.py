from random import randint

# ulohy 2 a 3 som spojil do jednej

with open("python/file_manipulation/nahodne_cisla.txt", "w") as file:
    for i in range(100):
        print(file.write(f"{randint(1, 500)} "))