
user_name = input("Enter your first name: ")
user_surname = input("Enter your last name: ")
user_age = int(input("Enter your age: "))

with open("udaje.txt", "w") as file:
    file.write(f"{user_name} {user_surname} {user_age}")

"""
verzia cez json
import json
save_data = {
        'user_name': user_name,
        'user_surname': user_surname,
        'user_age' : user_age
}

with open("udaje.json", "w") as file:
    json.dump(save_data, file)
"""