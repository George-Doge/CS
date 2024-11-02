# uloha 37 no-gui

vaha = float(input("Zadaj hmotnost v kg: "))
vyska = float(input("Zadaj vysku v m: "))

bmi = vaha/vyska**2

print(f"BMI index: {round(bmi, 5)}")

if bmi < 18.5:
    print("Podvaha")

elif bmi < 25:
    print("Normalna hmotnost")

elif bmi < 30:
    print("Nadvaha")

else:
    print("Obezita")