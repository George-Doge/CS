# uloha 30

'''
Zadajte email: michal.velky@mail.pythonsoftware.net 
TLD: .net
Server: mail.pythonsoftware.net 
User: michal.velky 
Domény: 
Doména 1. úrovne je: net 
Doména 2. úrovne je: pythonsoftware 
Doména 3. úrovne je: mail
'''

tld_string = ""

# velky_string = input("Zadajte emailovu adresu: ")
velky_string = "michal.velky@mail.pythonsoftware.net"

velky_string = velky_string.split("@")
user_string = velky_string[0]
server_string = velky_string[1]

domeny = server_string.split(".")

print(f"User: {user_string}\nServer: {server_string}")

pocet_domen = len(domeny)

for i in range(pocet_domen, 0, -1):
    print(f"Domena {i} urovne: {domeny[i-1]}")