nazov = input("Napis aky chces nazov suboru bez pripony: ")

with open(f"{nazov}.txt", "w") as file:
    file.write("Ahoj, ja som subor")