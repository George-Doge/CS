# bonus vypis ascii

print("ASCII TABLE")

print("Dec\tHex\tOct\tChr")
for i in range(32):
    print(f"{i}\t{hex(i)}\t{oct(i)}\t{chr(i)}")

print("\nDec\tHex\tOct\tChr")
for i in range(32, 64):
    print(f"{i}\t{hex(i)}\t{oct(i)}\t{chr(i)}")

print("\nDec\tHex\tOct\tChr")
for i in range(64, 96):
    print(f"{i}\t{hex(i)}\t{oct(i)}\t{chr(i)}")

print("\nDec\tHex\tOct\tChr")
for i in range(96, 128):
    print(f"{i}\t{hex(i)}\t{oct(i)}\t{chr(i)}")
