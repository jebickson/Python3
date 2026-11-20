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

#Login Validation System

"""correct_username = "jebi"
correct_password = "1234"

username = input("Enter username:")
password = input("Enter password:")

if username == correct_username and password == correct_password:
    print("Login succcessful!")
else:
    print("Invalid username or password.")"""

# Login Validation Using or

"""username = input("Enter username:")

if username == "jebi" or username == "admin":
    print("Login successful!")
else:
    print("Invalid username.")"""

#Login Validation Using not
"""
password = input("Enter password:  ")

if not password==123 :
    print("Password cannot be empty.")
else:
    print("Password accepted.")"""

# Basic Shopping Cart Program

"""product_name = "Laptop" 
price = 50000
quantity = 2

total = price * quantity

print("Product:", product_name)
print("Price:", price)
print("Quantity:", quantity)
print("Total:", total)"""

# Shopping Cart with Discount
"""product_name = "Mobile"
price = 15000
quantity = 2

total = price * quantity

if total >= 10000:
    discount = total * 0.10
else:
    discount = 0

final_price = total - discount

print("Product:", product_name)
print("Total:", total)
print("Discount:", discount)
print("Final Price:",final_price)"""

#Shopping Car with Multiple Products

"""laptop_price = 50000
mouse = 500
keyboard = 1000

laptop_quantity = 1
mouse_quantity = 2
keyboard_quantity = 1

laptop_total = laptop_price * laptop_quantity
mouse_total = mouse * mouse_quantity
keyboard_total = keyboard * keyboard_quantity

cart_total = laptop_total + mouse_total + keyboard_total

if cart_total >= 10000:
    discount = cart_total * 0.10
else:
    discount = 0

final_price = cart_total - discount

print("Laptop Total:", laptop_total)
print("Mouse Total:", mouse_total)
print("Keyboard Total:", keyboard_total)
print("Cart Total:", cart_total)
print("Discount:", discount)
print("Final Price:", final_price)
"""

#Basic Search Using

"""products = ["Laptop", "Mobile", "Mouse", "Keyboard"]

search = input("Enter product name: ")

if search in products:
    print("Product found!")
else:
    print("Product not found!")"""

#Search Using not in

"""students = ["Sam", "John","David", "Alex"]

name = input("Enter student name:")

if name not in students:
    print("Student not found!")
else:
    print("Student found!")
    """

# Case-Insensitive Search
#The following program allows users to search without worrying about uppercase or lowercase letters.

"""products = ["Laptop", "Mobile", "Mouse", "Keyboard"]

search = input("Search products: ").lower()

#Convert all products to lowercase

products = [product.lower() for product in products]

if search in products:
    print("product available")
else:
    print("product not available")"""

#Search Functionality Using Dictonary

"""products = {
    "Laptop" : 50000,
    "mobile" : 20000,
    "mouse" : 500,
    "keyboard" : 1000
}

search = input("Enter product name:").lower()

if search in products:
    print("Product found! Price:", products[search])
else:
    print("Product not found!")"""