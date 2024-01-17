import random
print("Play a game")
min = int(input("Enter minimal value: "))
max = int(input("Input maximal value: "))

correct_num = random.randint(min, max)
guess = 0
lives = 0


while guess != correct_num:
    while lives <= 10:  
        print(lives)
        guess = int(input("Guess a number: "))
        if guess < correct_num:
            print("Guess a bigger number.")
        elif guess > correct_num:
            print("Guess a smaller number.")
        lives += 1
    print("You lost, try again")
    input()
    
print("You won!")