print("Program to check eligibility to vote")
name = input("enter your name")
age = int(input("enter age"))
if age >= 18:
    print(name, "is Eligible to Vote")
else:
    print(name, "is not eligible to vote")
