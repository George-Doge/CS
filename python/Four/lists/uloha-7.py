def print_type(list):
    for item in list:
        if type(item) == str:
            print(f"{item} - string")

        elif type(item) == int:
            print(f"{item} - int")

        elif type(item) == float:
            print(f"{item} - float")

        else:
            print(f"{item} - other")



list = [1, 5.0, "ahoj", 15, ()]
print_type(list)