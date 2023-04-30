#import cmath
import math

a = float(input("enter the value of a: "))
b = float(input("enter the value of b: "))
c = float(input("enter the value of c: "))
# calculate the discriminant that is b square - 4ac
d = (b**2)- (4*a*c)

#possible solutions
sol1 = (-b-math.sqrt(d))/ (2*a)

sol2 = (-b + math.sqrt(d))/ (2*a)

print("the solutions are {0} and {1}".format(sol1,sol2))