list1 = ["stolicka", "macka", 3, "pes"]
list2 = ["chatgpt", 151, "ananas", "10"]

def spoj_zoznamy(output_zoznam, list_two):
    
    for item in list_two:
        output_zoznam.append(item)


    return output_zoznam


print(spoj_zoznamy(list1, list2))