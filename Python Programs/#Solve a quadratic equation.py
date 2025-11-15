#Solve a quadratic equation
a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))

def solve(a,b,c):
    det = (b**2)- (4*a*c)
    if det >= 0:
        root1 = -(b-(det**.5)/(2*a))
        root2 = -(b+(det**.5)/(2*a))
        return f"the roots are {root1} and {root2}"
    else:
        return "the eqaution has imaginary roots"
    
print (solve(a,b,c))