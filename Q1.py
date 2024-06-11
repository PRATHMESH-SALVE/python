A=int(input("enter your age"))
if A > 18:
    print("you can vote")
else:
    print("you cannot vote")

Q2
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))


largest = max(num1, num2, num3)


print(f"The largest number is: {largest}")

Q3
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


largest = max(num1, num2, )


print(f"The largest number is: {largest}")

Q4
number = int(input("enter a number"))
if number % 2 == 0:
    print("the number is even")
else:
    print("the number is odd")

Q5
char = input("enter a character")
if char.islower():
    print(char.upper())
elif char.isupper():
    print(char.lower())
else:
    print("enter a valid character")

Q6

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

Q7
number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

Q8
char = input("Enter a character ").lower()


if char in 'aeiou':
    print("Vowel")
else:
    print("Not a vowel")
    
