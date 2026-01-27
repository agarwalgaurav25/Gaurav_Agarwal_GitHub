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

# num = 13
# i = 2
# while i < num:
#     if num % i == 0:
#         is_prime = False
#     elif num % i != 0:
#         is_prime = True
# if is_prime == True:
#     print("prime")
# else:
#     print("not prime")
# a = "hello"
# b = id(a)
# (a == b )
# #Write a program to solve a Quadratic Equation
# variables = {"a": 0,"b": 0,"c":0 }
# for i in variables:
#     variables[i] = int(input(f"Enter the value of {i}: "))

# print (variables)

def fizzBuzz(n) :
    if n % 3 == 0 :
        print("fizz")
    elif n % 5 == 0 and n % 3 == 0: 
        print("buzz")
    else :
        print (n)
    
n = int(input("enter the integer"))
a = 0 
while a < n :
    fizzBuzz(a)
    a += 1

