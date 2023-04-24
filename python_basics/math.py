import math

#prints the value of any name
my_name = input("what is your name: ")
print("hello" + " " + my_name + " how are you doing?")

#prints the text in ""
print("do you want to take the physics/maths chat?")
answer= str(input("enter your answer: "))
print("lets continue")

#prints the square root of the variable number
number = float(input("enter any number to find its square root: "))
print("the square root of the number is:",math.sqrt(number))

# prints the square of the number
number_square =float(input("Enter any number to get the square: "))
print("The square of the number is: ", number_square * number_square)

# prints the value of the number in celcius
celc = float(input("Enter the number to be converted to kelvin: "))
print("in kelvin, it is:", celc + 273)

# prints the value of the weight of the body where g is acceleration due to gravity
print("assuming the acceleration due to gravity of a body is 10")
mass = float(input("enter the mass of the body: "))
g = 10
print("the value for weight = ", mass*g)

#prints the cosine value of any angle input
cos = float(input('Enter the angle to get the cosine value: '))
print("the cosine value is: ",math.cos(math.radians(cos)))

#prints the sine value of any angle given
sin = float(input("Enter the angle to be converted to sine: "))
print("the sin value is: ", math.sin(math.radians(sin)))

#prints the tan value of any angle inputed
tan = float(input("Enter the angle to get the tan value: "))
print("the tan value is: ", math.tan(math.radians(tan)))


# prints the area of a circle
pi_value = math.pi
radius = float(input("Enter the radius given to find the area of the circle: "))
print("The area of the circle is: ", pi_value*radius*radius)

# prints the value of the centripetal force
mass = float(input("Enter the mass given to solve for centripetal force: "))
velocity = float(input("Enter the velocity given: "))
radius = float(input('Enter the radius given: '))
print('The centripetal force in Newton=', (mass*velocity*velocity)//radius)

#prints the value of refractive index
critical_angle = float(input("Enter the angle to get the refractive index: "))
print("the refractive index is: ", 1/(math.sin(math.radians(critical_angle))))

#prints the value of the number in degree fahrenheit
temp = float(input("Enter any number in degree celcius to get its value in degree fahrenheit: "))
print("The value in degree Fahrenheit is: ", (9/5) * temp + 32)
