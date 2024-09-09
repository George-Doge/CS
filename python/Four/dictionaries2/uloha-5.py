studenti = {
    "Peter":[80, 90, 85],
    "Anna":[75, 80, 82],
    "Tomas":[90, 92, 88]
}

vysledky = {}

# vypocita priemery a da ich do dict
for key, value in studenti.items():
    priemer = sum(value)/len(value)
    vysledky[key] = priemer

# printne priemery
print("Priemery:")
for key, value in vysledky.items():
    print(f"{key}:{value}")