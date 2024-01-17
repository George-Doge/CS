#ULOHA 8

def factorial_func(number):
    factorial = 1
    for i in range(1, number+1):
        factorial *= i

    return factorial


number = int(input("Enter a number: "))
factorial = factorial_func(number)
print(f"Factorial of {number} is {factorial}.")