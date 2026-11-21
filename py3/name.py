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

# Real-World Example: Object Validation
"""
user = None
if user is None:
    print("User not logged in")
else:
    print("User logged in")
    """

#Student Data Analysis System
"""name = input("Enter student name: ")

#Student marks
maths = float(input("Enter Maths marks: "))
science = float(input("Enter Science marks: "))
computer = float(input("Enter Computer marks: "))


#Attendance perceentage
attendance = float(input("Enter attendance percentage: "))

#Arithmetic operating
total = maths + science + computer
average = total / 3

# Comparison and logical operations
if average >= 90 and attendance >- 75:
    result = "Excellent"
elif average >= 60 and attendance >= 75:
    result = "Pass"
else:
    result = "Fail" 

#Display results
print("\n --------------STUDENT ANALYSIS -----------")
print("Student Name:", name)
print("Total Marks:", total)
print("Average Marks:", average)
print("Attendance Percentage:", attendance)
print("Result:", result)"""

# Check whether a number is positive, negative or zero

"""num = int(input("Enter a number:"))

if num > 0:
    print(f"{num} is a positive number.")
elif num < 0:
    print(f"{num} is a negative number.")
else:
    print(f"{num} is zero.")"""

# Check whether a number is even or odd

"""num = int(input("Enter a number:"))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")"""

# Find the largest of two numbers

"""a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest number: ", a)
elif b > a:
    print("Largest number: ", b)
else:
    print("Both numbers are equal")"""

#Check whether a person is eligible to vote

"""age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")"""

#check whether a year is leap year

"""year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")"""

#Student grade calculation
"""
mark = int(input("Enter your mark: "))

if mark < 0 or mark > 100:
    print("Invalid marks")
elif mark >= 90:
    print("Grade A")
elif mark >= 80:
    print("Grade B")
elif mark >= 70:
    print("Grade C")
elif mark >= 80:
    print("Grade D")
elif mark >= 50:
    print("Grade E")
else:
    print("Fail")"""

# Simple Calculator using match-case
"""
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operator = input("Enter operator(+,-,*,/): ")

match operator:
    case "+":
        print("Result:", num1 + num2)
    case "-":
        print("Result:", num1 - num2)
    case "*":
        print("Result:", num1 * num2)
    case "/":
        print("Result:", num1 / num2)
    case _:
        print("Invalid operator")"""

#Login authentication with username and password

"""correct_username = "admin"
correct_password = "python123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username:
    if password == correct_password:
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Invalid username")"""

#E-cormmerce discound calculation
"""amount = float(input("Enter purchase amount: "))

if amount < 0:
    print("Invalid amount")
else:
    if amount >= 100:
        discount = 20
    elif amount >= 5000:
        discount = 10
    elif amount >=2000:
        discount = 5
    else:
        discount = 0
    discount_amount = amount * discount / 100
    final_amount = amount - discount_amount

    print("Purchase amount:", amount)
    print("Discount:", discount, "%")
    print("Discount amount:", discount_amount)
    print("Final amount:", final_amount)"""

# ATM withdrawal validation

"""balance = 10000

withdraw = int(input("Enter withdrawal amount: "))

if withdraw <= 0:
    print("Invalid withdrawal amount")
elif withdraw % 100 != 0:
    print("Enter amount in multiples of 100")
elif withdraw > balance:
    print("Insufficient balance")

else:
    balance = balance - withdraw

    print("withdrawal successful")
    print("Remaining balance:", balance)
"""

# Banking transaction management

"""balance = 10000

while True:

    print("\n======== BANKING SYSTEM========")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            print("Current balance:", balance)
        case 2:
            amount = float(input("Enter deposit amount: "))

            if amount > 0:
                balance += amount
                print("Deposite successful")
                print("New balance:", balance)
            else:
                print("Invaild amount")
        case 3:
            amount = float(input("Enter withdrawal amount: "))

            if amount <=0:
                print("Invaild amount")
            elif amount > balance:
                print("Insufficient balance")
            else:
                balance -= amount
                print("Withdrawal successful")
                print("New balance:", balance)
        case 4:
            print("Thank you for banking")
            break
        case _:
            print("Invalid choice")"""

#Employee salary and tax calculation

"""salary = float(input("Enter annual salary: "))

if salary < 0:
    print("Invaild salary")

else:
    if salary <= 30000:
        tax_rate = 0
    elif salary <= 60000:
        tax_rate = 5
    elif salary <= 1000000:
        tax_rate = 10
    else:
        tax_rate = 20

    tax = salary * tax_rate / 100
    net_salary = salary - tax

    print("Annual salary:", salary)
    print("Tax rate:", tax_rate, "%")
    print("Tax amount:", tax)
    print("Net salary:", net_salary)
    """

#E-commerce shopping cart checkout
"""
products = {
    "laptop": 50000,
    "mouse": 500,
    "Keyboard": 1500,
    "monitor": 12000
}
print(type(products))
cart = {}

while True:
    print("\n========PRODUCT STORE =============")

    for product, price in products.items():
        print(product,":",price)
    choice = input("\n Enter product name or 'done': ").lower()

    if choice == "done":
        break

    if choice not in products:
        print("Product not available")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Invaild quantity")
        continue

    cart[choice] = cart.get(choice, 0) + quantity
total = 0

print("\n===== SHOPPING BILL ======")

for product, quantity in cart.items():

    price = products[product]
    subtotal = price * quantity

    total += subtotal

if total >= 500000:
    discount = total * 0.10

else: 
    discount = 0

final_amount = total - discount

print("\nTotal: ", total)
print("Discount:", discount)
print("Final amount:", final_amount)"""

#Multiple-condition user authentication
"""
correct_username = "admin"
correct_password = "python123" 
correct_otp = "4567"

account_active = True

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    if account_active:

        otp = input("Enter OTP: ")

        if otp == correct_otp:
            print("Authentication successful")
            print("Welcome to the system")
        else:
            print("Account is inactive")
else:
    print("Invalid username or password")"""

    