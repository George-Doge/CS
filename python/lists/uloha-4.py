from random import randint

numbers = []

def zostupne(numbers):
    print(numbers)
    temp_numbers = numbers
    temp_numbers.sort()
    temp_numbers = temp_numbers[::-1]

    if numbers == temp_numbers:
        print("Je to utriedené")

    else:
        print(f"Po zotriedení to je: {temp_numbers}")


for i in range(10):
    numbers.append(randint(1, 99))

zostupne(numbers)