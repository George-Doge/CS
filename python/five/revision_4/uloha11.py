from random import randint

def kocka():
    return randint(1, 6)

minule = 0

for i in range(20):
    teraz = kocka()
    print(teraz, end=" ")

    if teraz == minule:
        print("*", end=" ")

    minule = teraz