from random import shuffle

def shuffle_string(input_string):
    length = len(input_string)
    if length < 4:
        print("The string needs to have more than 4 characters.")

    else:
        while True:
            first_letter = input_string[0]
            last_letter = input_string[-1]

            list_string = list(input_string)
            list_string.remove(first_letter)
            list_string.remove(last_letter)

            shuffle(list_string)
            list_string.insert(0, first_letter)
            list_string.insert(length, last_letter)

            output_string = ""
            output_string = output_string.join(list_string)

            if output_string != input_string:
                return output_string



input_string = input("Please enter a string with 4 or more characters: ")
answer = shuffle_string(input_string)
print(f"The switched word is: {answer}")