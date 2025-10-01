bill = int(input("Enter the total Bill amount = "))
ppl = int(input("How many people are there = "))
tip = int(input("What %  of  bill you wanna tip = "))

split = round(( ((bill * (1+(tip/100)))/ppl)),2)

print(f"each person has to pay = {split}")