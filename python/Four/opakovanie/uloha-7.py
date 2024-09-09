hour = int(input("Zadaj pocet hodin: "))
minute = int(input("Zadaj pocet minut: "))

seconds = 0 

seconds += (hour * 60 * 60) + minute * 60

print(f"V prepocte to je {seconds} sekund.")