# uloha 4

start_a = int(input("Zadaj premennu 'a': "))
start_b = int(input("Zadaj premennu 'b': "))
print(f"Program vypise cisla od {start_a} do {start_b}.")

if start_a < start_b:
    for i in range(start_a, start_b+1):
        if i%2 == 0:
            print(i)

elif start_a > start_b:
    for i in range(-start_a, -start_b+1):
        if i%2 == 0:
            print(-i)

else:
    print("Cisla sa nemozu rovnat.")
