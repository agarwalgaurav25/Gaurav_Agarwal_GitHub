#Program to fnd eligibility to for anything

#Define Variables
minage = 21
efor = "to Drink"

print ("Program to check eligibility to vote")
name = input("enter your name")
age = int(input("enter age"))
Fname = str(input("enter father's name"))
if age >= minage:
    print ( f'{name} having the age of {age}yrs is eligible {efor}')
else:
    print ( f'{name} having the age of {age}yrs is not eligible {efor}')
    