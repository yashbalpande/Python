# Day 1: Print Function

The print() function is fundamental in Python for displaying output to the console. It allows you to output text, numbers, and other information.

#Variable
A variable is used to store a value in a memory location within a program. When defining names or certain words as variables, enclose them in either single ('') or double ("") quotation marks. Numeric values can be defined directly without the need for commas or quotes.


name = "Yash"
age = 19
college = "GCOEN"

print(name, age, college)

There are rules for identifiers:

Variables cannot be separated; they must be added together.
Special symbols like !, @, $, % are not permitted in identifiers.
Identifiers can be of any length.

# Data Types
Python has five specific data types:

Integer (e.g., 1, 2, 3)
Float (e.g., 1.2, 2.3333)
String (used to define any text)
Boolean (True or False)
Complex number (e.g., 1i)
Types Of Operators
Arithmetic Operations (+, -, *, /, %, **)
Relational/Comparison Operations (==, !=, >, <, >=, <=)
Assignment Operators (=, +=, -=, =, /=, %=, **=)
Logical Operators (not, and, or)
Input in Python
The input() function is used to accept user input.

# Questions Based on this Day 1
Question 1: Write a program to input 2 numbers & print the sum...


a = float(input("Enter the Value of a: "))
b = float(input("Enter the Value of b: "))

add = a + b
sub = a - b
mul = a * b
div = a / b

print("Sum:", add, "\nDifference:", sub, "\nProduct:", mul, "\nQuotient:", div)
Question 2: Write a program to input the side of a square & print its area.


side = int(input("Enter the value of side of square: "))
area = side * side
print("Area of square:", area)
Question 3: Write a program to input 2 numbers & print the average.


c = float(input("Enter the Value of c: "))
d = float(input("Enter the Value of d: "))
average = (c + d) / 2
print("Average:", average)
Question 4: Write a program to input 2 numbers a and b. Print True if a is greater than or equal to b; if not, print False.


o = int(input("Enter the Value of o: "))
p = int(input("Enter the Value of p: "))

if o >= p:
    print(True)
else:
    print(False)

    
Feel free to reach out if you have any questions or need further clarification!
