"Write a Python program to display the sum of n numbers using a list"
numbers = []
num = int(input("How many numbers:"))
for n in range(num):
    x = int(input("Enter number :"))
    numbers.append(x)
print("Sum of numbers in the given list is:", sum(numbers))

"Write a Python program to implement linear search"

numbers = [4,2,7,1,8,3,6]
f = 0
x = int(input("Enter the number to be found out: "))
for i in range(len(numbers)):
      if (x==numbers[i]):
          print(" Successful search, the element is found at position", i)
          f = 1
          break
if(f==0):
      print("Oops! Search unsuccessful")

"# Python program to implement linear search for strings"

strings = ["apple", "cars", "bmw", "banana"]
x = input("Enter the string you want to find: ")
for i in range(len(strings)):
    if x == strings[i]:
        print(f"Search successful! The string '{x}' was found at position {i}.")
        break
else:
    print(f"Oops! The string '{x}' was not found in the list.")

"Write a Python program to find the odd numbers in a List"

numbers = [1, 2, 3, 4, 5, 6]
odd_numbers = []
for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)
print("The odd numbers in the list are:", odd_numbers)

"Write a Python program to print all the items in a dictionary"

phone_book = { 'John' : [ '8592970000', 'john@xyzmail.com' ],
                              'Bob': [ '7994880000', 'bob@xyzmail.com' ],
                              'Tom' : [ '9749552647' , 'tom@xyzmail.com' ] }
for k,v in phone_book.items():
     print(k, ":", v)



my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "job": "Engineer"
}
print("Dictionary items:")
for k,v in my_dict.items():
    print(f"{k}: {v}")