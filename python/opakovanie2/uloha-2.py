numbers_tuple = (15, 184, 5, 111, 0, 45, 3)

def biggest_number(input_tuple):
    max_val = input_tuple[0]

    for number in input_tuple:
        if number > max_val:
            max_val = number

    return max_val


print(biggest_number(numbers_tuple))