input_list = [3, 2.5, 0.5, 10, 1.2, 1.2]

def shop(input_list):
    final_price = 0
    for i in range(0, len(input_list), 2):
        final_price += input_list[i] * input_list[i+1]

    print(f"The final price is: {final_price}.")


shop(input_list)