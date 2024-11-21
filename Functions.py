#cube value of a given number
def cube(x):
    return(x*x*x)
num = 5
result = cube(num)
print("Cube of",num,"=",result)

#find Maximum/Minimum among two given numbers
def findMax(x,y):
    if x>y:
        return x
    else:
        return y
def findMin(x,y):
    if x<y:
        return x
    else:
        return y
a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
print("Maximum value = ", findMax(a,b))
print("Minimum value = ", findMin(a,b))

# Nested function
def cube(x):
    c = x*x*x
    def square(x):
        s = x*x
        print(s)
    square(n)
    print(c)
n = int(input("Enter a value: "))
cube(n)

def cube(x):
    def square(x):
        s = x*x
        return s
    c = square(n)*x
    print(c)
n = int(input("enter a value: "))
cube(n)

"Write a Python program to print the numbers from a given number n till 0 using recursion"

def print_numbers(n):
    if n < 0:
        return
    print(n)
    print_numbers(n - 1)
start_number = int(input("Enter a number :"))
print_numbers(start_number)

"Write a Python program to find the factorial of a number using recursion"
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


number = int(input("Enter a number: "))
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {number} is {factorial(number)}")

"Write a Python program to find the Nth term in a Fibonacci series using recursion"
def Fib(n):
       if n<0:
          print("The input is incorrect.")
       elif n==1:
          return 0
       elif n==2:
          return 1
       else:
          return Fib(n-1)+Fib(n-2)
print(Fib(7))