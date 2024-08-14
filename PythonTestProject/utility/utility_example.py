# Import the module named mymodule, and call the greeting function:
import datetime
import json
import math
import platform
import re
from decimal import Decimal

import mymodule
import mymodule as mx

mymodule.greeting("Jonny")

# Import the module named mymodule, and access the person1 dictionary
a = mymodule.person1["age"]
print(a)

# Create an alias for mymodule called mx:
a = mx.person1["name"]
print(a)

# Import and use the built-in platform module:
x = platform.system()
print(x)  # OS name

# List all the defined names belonging to the platform module:
# x = dir(platform)
# print(x)

# Import the datetime module and display the current date:
x = datetime.datetime.now()
print(x)

# Return the year and name of weekday:
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

# Create a date object:
x = datetime.datetime(2024, 5, 17)
print(x)

x = datetime.datetime.now()
print(x.strftime("%B"))  # Month full name
print(x.strftime("%b"))  # Month short name
print(x.strftime("%m"))  # Month number
print(x.strftime("%H %M %S"))

# Python Math module

x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)

# The abs() function returns the absolute (positive) value of the specified number:
x = abs(-7.25)
print(x)

# Return the value of 4 to the power of 3 (same as 4 * 4 * 4):
x = pow(4, 3)
print(x)

x = math.sqrt(64)
print(x)

x = math.ceil(1.4)
y = math.floor(1.4)

print(x)  # returns 2
print(y)  # returns 1

# Convert from JSON to Python:
# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["city"])

# a Python object (dict):
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

# Convert Python objects into JSON strings, and print the values:

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x))

# RegEx expressions in Python
# Search the string to see if it starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

# Print a list of all matches:
# The list contains the matches in the order they are found.
txt = "The rain in Spain"
x = re.findall("in", txt)
print(x)

# No match
x = re.findall("Portugal", txt)
print(x)

# Search for the first white-space character in the string:
txt = "The rain in Spain"
x = re.search("\\s", txt)
print("The first white-space character is located in position:", x.start())

txt = "The rain in Spain"
x = re.split("\\s", txt)
print(x)

# Replace every white-space character with the number 9:
txt = "The rain in Spain"
x = re.sub("\\s", "9", txt)
print(x)

# Replace the first 2 occurrences:
x = re.sub("\\s", "9", txt, 2)
print(x)

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)  # this will print an object
x = re.search("aim", txt)
print(x)

# Search for an upper case "S" character in the beginning of a word, and print its position:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

# String formatting

price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

# Return "Expensive" if the price is over 50, otherwise return "Cheap":
price = 49
txt = f"It is very {'Expensive' if price > 50 else 'Cheap'}"
print(txt)

fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)


def myconverter(x):
    return x * 0.3048


txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# based on index
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

# Named index
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname="Hyundai", model="i10"))

print(4.5 - 3.2)
# use Decimal class for accurate results
value1 = Decimal('4.5')
value2 = Decimal('3.2')
print(value1 - value2)
