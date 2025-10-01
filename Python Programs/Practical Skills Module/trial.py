
a = float(input("enter the value of a :"))
b = float(input("enter the value of b :"))
c = float(input("enter the value of c :"))

det = ((b**2) - (4 * a *c ))
if int(det) >= 0:
	root1 = (-b + (det**0.5)) / (2*a)
	root2 = (- b - (det**0.5))/(2 * a) 
	print ( f' the roots of the quadratic equation are {root1} and {root2}')
else:
	print("no roots exist")


# num = int(input("enter the number to check for prime or non prime : "))

# for a in range(2, num):
#     if num % a == 0:
#         print(f"{num} is a non-prime number")
#         break
# else:
#     print(f"{num} is a prime number")




# L = [34,67,89,91,95,99]
# print ("Original List" )
# print(L)

# print("list after eliminating 2nd element")
# L.pop(1)
# print (L)

# print("List after changing 5th element to 32")
# L[4] = 32
# print (L)


# a = 3 + 5/8
# print( a)
# b = int(3 + 5/8)
# print(b)
# c = 3 + float(5/8)
# print(c)
# d = 3 + float(5)/8
# print(d)
# e = 3 + 5.0/8
# print (e)
# f = int (3 + 5/7.0)
# print (f)