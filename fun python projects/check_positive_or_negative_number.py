import random
def Numbercheck(a):
    if a > 0:
        print("number given is positive")
    elif(a == 0):
        print("number given is zero")
    else:
        print("number is negative")
        
a = float(input("enter a number as input value: "))
(Numbercheck(a))

# to see if a random number chosen is positive, zero or negative
b = random.randint(-10, 10)
if b < 0:
    print(f"{b :d} is negative")
elif(b==0):
    print(f"{b :d} is zero")
else:
    print(f"{b :d} is positive")
    