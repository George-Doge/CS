from random import randint

list = []

for i in range(100):
    list.append(randint(1, 300))

print(f"Sum: {sum(list)}\nMin:{min(list)}\nMax:{max(list)}")