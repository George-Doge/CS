from math import sqrt, sin, cos

print("sqrt(sin(x)+cos(x))")
input_num = float(input("Enter x: "))

odpoved = sqrt(sin(input_num)+cos(input_num))

print(f"Riesenie rovnice sqrt(sin({input_num})+cos({input_num})) je {round(odpoved, 3)}.")
