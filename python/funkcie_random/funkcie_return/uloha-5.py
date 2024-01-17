#ULOHA 5

def sum_of_divisors(number):
    divisors = []
    sum = 0

    for i in range(1, number+1):
        if number % i == 0:
            divisors.append(i)

    for i in divisors:
        sum += i

    return sum

number = int(input("Enter a number: "))

sum = sum_of_divisors(number)

print(f"Sum of {number}'s divisors is {sum}.")