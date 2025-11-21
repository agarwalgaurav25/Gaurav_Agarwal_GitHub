# #Solve Quadratic Equation

# a = float(input("enter the value of a : "))
# b = float(input("enter the value of b : "))
# c = float(input("enter the value of c : "))

# def solve(a,b,c):
# 	det = (b**2) - (4*a*c)
# 	if det >= 0 :
# 		root1 = -(((b)- (det**0.5))/ (2*a))
# 		root2 = -(((b)+ (det**0.5))/ (2*a))
# 		print (f"""
# first root  = {root1}
# second root = {root2}""")
# 	else:
# 		print ( "The equation has no roots")

# solve(a,b,c)



# #Fibonacci Sequence 
# elements_needed = int(input("enter the number of elements needed in the sequence"))
# a = 0
# b = 1
# check = 0 
# seq = [a,b]
# while check < (elements_needed - 2):
# 	seq.append(a+b)
# 	c = a+b
# 	a = b
# 	b = c
# 	check += 1 
# 	print(seq)


# L1 = [1,2,3,4,5]
# L2 = ["one", "two", "three", "four","five"]
# D1 = {}
# b = 0
# while b < 5:
# 	D1[b]= L2[b]
# 	b += 1 	

# print (D1)

#Count the number of 


#letter
# def letters(string):
# 	letters_count = 0
# 	lowercase = 0
# 	uppercase = 0
# 	for a in string:
# 		letters_count += 1
# 		if a.isupper():
# 			uppercase += 1 
# 		if a.islower():	
# 			lowercase += 1
# 	print (f"""
# 	Total letters = {letters_count}
# 	Uppercase     = {uppercase}
# 	Lowercase     = {lowercase}""")
# Str = "I Love My Country ,India"
# No_space_string = "".join((Str.split(" ")))
# print(No_space_string)
# letters(No_space_string)

nos = [1,2,3,4,5,6,7,8,9,9,9,9,9,9]


# mode = 0

# mean = sum(nos)/len(nos)

# def median(numbers):
# 	nos = len(numbers)
# 	if len(numbers)% 2 != 0:
# 		median  = numbers[int(nos/2)]
# 	else:
# 		median =(((numbers[int((nos +1) / 2)]) + (numbers[int((nos -1)/ 2)]))) / 2
# 	print(median)
	

# def mode(nos):
# 	unique = set(nos)
# 	mode = 0
# 	for a in unique:
# 			mode_new = nos.count(a)
# 			if mode_new > mode:
# 				mode = mode_new
# 	print (mode)
	
	
# mode(nos)
# median(nos)
# print (mean)
# print(len(nos))

from statistics import mode
from statistics import median
from statistics import mean
print(mode(nos))
print(median(nos))
print(mean(nos))