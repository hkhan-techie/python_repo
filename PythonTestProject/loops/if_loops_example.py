a = 33
b = 200
if b > a:
    print("b is greater than a")

# if b > a:
# print("b is greater than a")

a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# shorthand if :- If you have only one statement to execute, you can put it on the same line as the if statement.
if a > b: print("a is greater than b")

# shorthand if else
a = 2
b = 330
print("A") if a > b else print("B")

# And
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

# OR
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")

# Not
a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")

# Nested if
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# Pass
a = 33
b = 200

if b > a:
    pass
