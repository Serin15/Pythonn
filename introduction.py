"""Write a Python program to convert the temperature in degree centigrade to Fahrenheit"""

def celsius_to_fahrenheit(celsius):
     fahrenheit = (celsius * 9/5) + 32
     return fahrenheit

celsius = float(input("enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")



c = input("enter temperature in Centigrade: ")
f = (9*(int(c))/5)+32
print("Temperature in Fahrenheit is:", f)



celsiustemp = int(input("Enter the temperature in Celsius: "))

fahrenheittemp = (celsiustemp * 9 / 5) + 32

print("The temperature in Fahrenheit is: ", fahrenheittemp)

"""Python code to find the circumference and area of a circle with a given radius"""

radius = float(input("input the radius of the circle :"))
circumference = 2 * 3.14 * radius
area = 3.14 * radius * radius

print("The circumference of the circle is: ", circumference)
print("The area of the circle is:", area)


"""Write a Python program to find the area of a triangle whose sides are given"""
import math


a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))


if a + b > c and a + c > b and b + c > a:

    s = (a + b + c) / 2

    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"The area of the triangle is: {area:.2f}")
else:
    print("The given sides do not form a valid triangle.")

"""Write a Python program to convert a given temperature in Fahrenheit to degrees Celsius."""



fahrenheit1 = float(input("enter temperaute in Fahrenheit: "))

celsius1 = (fahrenheit1 - 32) * 5 / 9

print(f"The temperature in Celsius is: {celsius1:.2f} C")


"""Write a Python program that takes the radius and height of a cylinder as inputs and calculates both its volume and surface area."""

import math

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))


# volume of a cylinder = pi x radius^2 x heitght

volume = math.pi * radius * radius * height

# Surface Area of a Cylinder: = 2 x pi x radius x ( radius + height )

surface_area = 2 * math.pi * radius * (radius + height)

print(f"The volume of the cylinder is: {volume:.2f}")
print(f"The surface area of the cylinder is: {surface_area:.2f}")


"""Write a Python program to convert a given length in kilometers to miles."""
# Miles=Kilometers × 0.621371  formula

kilometers =  float(input("enter distance in kilometers: "))

miles = kilometers * 0.621371

print(f"The distance in miles is: {miles:.2f}")

"""Write a Python program that calculates the simple interest given the principal, rate of interest, and time in years."""

# Simple_interest = principal x rate of interest x time / 100
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (%): "))
time = float(input("Enter the time in years: "))

simple_interest = (principal * rate * time) / 100

print(f"The simple interest is: {simple_interest:.2f} ")

