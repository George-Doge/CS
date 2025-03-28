import tkinter as tk

root = tk.Tk()
root.title("Login uloha")
root.geometry("400x400")

passwd = {}

with open("hesla.txt", "r") as file:
    data = file.readlines()
    for line in data:
        line = line.split()
        passwd[line[0]] = line[1]


# print(data, passwd)

def nove_okno():
    new_window = tk.Toplevel(root)
    new_window.title("Login uloha")
    new_window.geometry("200x100")
    label = tk.Label(new_window, text="SI PRIHLASENY")
    label.pack()


def login():
    meno = vstup_meno.get()
    heslo = vstup_heslo.get()

    spravne_meno = spravne_heslo = False

    print(meno, heslo)

    for key, value in passwd.items():
        if meno == key:
            spravne_meno = True

            if heslo == value:
                spravne_heslo = True


    if spravne_meno and not spravne_heslo:
        vysledok.config(text="Spravne meno, nespravne meno")

    elif spravne_meno and spravne_heslo:
        vysledok.config(text="Uspesny login!")
        nove_okno()

    else:
        vysledok.config(text="Nespravne meno")


    # vysledok.config(text=f"{spravne_meno}, {spravne_heslo}")    


nadpis_meno = tk.Label(root, text="Prihlasovacie meno:").pack()
vstup_meno = tk.Entry(root)
vstup_meno.pack()

nadpis_heslo = tk.Label(root, text="Heslo:").pack()
vstup_heslo = tk.Entry(root)
vstup_heslo.pack()

tlacidlos = tk.Button(root, text="potvrd", command=login).pack()

vysledok = tk.Label(root, text='')
vysledok.pack()

root.mainloop()