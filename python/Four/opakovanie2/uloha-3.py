items_list = ["stolicka", "co", "co", "gilotina", 420, 8, 127, 127]

def remove_duplicates(input_list):
    for item in input_list:
        if input_list.count(item) > 1:
            input_list.remove(item)

    return input_list


print(remove_duplicates(items_list))