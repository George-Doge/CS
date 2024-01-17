#ULOHA 5
def palindrome(r):
    if r == r[::-1]:
        return True
    else:
        return False

r = input("Enter a string to find out if it is a palindrome: ")
print(palindrome(r))