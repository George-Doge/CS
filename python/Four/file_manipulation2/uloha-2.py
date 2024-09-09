
year = 2024

with open("udaje.txt", "r") as file:
    data = file.read()

data = data.split()
born_year = year - int(data[2])

print(f"User's name is {data[0]} {data[1]} and is {data[2]} years old. The user was born in {born_year}.")

"""
json verzia
import json
with open("udaje.json", "r") as file:
    save_data = json.load(file)
    user_name = save_data.get('user_name')
    user_surname = save_data.get('user_surname')
    age = save_data.get('user_age')

born_year = year - age

print(f"User's name is {user_name} {user_surname} and is {age} years old. The user was born in {born_year}.")
"""