# zisti palindrom
import tkinter as tk

root = tk.Tk()
root.geometry("400x400")
root.title("Palindrom")

def palindrom():
    slovo = vsup_slovo.get()
    slovo_otocene = slovo[::-1]

    if len(slovo) <= 1:
        vystup.config(text="Zadaj slovo")
    elif slovo == slovo_otocene:
        vystup.config(text="Je to palindrom")
    else:
        vystup.config(text="Slovo nie je palindrom")
    
    # print(slovo, slovo_otocene)


label_vstup = tk.Label(root, text="Napis slovo:").pack()
vsup_slovo = tk.Entry(root)
vsup_slovo.pack()

button_vstup = tk.Button(root, text="Test na palindrom", command=palindrom)
button_vstup.pack()
vystup = tk.Label(root, text="")
vystup.pack()

root.mainloop()