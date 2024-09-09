farby_dictionary = {
    "biela": "white",
    "cierna": "black", 
    "cervena": "red",
    "modra": "blue",
    "zlta": "yellow",
    "zelena": "green"
}

def farba(input_colour):
    return farby_dictionary.get(input_colour, "pink")


input_colour = input("Napis farbu (malymi pismenami a bez diakritiky): ")

output_colour = farba(input_colour)

print(f"Suvisiaca farba pre tkinter je: {output_colour}")