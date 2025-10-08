# pv = int(input("enter the present value =\n"))
# fv = int (input("enter the expected future value =\n"))
# r = float(input("Enter the annual interest rate = \n"))
# y = 1
# fv_check = 0
# while y >0:
#     pv = round(pv *((1+r)**y),2)
#     y += 1 
#     print (f' FV at yr {y} is {pv}')
#     if pv > fv:
#         break
    
# print(f'it would take {y} yrs approx to generate wealth equal to or above {fv}')

num = 13
i = 2
while i < num:
    if num % i == 0:
        is_prime = False
    elif num % i != 0:
        is_prime = True
if is_prime == True:
    print("prime")
else:
    print("not prime")
