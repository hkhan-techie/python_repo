def my_function():
    print("Hello, Welcome to Technoflix Technologies")


my_function()


# Arguments
def my_function(fname):
    print(fname + " John")


my_function("Jim")
my_function("Jockey")
my_function("Emilly")


# Two arguments, you can pass as many as you want.
def my_function(fname, lname):
    print(fname + " " + lname)


my_function("Jim", "Kennedy")


# Arbitrary Arguments, *args
def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Jim", "John", "Elly")


# Keyword Arguments - order of the arguments does not matter
def my_function(child3, child2, child1):
    print("The youngest child is " + child1)


my_function(child1="Jim", child2="John", child3="Elly")


# Arbitrary Keyword Arguments, **kwargs -
# function will receive a dictionary of arguments, and can access the items accordingly
def my_function(**kwargs):
    print("His last name is " + kwargs["lname"])


my_function(fname="John", lname="Kennedy")


# Default parameter value
def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# Passing a List as an Argument, pass any datatype it will be treated same inside the function.
def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)


# Return Values - To let a function return a value, use the return statement.
def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))


# Pass statement to define empty function
def myfunction1():
    pass


# Recursion example
def try_recursion(k):
    if (k > 0):
        result = k + try_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
try_recursion(5)
