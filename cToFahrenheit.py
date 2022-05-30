def celsius_converter(celsius):
    return (celsius * 9/5) + 32

celsius = int(input("how many celsisus degrees do you want to convert to fahrenheit ? : "))

print( str(celsius) + "°C is " + str(celsius_converter(celsius)) + "°Fahrenheit")