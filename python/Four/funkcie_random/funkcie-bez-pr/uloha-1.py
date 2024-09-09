import random

def kocka():
    cislo = random.randint(1, 6)
    print(f"Kocka hodila cislo {cislo}")

for i in range(100):
    kocka()
