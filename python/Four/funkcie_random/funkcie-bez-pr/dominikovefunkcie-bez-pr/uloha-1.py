import random

def kocka():
    cisielko = random.randint(1, 6)
    print(f"Hodili ste {cisielko}")

for i in range(100):
    kocka()
