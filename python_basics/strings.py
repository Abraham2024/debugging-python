a = "good morning"
print(a)
# you can find the position of a character
b = "hello world"
print(b[0])
#print specific characters from their positions
c = "hello"
print(c[2:4])
# to print strings in a loop using for
for d in "friend":
     print(d)
# to print the length of a string
e = "elephant"
print(len(e))
# to  check for word in a string and if true print a text, there must be a space after an if statement
f = "i am a good boy"
print("boy" in f)
print("girl" in f)
if "boy" in f:
     print("my name is Abraham")
# to slice a string from beginning or end
#from position 3 to 
g = 'hello world'
print(g[:3])
#from 3 to end
print(g[3:])
#negative slicing
print(g[-5:-2])
# to change a string to uppercase
h = "good day"
print(h.upper())
#to change string to lower
print(h.lower())
# to remove whitespace from beginning to end
i = "    hello, world    "
print(i.strip())
# to replace a text or word in a string
print(i.replace("hello", "good morning"))
# to split a string into substrings
print(i.split(","))
#string concatenation
print(a + " " + b )
#how to combine strings and integers, we use {} as an argument
# and format()
age = "27"
j = "john is {} years old"
print(j.format(age))
height = "5.7"
k ="Ade is {}m tall"
print(k.format(height))
age = "38"
height = "6.1"
position = "11"
l = "John is {} years old, {}m tall and he came out {}th in class"
print(l.format(age, height, position))
quantity = "10"
item = "101"
price = "150000"
m = "i will pay #{2} for {1} bags of rice in {0} section of the warehouse"
print(m.format(quantity, item, price))
