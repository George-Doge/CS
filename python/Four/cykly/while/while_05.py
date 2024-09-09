S1 = r' ______  _______ __   _ _     _  _____  _______ _______ _______'
S2 = r' |_____] |_____| | \  | |____/  |     | |  |  | |_____|    |   '
S3 = r' |_____] |     | |  \_| |    \_ |_____| |  |  | |     |    |   '
print(S1, '\n', S2, '\n', S3, '\n')

suma = input("Napiste sumu, ktoru chcete vybrat ")
a = 0
b = 0
c = 0
d = 0
astr = ""
bstr = ""
cstr = ""
dstr = ""
if suma[-1] == "0":
    suma = int(suma)
    while suma > 0:
        if suma >= 100:
            suma -= 100
            a += 1
            if a > 0:
                astr = str(a) + "x100 "
        elif suma >= 50:
            suma -= 50
            b += 1
            if b > 0:
                bstr = str(b) + "x50 "
        elif suma >= 20:
            suma -= 20
            c += 1
            if c > 0:
                cstr = str(c) + "x20 "
        elif suma >= 10:
            suma -= 10
            d += 1
            if d > 0:
                dstr = str(d) + "x10 "
        else:
            print("ERROR")
        print(f"Bolo vam vydanych {astr}{bstr}{cstr}{dstr}eur.")
else:
    print("Bankomat nevie vydat tuto sumu.")
