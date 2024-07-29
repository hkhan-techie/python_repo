fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# Loop through the letters in the word "banana":
for x in "banana":
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

# Do not print banana:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# Using the range() function
for x in range(6):
    print(x)

# Using the start parameter
for x in range(2, 6):
    print(x)

# Increment the sequence with 3 (default is 1)
for x in range(2, 30, 3):
    print(x)

# Print all numbers from 0 to 5, and print a message when the loop has ended
for x in range(6):
    print(x)
else:
    print("Finally finished!")

for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)

# Pass an empty for loop
for x in [0, 1, 2]:
    pass
