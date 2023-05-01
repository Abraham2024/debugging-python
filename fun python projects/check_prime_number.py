import random

lower = 1
upper = 500
for n in range(lower, upper +1):
    if n > 1:
        for i in range (2, n):
            if (n % i) == 0:
                break
            else:
                print(n)
#prints all the prime numbers in a range
lower = int(input("Enter the start of the range: "))
upper = int(input("Enter the end of the range: "))
for num in range (lower, upper +1 ):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
            else:
                print("the prime numbers from range is:", num )
                
                
# 
num1 = random.randint(0,100)
for prime in range (num1 + 1):
    if prime >1:
        for i in range(2, prime):
            if (prime % i) == 0:
                break
            else:
                print('{0} is a prime number', prime)