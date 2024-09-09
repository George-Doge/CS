#ULOHA 2

def max2(a, b):
    if a > b:
        return a

    elif b > a:
        return b
    

a = int(input("Enter number A: "))
b = int(input("Enter number B: "))

print(f"{max2(a, b)} is bigger.")