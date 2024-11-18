"""Write a program to determine whether a person is eligible to vote"""

age = int(input(print("Enter your age: ")))
if(age>=18):
    print("eligible for voting!")
print("your age is:")
print(age)

"Write a python code to check the entered character is alphabet or digit"

ch = input("enter any charachter")

if(ch.isalpha()):
    print("Characher is alphabet")
if(ch.isdigit()):
    print("Charachter is digit")
if(ch.isspace()):
    print("character is Space")

"""Write a Python program to check whether the given number is even or not"""
number = int(input("Write a number: "))
if number % 2 == 0:
    print(f"{number} is even")
else:
    print("Number is not even")

"""Write a Python program to check whether the given integer is a multiple of both 5 and 7"""

number = int(input("Enter an integer: "))
if (number%5==0) and (number%7==0):
    print(number, "is a multiple of both 5 and 7")
else:
    print(number, "is not a multiple of both 5 and 7")

"""Write a Python program to find the roots of a quadratic equation"""
import math
a = float(input("Enter the first coefficient: "))
b = float(input("Enter the second coefficient: "))
c = float(input("Enter the third coefficient: "))
if (a!=0.0):
      d = (b*b)-(4*a*c)
      if (d==0.0):
             print("The roots are real and equal.")
             r = -b/(2*a)
             print("The roots are ", r,"and", r)
      elif(d>0.0):
                print("The roots are real and distinct.")
                r1 = (-b+(math.sqrt(d)))/(2*a)
                r2 = (-b-(math.sqrt(d)))/(2*a)
                print("The root1 is: ", r1)
                print("The root2 is: ", r2)
        else:
              print("The roots are imaginary.")
              rp = -b/(2*a)
              ip = math.sqrt(-d)/(2*a)
              print("The root1 is: ", rp, "+ i",ip)
              print("The root2 is: ", rp, "- i",ip)
else:
      print("Not a quadratic equation.")