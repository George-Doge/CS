def spoj(list):
    odpoved = ""
    for word in list:
        odpoved += f"{word} "

    return odpoved


slova = ["Jano", "nepi", "vodu"]
print(spoj(slova))