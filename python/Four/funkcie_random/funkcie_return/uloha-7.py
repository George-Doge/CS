#ULOHA 7

def number_of_divisors(number):
    count = 0

    for i in range(1, number+1):
        if number % i == 0:
            count += 1

    return count


def is_prime(count):
    if count > 2:
        return False
    
    return True


number = int(input("Enter a number: "))
count = number_of_divisors(number)
ans = is_prime(count)
print(f"Q:Is {number} a prime number?\nA:{ans}")