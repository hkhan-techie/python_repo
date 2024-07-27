x = 5
y = "Jonny"
print(x)
print(y)

x = "Philip"  # x is now of type str
print(x)

x = str(3)  # x will be '3'
y = int(3)  # y will be 3
z = float(3)  # z will be 3.0

print(x, y, z)
print(f"x:{x} y:{y} z:{z}")

x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
# is the same as
x = 'John'

print(x)

a = 4
A = "Peter"
# A will not overwrite a
print(a, A)

# illegal variable names:
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# based on value of the variables implementation will change, ex: appending strings and sum of two numbers
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

# Error
# x = 5
# y = "John"
# print(x + y)
