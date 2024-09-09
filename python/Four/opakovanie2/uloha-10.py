zoznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def rozdel_zoznam(input_zoznam, length):
    # in order to work properly, the length main list should be divisible by the desired length of the sub-lists 
    if length == 0 or len(input_zoznam) % length != 0:
        return "Invalid length number, please change it."

    output_zoznam = []
    
    delta = 0

    while len(output_zoznam) < len(input_zoznam)/length:
        temp_zoznam = []
        for i in range(delta, length + delta):
            temp_zoznam.append(input_zoznam[i])
            delta = i+1

        output_zoznam.append(temp_zoznam)

    return output_zoznam


print(rozdel_zoznam(zoznam, 4))