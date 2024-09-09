word = input("Napis slovo: ")
new_word = ""

for letter in word:
    new_word += letter
    new_word += "*"


print(f"Nove slovo je {new_word[:-1]}")