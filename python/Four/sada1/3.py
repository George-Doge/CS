print("Binary to decimal converter")
binary = input("Enter a binary number: ")
binary_rev = binary[::-1]
decimal = 0

for i, number in enumerate(binary_rev):
    print(f"{number} * 2^{i}")
    decimal += int(number) * 2**i

print(f"Binary number '{binary}' is '{decimal}' in decimal.")