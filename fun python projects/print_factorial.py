import random
factorial = 1
num = int(input("enter the number:"))
if num < 0:
    print("factorial does not exist for negative numbers")
elif(num==0):
    print("the factorial of 0 is 1")
else:
    for i in range(1, num+1):
        factorial = factorial * i
        print("the factorial of", num, "is" ,factorial)
