import random

for i in range(9):
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    
    for i in range(1, a+1):
        print(b * "*")
        
    print("")