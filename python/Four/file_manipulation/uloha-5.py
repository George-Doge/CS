meno = input("Napis meno suboru, ktory chces precitat (spolu s priponou): ")

# to try: except tu je aby program nespadol ked nenajde subor, cisto teoreticky to tu nemusi byt
try:
    with open(f"{meno}", "r") as file:
        print(file.read())

except FileNotFoundError as e:
    print(e)