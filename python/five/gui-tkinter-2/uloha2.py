# uloha 2, hesla
import tkinter as tk

root = tk.Tk()
root.title("Hesla uloha")
root.geometry("300x150")


def read_file():
    data_dict = {}
    with open("hesla.txt", "r") as file:
        data = file.read().split("\n")
        
    
    for line in data:
        line = line.split(" ")
        data_dict[line[0]] = line[1]


    return data_dict


def open_window():
    new_window = tk.Toplevel(root)
    new_window.title("Prihlasenie")
    new_window.geometry("200x100")
    label = tk.Label(new_window, text="SI PRIHLASENY")
    label.pack()



def login():
    login_data = read_file()

    spravne_meno = spravne_heslo = False

    login_meno = entry_meno.get()
    login_heslo = entry_heslo.get()

    for key, value in login_data.items():
        if key == login_meno:
            spravne_meno = True

        if value == login_heslo:
            spravne_heslo = True


    if not spravne_heslo or not spravne_meno:
        label_vystup.config(text="Zle meno alebo heslo, skus este raz!")

    else:
        label_vystup.config(text="")
        open_window()

label_meno = tk.Label(root, text="Zadaj meno:")
label_meno.pack()

entry_meno = tk.Entry(root)
entry_meno.pack()

label_heslo = tk.Label(root, text="Zadaj heslo:")
label_heslo.pack()

entry_heslo = tk.Entry(root)
entry_heslo.pack()

start_button = tk.Button(root, text="Login", command=login)
start_button.pack()


label_vystup = tk.Label(root)
label_vystup.pack()

root.mainloop()