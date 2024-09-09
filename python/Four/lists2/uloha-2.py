input_list = []
for i in range(10):
    input_list.append(int(input("Enter a number: ")))


def counter(input_list):
    output_list = []
    for number in input_list:
        if input_list.count(number) == 1:
            output_list.append(number)

    print(output_list)

counter(input_list)