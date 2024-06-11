char = input("enter a character")
if char.islower():
    print(char.upper())
elif char.isupper():
    print(char.lower())
else:
    print("enter a valid character")