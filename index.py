      
# Q-1 Write a Python program that declares two variables a and b. Assign them any values of your choice. Print the result of their sum, difference, 
# multiplication, and division.
 
a = 25
b = 4

print(a+b)        #Sum
print(a-b)        #Difference
print(a*b)        # Multiplication
print(a/b)        #Division


#   Q-2 Write a Python program that demonstrates the use of single-line and multi-line comments. Inside the program, print "Hello, Python!"
#   as an example output.

# This is a single-line comment

"""
This is a multi-line comment
It can span multiple lines
"""

print("Hello, Python!")

# Q-3 Write a Python program that declares a variable name and assigns your name to it. Then, print a greeting 
# message such as "Hello, [Your Name]!"


name = "Amina"

print("Hello" +name +"!")

# Q-4 Write a Python program that accepts a number from the user, converts it to a float, and then converts the same number
# to an integer. Print both the float and integer values.

num = input("Enter Your Number:")

float_num = float(num)
int_num =  int(float_num)


print(float_num)
print(int_num)


# Q-5 Write a Python program that declares three variables: an integer, a float, and a string. Assign them values 
# and print their data types using the type() function.

x = 8
y = 4.5
v = "ICodeGuru"

print(type(x))
print(type(y))
print(type(v))


# Q-6 Write a Python program to calculate the area of a rectangle. Take the length and width as inputs from the user a
# nd print the calculated area.

length = int(input("Enter the length:"))
width  = int(input("Enter the width:"))

area = length * width

print("Area of the Rectangle is:", area)

# Q-7 Write a Python program that initializes a variable x with the value 10. Then, use assignment operators 
# (+=, -=, *=, /=, etc.) to modify and print the value of x.


x = 10

x += 6
print(x)
x -= 4
print(x)
x *= 3
print(x)
x /= 5
print(x)

# Q-8 Write a Python program that takes two numbers as input and compares them using comparison operators (>, <, >=, <=, ==, !=). 
# Print the results of the comparisons

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Compare the numbers using comparison operators
print(num1 > num2)
print(num1 < num2)
print(num1 >=num2)
print(num1 <=num2)
print(num1 ==num2)
print(num1 !=num2)


# Q-9 Write a Python program that takes two integers as input. Use logical operators to check if both numbers are greater than 0.
# Print an appropriate message based on the result.

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

if num1 > 0 and num2 > 0:
    print ("Both Numbers Are Greater Than 0")

else:
    print("At least One Number Is Greater Than 0")


# Q-10 Write a Python program that checks whether the string 'Python' is present in a list of programming languages: 
# ['Java', 'Python', 'C++', 'JavaScript'].Use the in operator to check and print the result.


languages = ['Java', 'Python', 'C++', 'JavaScript']

if 'Python' in languages:
    print("Python is present in list of programming languages")
else:
    print("Python is not present in list")

# Q-11 Write a Python program that compares two variables x and y using the identity operators (is and is not).
# Assign any values to x and y and print the result of the comparison.

x = 10
y = 10

print("x is y", x is y)
print ("x is not y", x is not y)


# Q-12 Write a Python program that takes two integers as input from the user. Perform addition, subtraction, multiplication,
# and division on these numbers and print the results.


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


print( num1 + num2)
print( num1 - num2)
print( num1 * num2)
print( num1 / num2 )


# Q-13 Write a Python program that takes a string input from the user, converts it into an integer, 
# and multiplies it by 10. Print the result.



user_input = input("Enter a number: ")
number = int(user_input)

result = number * 10

print("The result is:",result)


# Q-14 Write a Python program that initializes two boolean variables a and b with True and False, respectively.
# Use logical operators (and, or, not) and print the results of the operations.

a = True
b = False

print(a and b)
print(a or b)
print(not a)
print(not b)


# Q-15 Write a Python program that takes an integer as input from the user and checks whether the number is even or odd. 
# Print the appropriate message.

number = int(input("Enter an integer: "))


if number % 2 == 0:
    print("number is even")
else:
    print("number is odd")











