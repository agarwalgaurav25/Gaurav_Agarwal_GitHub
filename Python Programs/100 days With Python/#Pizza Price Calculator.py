print("Hi , Welcome to Python Pizza Deliveries")
wish = str(input(" Do you want a pizza ? Y or N "))
bill = 0
a = 0
if wish == "Y":
#Check for Size of Pizza
    size = input("What size of Pizza do you want ?? S M or L ") 
    if size == "S":
        bill = 15
    elif size == "M":
        bill = 2
    elif size == "L":
        bill = 25
    else:
        print("Wrong input Run Again")
        exit()
#check for pepperoni
    pep = input("Do you want Pepporoni ? Y or N ")
    if pep == "Y":
            if size == "S":
                bill += 2
            else:
                 bill += 3

#Check for cheese
    cheese = input("Do you want Cheese ? Y or N ")
    if cheese == "Y":
        bill += 1
    print (f"Your Bill total = {bill}")
print("Thank you for visitng us")