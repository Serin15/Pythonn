"Write a program to find factorial of a given number"
n = int(input("enter value of n: "))
f = 1
if(n<0):
    print("n must be non negative value")
else:
    for i in range(1,n+1):
        f = f*i
    print("factorial result is: ", f)


"Write a program to display the cube of the number up to given an integer."

n = int(input("Enter an integer: "))

print("Cube of numbers from 1 to", n)
for i in range(1, n+1):
    cube = i ** 3
    print(f"{i}^3 = {cube}")

"Write a program to display the sum of digits in a given number"

n = int(input("Enter any number: "))
total = 0
while(n>0):
    d = n % 10
    total = total + d
    n = n // 10
print("sum of digits : ", total)

"Write a Python program to find out the average of a set of integers"

count = int(input("Enter the count of numbers: "))
i = 0
sum = 0
for i in range(count):
        x = int(input("Enter an integer: "))
        sum = sum + x
avg = sum/count
print(" The average is: ", avg)

"Write a Python program to generate the prime numbers from 1 to N"
num =int(input("Enter the range: "))

for n in range(2,num):
      for i in range(2,n):
            if(n%i==0):
                      break
      else:
            print(n)

"Write a Python program to display the given integer in reverse"
n=int(input("enter an integer:"))

a=(str(n)[::-1])

print(a)