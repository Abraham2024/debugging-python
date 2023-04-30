#from celcius to kelvin
temp_1 = float(input("Please enter the temperature in Celcius: "))
convert_kelvin = temp_1 + 273
print("%.2f degree celcius is equal to %.2f kelvin" % (temp_1, convert_kelvin))

# from kelvin to celcius
temp_2 = float(input("please enter the temperature in kelvin: "))
convert_temp = temp_2 - 273
print("%.2f degree kelvin is equal to %.2f degree celcius" % (temp_2, convert_temp))
