print("!!!RETAZCE MUSIA MAT ROVNAKU DLZKU!!!")
string_one = input("Zadaj prvy retazec: ")
string_two = input("Zadaj druhy retazec: ")

new_string = ""

if len(string_one) != len(string_two):
    print("Retazce musia mat rovnaku dlzku")

for i in range(len(string_one)):

    new_string += string_one[i]
    new_string += string_two[i]
    
print(f"Spojeny retazec je: {new_string}")