i = 1
while i < 6:
    print(i)
    i += 1 
    
# a break statement can be used to stop the loop if the conditions are true
a = 1
while a < 6:
    print(a)
    if (a == 3):
       break
    a += 1
    
#continue is used to stop the current iteration and goes to the next so d condition wont be printed

b = 1
while b < 9:
    b += 1
    if b == 4:
        continue
    print(b)
    
# if the condition is not true the continue doesnt work
c = 11
while c > 15 and c < 20:
    c +=1
    if c == 18:
        continue
    print(c)

#you can also use else statement in loops
d = 1
while d > 4:
    print(d)
    d += 1
else:
    print("good morning")
    
#
days =["monday", "tuesday", "wednesday", "thursday", "friday"]
for x in days:
    print(x)

# if y gets to apple and the condition is true the loop ends
fruits = ['mango', "orange", "banana", "apple", "cherry"]
for y in fruits:
    if y == "apple":
        break
    print(y)
    
    
#
colours = ["red", "white", "blue", "green", "purple"]
for j in colours:
    if j == "blue":
        continue
    print(j)
    
# range does not add the number of the range like range (10) is between 0- 9
for v in range(4):
    print(v)
    
# we can also specify the start of the range loop
#by specifying the start of the loop number it starts from the first number
#but doesnt include the last number
for u in range(5, 12):
    print (u)

# we can also specify the number it increments by adding a third value in the range

for k in range(9, 81, 9):
    print(k)
    
#using nested loops in range
num = [1, 2, 3, 4, 5]
colours = ["red", "blue", "grey"]
for g in num:
    for h in colours:
        print(g, h)