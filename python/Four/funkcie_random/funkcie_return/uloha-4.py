#ULOHA 4

def average_func(a, b):
    average = (a + b)/2

    return average 

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

average = average_func(a, b)

print(f"Average of {a} and {b} is {average}.")