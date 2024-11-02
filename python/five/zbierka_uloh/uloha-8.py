# uloha 8

text_input = input("Zadaj spravu: ")


text_input = text_input.split(" ")
pocet_slov = len(text_input)

text_output = ""

for slovo in text_input:
    slovo = slovo.capitalize()
    text_output += slovo

print(f"Pocet slov: {pocet_slov}\nKRatka sprava:{text_output}")