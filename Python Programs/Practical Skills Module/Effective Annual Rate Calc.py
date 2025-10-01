rate_of_interest = float(input("Enter the annual rate in decimals ( 10% = .1) = "))
compounding_Periods = int(input("Number of compounding periods in a year = "))
amt = int(input("enter the amount invested = "))
def EAR(i,m):
    return (round((((1+(i/m))**m)-1)*100,4))
print(f"eay ={EAR(rate_of_interest,compounding_Periods)}%")
per_period = (1 +(rate_of_interest/compounding_Periods))
eay = round((per_period**compounding_Periods)-1 ,4)
print (f"Effective Annual Rate = {eay*100}%")
interest = round((amt * (1+eay) - amt))
print (f"interest income = {interest}")
A = [-10,-30,-80.6,70,21.9]
B = [-3,7.3,4.7,6,8]

# snum = sum(A) + sum(B)
# print (round((abs(snum))))


# for i in A:
#     for j in B:
#         print (f"the absolute sum of {abs(i)} and {abs(j)} is {(round(sum((abs(i) ,abs(j)))))}")