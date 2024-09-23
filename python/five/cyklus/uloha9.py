# uloha 9

zaciatok = 1
koniec = 50

for cislo in range(zaciatok, koniec+1):
    if cislo % 5 == 0 and cislo % 3 == 0:
        print("FizzBuzz")

    elif cislo % 5 == 0:
        print("Buzz")

    elif cislo % 3 == 0:
        print("Fizz")
