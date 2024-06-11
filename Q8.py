number = float(input("Enter a number: "))

if number < 0:
    print("less than 0")
elif number < 10:
    print("between 0 and 10")
elif number < 20:
    print("between 10 and 20")
elif number < 30:
    print("between 20 and 30")
else:
    print("30 or greater")