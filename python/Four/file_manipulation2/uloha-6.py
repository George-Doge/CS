with open("vstup50.txt", "r") as file:
    input_string = file.read()


output_string = ""
for letter in input_string:

    if 65 <= ord(letter) <= 90:
        output_string += "_"

    elif 48 <= ord(letter) <= 56:
        output_string += "_"

    else:
        output_string += letter

with open("vystup50.txt", "w") as file:
    file.write(output_string)