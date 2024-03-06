def sequence(start, end, step):
    output_list = []

    if step == 0:
        print(output_list)

    elif step < 0:
        number = start
        while number > end:
            output_list.append(number)
            number += step


        print(output_list)

    else:
        number = start
        while number < end:
            output_list.append(number)
            number += step


        print(output_list)


sequence(20, 0, -2)