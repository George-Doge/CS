zoznam_veci = ["ananas", "macka", "macka", "pes", "ananas", "stolicka", "stol"]

def spocita_veci(input_list):
    output_dict = {}

    for item in input_list:
        output_dict[item] = input_list.count(item)

    return output_dict



print(spocita_veci(zoznam_veci))