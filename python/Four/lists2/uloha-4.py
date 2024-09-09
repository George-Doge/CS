names_list = ['hela', 'adam', 'boris', 'adela', 'bobo', 'miso', 'hektor', 'borka', 'mino']
beginning = "mi" # EDIT THIS VARIABLE TO CHANGE THE BEGINNING

def start(names_list, beggining):
    output_list = []
    beginning_length = len(beginning)

    for name in names_list:
        if name[0:beginning_length] == beginning:
            output_list.append(name)

    print(output_list)

start(names_list, beginning)
