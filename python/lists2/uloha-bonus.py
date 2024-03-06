from random import randint

first_number_list = []
second_number_list = []
answers_list = []
points = 0

# generates questions
for i in range(10):
    first_number_list.append(randint(0, 10))
    second_number_list.append(randint(0, 10))

    # generates answers
    answers_list.append(first_number_list[i] * second_number_list[i])


# starts questions
print("You will have 10 questions to answer, from basic multiplication.")

for i in range(0, len(answers_list)):
    answer = int(input(f"{first_number_list[i]}*{second_number_list[i]} = "))

    if answer == answers_list[i]:
        print("Correct!")
        points += 1

    else:
        print(f"Wrong! {answers_list[i]} was correct.")
        # points -= 1

print(f"You have earned {points} points!")
