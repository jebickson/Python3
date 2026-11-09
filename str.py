"""In Python, string methods (str methods) are built-in functions used to manipulate and work with text."""
from idlelib import replace

#variables = values
name = ("\t Jebickson Samuel ")

Hobbie = "Education"
Love = "Math"
Laugh = "Life is Easy or Hard we have live it that was the fact"
quote_of_life = """Happy Sad Stress and more type os Emotion that show by human
beings and we have to live with flow of life and it was important to go with flow....Otherwise
you never get what you want"""

#-------------------------
#Case Conversation Method
#-------------------------

#UPPERCASE
jebiupper = name.upper()
print(jebiupper)

#------------------------
#Case Conversation Method
#------------------------

#upper() = Convert to Uppercase
print(name.upper())

#lower() = Convert to lowercase
print(name.lower())

#capitalize() = First letter uppercase
print(name.capitalize())

#title() = First letter of each word uppercase
print(name.title())

#swapcase() = reverse letter cases
print(name.swapcase())

#--------------------
#Searching Methods
#----------------------

#find() = Finds position of Text
print(name.find("a"))

#index() = Finds position and raises error if missing
print(name.index("m"))

#count() = count occurrences
print(name.count("e"))

#startswith() = checking starting characters
print(name.startswith("J"))

#endswith() = checking ending characters
print(name.endswith("e"))

#------------------------------
#Removing Spaces and Characters
#------------------------------

#strip() = Remove spaces from both ends
print(name.strip())

#rstrip() = Remove spaces from right side
print(name.rstrip())

#lstrip() = Remove spaces from left side
print(name.lstrip())

#-------------------------------
#Replacing and splitting methods
#-------------------------------

#replace() = Replace Text
print(name.replace("Jebickson Samuel","Rosie"))

#split() = Split string in a list
print(name.split())

#splitlines() = split line by line
print(name.splitlines())

#join() = joins strings
print(" ".join(name))

#--------------------------
#Checking Methods (Boolean)
#----------------------------
#These methods return True or False.

#isalpha() = Checks alphabetic characters
print(name.isalpha())

#isdigit() = Checks digits
print(name.isdigit())

#isalnum() = Checks letters and numbers
print(name.isalnum())

#islower() = Checks lowercase
print(name.islower())

#isupper() = Checks uppercase
print(name.isupper())

#istitle() = Checks title case
print(name.istitle())

#isspace() = Checks Whitespace
print(name.isspace())

#isascii = Checks ASCII Character
print(name.isascii())

#isdecimal() = Check decimal
print(name.isdecimal())

#isnumeric() = Check numeric
print(name.isnumeric())

#-------------------------
#Other Method
#-------------------------

#center() = Center text
print(name.center(100))

#ljust() = Aligns text left
print(name.ljust(10))

#rjust() = Aligns text right
print(name.rjust(100))

#zfill() = Add zeros to left
print(name.zfill(100))

#removeprefix()= Remove prefix
print(name.removeprefix("Jebickson"))

#removesuffix() = Removes a suffix
print(name.removesuffix("Sam"))

#partition() = split into three parts
print(name.partition(name))

#expandtabs() = Expands tab character
print(name.expandtabs())



