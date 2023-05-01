# checks if a random number is an even or odd number
import random
n = random.randint(10, 200)
# if the remainder is equal to zero its even where % is remainder otherwise its odd
if n % 2 == 0 :
    print(f"{n :d} is even")
else:
    print(f'{n :d} is odd')