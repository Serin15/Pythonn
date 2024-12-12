#generate OTP
import random,math

from beginner.introduction import circumference


def generateOTP():
    digits = ("0123456789")
    OTP = " "
    for i in range(1,5):
        a = random.random()
        b = math.floor(a*10)
        OTP += str(b)
    return OTP
print("OTP of 4 digits", generateOTP())

#Math Module Operations You have been tasked with writing a Python
#program that utilizes the math module to perform various mathematical calculations.

"""Question 1: Calculate the square root of the sum of two numbers.

Prompt the user to enter two numbers.

Calculate the sum of the two numbers.

Compute the square root of the sum using the math.sqrt() function.

Display the square root of the sum." """

import math

number1 = float(input("Insert first number: "))
number2 = float(input("Insert second number: "))

sum = number1 * number2

square_root = math.sqrt(sum)

print(f"The square root is {square_root}")


"""Question 2: Calculate the circumference and area of a circle.

Prompt the user to enter the radius of a circle.

Calculate the circumference of the circle using the formula 2 * math.pi * radius.

Calculate the area of the circle using the formula math.pi * radius ** 2.

Display the circumference and area of the circle."""

import math
radius = float(input("Insert the radius of a circle :"))
circumferencee = 2 * math.pi * radius
area = math.pi * radius ** 2

print(f"The circumference and area : {circumferencee} {area}")


