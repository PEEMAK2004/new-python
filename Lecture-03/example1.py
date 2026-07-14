text = input("Enter a string: ")
vowels = "aeiouAEIOU"
for char in text:
    if char in vowels:
        print(char + "*", end="")
    else:
        print(char.upper(), end="")
       

