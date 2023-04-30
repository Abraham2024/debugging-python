import random

n = random.random()

print(n)
# generates a random number from the range of numbers
a = random.randint(0, 3)
print(a)

# generates a random number from 100 to 200
b = random.randint(100, 200)
print(b)

#  we can use for loop in randint();
rand_list = []
# numbers printed  is 5
for i in range(0, 5):
# randint prints 5 random numbers from 0 - 50
    n = random.randint(0, 50)
# rand_list.append(n) compiles the statement
    rand_list.append(n)
print(rand_list)

rand_array = []
for i in range(0, 10):
    d = random.randint(0, 1000)
    rand_array.append(d)
print(rand_array)

# we can also use sample() to generate a random list of numbers and assigning a range
random_list = random.sample(range(10, 50), 10)
print(random_list)