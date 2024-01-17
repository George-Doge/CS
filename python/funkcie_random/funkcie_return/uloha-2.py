#ULOHA 2

def even(number):
    if number % 2 ==0:
        return True
    
    else:
        return False

number = int(input("Enter a number: "))
answer = even(number)
print(f"Q:Is {number} even? \nA: {answer}")