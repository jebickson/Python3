#Create variables for your name, age, and college.
"""name = "jebi"
age = 20
college = "Korea University"
print(f"My name is {name}, I am {age} years old, and I study at {college}.")
"""
#Create two integer variables and calculate their sum.

"""a = 10
b = 20
sum = a + b
print(f"The sum of {a} and {b} is {sum}.")"""


#Store your marks in a list.
"""a = [85, 90, 78, 92, 88]
print(f"My marks are {a}.")
print(type(a))"""

#Create a dictionary containing student details
"""a = {"name": "jebi", "age":20, "college": "Korea University"}
print(f"My details are {a}.")"""

#Create a tuple containing five subjects.
"""a = ("Math", "Physics", "Chemistry", "Biology", "English")
print(f"My subjects are {a}.")"""

#Find the data type of 10, 10.5, "Hello", and True.
"""print(type(10))
print(type(10.5))
print(type("Hello"))
print(type(True))"""

#Convert a string "250" into an integer.
"""a = "250"
b = int(a)
print(f"The string '{a}' converted to an integer is {b}.")"""

#Create a set containing duplicate numbers.
"""a = {1,2,3,4,4,5,5}
print(f"The set with duplicates removed is {a}.")"""

#Check whether a variable is an integer using isinstance().

"""some_variable = 10.9
if isinstance(some_variable, int):
    print(f"{some_variable} is an integer.")
else:
    print(f"{some_variable} is not an integer.")"""


#Demonstrate mutable and immutable data types.

"""set = {1, 2, 3}  
frozenset =frozenset({1, 2, 3})


print(type(set))
set.add(4)  # Modifying the set
set.remove(1)
print(f"Modified set: {set}")
print(type(frozenset))"""

#Calculator using arithmetic Operator 
"""
def calculator():
    print("=" * 30)
    print(" Simple Calculator")
    print("=" * 30)
    print("Operations avaliable:")
    print("1. Addition(+)")
    print("2. Subtraction(-)")
    print("3. Multiplication(*)")
    print("4. Division(/)")
    print("5. Floor Division(//)")
    print("6. Modulus(%)")
    print("7. Exponentiation(**)")
    print("=" * 30)

    # Get user input for the operation
    num1 = float(input("Enter the first number:"))
    operator = input("Enter operator (+, -, *, /, //, %, **): ")
    num2 = float(input('Enter the second number:'))

    # Perform calculation
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    elif operator == '//':
        result = num1 // num2
    elif operator == '%':
         if num2 != 0:
            result = num1 % num2
         else:
            print("Error: Division by zero is not allowed!")
            return
    elif operator == '**':
        result = num1 ** num2
    else:
        print("Invalid operator")
        return

    print(f"The result of {num1} {operator} {num2} = {result}")

calculator()"""

#Version 2: Calculator With Continuous Loop

"""def calculator():
    print("Simple Calculator (type 'exit' to quit)")

    while True:
        try:
            num1 = input("\n Enter first number (or 'exit'): ")

            if num1.lower() == 'exit':
                print("Goodbye!")
                break
            num1 = float(num1)
            operator = input("Enter operator (+, -, *, /, //, %, **): ")
            num2 = float(input("Enter second number: "))

            if operator == '+':
                print(f"Result: {num1 + num2}")
            elif operator == '-':
                print(f"Result: {num1 - num2}")
            elif operator == '*':
                print(f"Result: {num1 * num2}")
            elif operator == '**':
                print(f"Result: {num1 ** num2}")
            elif operator == '/':
                if num2 != 0:
                    print(f"Result: {num1 / num2}")
                else:
                    print("Error: Division by zero is not allowed!")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
calculator()"""
