from math import sqrt

print("a*x^2 + a*b + c = 0")
param_a = float(input("Zadaj parameter a: "))
param_b = float(input("Zadaj parameter b: "))
param_c = float(input("Zadaj parameter c: "))

discriminant = param_b**2 - 4*param_a*param_c

if discriminant < 0:
    print("Riesenie v R neexistuje.")

elif discriminant == 0:
    answ_x = (-param_b+sqrt(discriminant))/(2*param_a)
    print(f"Riesenie je {round(answ_x, 2)}")

else:
    answ_x1 = (-param_b+sqrt(discriminant))/(2*param_a)
    answ_x2 = (-param_b-sqrt(discriminant))/(2*param_a)
    print(f"Riesenia su {round(answ_x1, 2)} a {round(answ_x2, 2)}")