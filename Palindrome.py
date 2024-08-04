a=input("Enter a string:")
def palindrome():
    if a==a[::-1]:
       print("palindrome")
    else:
       print("not palindrome")
palindrome()