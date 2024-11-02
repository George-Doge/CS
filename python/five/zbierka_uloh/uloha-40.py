# uloha 40

from random import choice

input_slovo = input("Zadaj slovo (min. 4 znaky): ")

if len(input_slovo) < 4:
    print("Kratke slovo")
else:
    prve_pismeno = input_slovo[0]
    posledne_pismeno = input_slovo[::-1][0]

    index_posledny = len(input_slovo)-1
    stred = input_slovo[1:index_posledny]

    stred_list = []
    # premena stringu stred na list
    for pismeno in stred:
        stred_list.append(pismeno)

    output_slovo = prve_pismeno

    for i in range(len(stred)):
        vyber = choice(stred_list)
        output_slovo += vyber
        stred_list.remove(vyber)

    output_slovo += posledne_pismeno

    print(output_slovo)