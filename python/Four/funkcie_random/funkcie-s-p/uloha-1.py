#ULOHA 1
def multiprint(n, output):
    for i in range(n):
        print(output)

output = input("Aký je vstup ? ")
n = int(input("Koľko krát mám tento údaj vypísať? "))
multiprint(n, output)