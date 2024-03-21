from random import randint

def dve_kocky(n):

    count_multiplications = {
        "2":0,
        "3":0,
        "4":0,
        "5":0,
        "6":0,
        "7":0,
        "8":0,
        "9":0,
        "10":0,
        "11":0,
        "12":0
    }

    for i in range(0, n):
        first_roll = randint(1, 6)
        second_roll = randint(1, 6)

        sum = first_roll+second_roll

        count_multiplications[str(sum)] += 1

    return count_multiplications


number_rolls = int(input("Enter number of rolls you want the script to take: "))

output_count = dve_kocky(number_rolls)

print("\nHere are the final counts:")
for key, value in output_count.items():
    print(f"{key}:{value}")