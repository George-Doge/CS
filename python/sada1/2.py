message = input("Enter an SMS message: ")
short = ""
        
words_list = message.split()
number_words = len(words_list)
print(words_list)

short = short.join(words_list)
             

print(f"Number of words:\n{number_words}\nShortened message: \n{short}")