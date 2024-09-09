zoznam_slov = ["pes", "mačka", "krava", "slon", "studio", "auto", "stolovanie"]

def zorad_dlzka(input_zoznam):
    output_zoznam = []

    output_zoznam = sorted(input_zoznam, key=len)

    return output_zoznam

print(zorad_dlzka(zoznam_slov))