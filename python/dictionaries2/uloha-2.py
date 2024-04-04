preklad = {
    "car":"auto",
    "chair":"stolicka",
    "cat":"macka",
    "dog":"pes",
    "computer":"pocitac",
    "game":"hra",
    "translator":"prekladac"
}

def translator(input_dict):
    score = 0
    # prejde cez hodnoty a prida body ak su spravne
    for key, value in input_dict.items():
        user_preklad = input(f"Napis preklad slova {key}: ")

        if user_preklad.lower() == value:
            print("Spravne")
            score += 1
        # skonci preklad ak bude nespravna odpoved
        else:
            print(f"Nespravne. Preklad bol {value}. Dosiahol si {score} bodov.")
            break


translator(preklad)