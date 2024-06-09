# sms uloha

vstup_sprava = input("Napis spravu: ")

vstup_sprava = vstup_sprava.split()

pocet_slov = len(vstup_sprava)

vystup_string = ""

for slovo in vstup_sprava:
    vystup_string += slovo.capitalize()

print(f"Pocet slov v sprave: {pocet_slov}\nKratka verzia: {vystup_string}")