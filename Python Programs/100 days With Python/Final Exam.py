# Final Exam - Programming with Python
# Gaurav Agarwal - Bcom Prog - 2422178

#write a program to count the frquency of a given element in the following list 
L = [1,1,2,2,2,2,3,3,3,4,4,4,4,5,6,8,8,8,8,8]
element = int(input("Enter the element to count : "))
count_of_Element = L.count(element)
print(f"The frequency of {element} = {count_of_Element}")

print("\n" *2)
#Write a program that prints the rhe following without using an nested loop.
print("The required pattern is")
for a in range(1, 6):
    print('#' * a)
