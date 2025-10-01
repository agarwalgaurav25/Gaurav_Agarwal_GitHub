#Program to fnd eligibility to for anything

#Define Conditions
minage = 18 #minimum age for the purpose
efor = "to Drink" #purpose


print ("Program to check eligibility ", efor)
name = input("enter your name")
age = int(input("enter age"))
Fname = str(input("enter father's name"))
state = str(input('enter name of state'))
if state == "Gujarat":
    print (name," lives in a dry state")
    a2 = 0
else:
    print (name, " doesnt live in a dry state")
    a2 = 1

if age >= minage:
    print ( f'{name} having the age of {age}yrs is eligible {efor}')
    a1 = 1
else:
    print ( f'{name} having the age of {age}yrs is not eligible {efor}')
    a1 = 0
print (a2 and a1 == 1)
