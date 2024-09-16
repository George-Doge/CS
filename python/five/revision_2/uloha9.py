# uloha 9

print("x^2+bx+c=0")
premenna_a = float(input("Zadaj hodnotu premennej 'a': "))
premenna_b = float(input("Zadaj hodnotu premennej 'b': "))
premenna_c = float(input("Zadaj hodnotu premennej 'c': "))

if premenna_a == 0:
    print("Zadana rovnica nie je kvadraticka.")

else:
    diskriminant = premenna_b**2-4*premenna_a*premenna_c

    if diskriminant < 0:
        print("Riesenie v rovine R neexistuje.")

    else:
        x_1 = (-premenna_b+diskriminant**(1/2))/(2*premenna_a)
        x_2 = (-premenna_b-diskriminant**(1/2))/(2*premenna_a)

        if diskriminant == 0:
            print(f"Rovnica ma jedno riesenie {round(x_1, 3)}")

        else:
            print(f"Rovnica ma dve riesenia: x1 {round(x_1, 3)} x2 {round(x_2, 3)}")