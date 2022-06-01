"""" 
Realizar un programa que permita ingresar grados Fahrenheit y muestre por pantalla 
el  dato  en  grados  centígrados  o  pasar  de  grados  centígrados  a  grados  Fahrenheit 
(puede realizar cualquiera de los dos programas).
"""

# Pass from fahrenheit degrees to celsius
fahrenheit_degrees = float(input("Enter the number of fahrenheit degrees: \n"))
celsius = (fahrenheit_degrees - 32) / 1.8

print(f"The conversion from {fahrenheit_degrees} °F to Celsius is: {celsius} °C")