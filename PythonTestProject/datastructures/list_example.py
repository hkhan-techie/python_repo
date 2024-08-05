from operator import attrgetter

marks = [23, 45, 56]
total = sum(marks)
min1 = min(marks)
max1 = max(marks)
print(f'sum {total}')
print(f'min {min1}')
print(f'max {max(marks)}')
print(f'len {len(marks)}')

marks.append(77)
print(f'append {marks}')

marks.remove(77)
print(f'remove {marks}')

animals = ['Cat', 'Dog']
animals.append('Fish')
print(animals)

# Extending the list
animals.extend(['Lion', 'Tiger'])
print(animals)

animals += ['Jackal', 10]
print(animals)

numbers = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven']
print(f'{numbers[2:6]}')
print(f'{numbers[:6]}')
print(f'{numbers[3:]}')
print(f'{numbers[1:6:2]}')
print(f'{numbers[1:6:2]}')
print(f'{numbers[-1]}')

for number in sorted(numbers, key=len, reverse=True):
    print(number)

numbers.insert(2, "Orange")
numbers[1:3] = ["blackcurrant", "watermelon"]
print(numbers)

# Remove the second item:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist.pop()
print(thislist)

del thislist[0]
print(thislist)

del thislist

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# Print all items by referring to their index number:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

# List Comprehension offers the shortest syntax for looping through lists:
# A short hand for loop that will print all items in a list:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

# Normal code without List Comprehension
for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# with List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# Only accept items that are not "apple"
newlist = [x for x in fruits if x != "apple"]

# Sort the list alphabetically:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)


# Sort the list based on how close the number is to 50:
def myfunc(n):
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

# Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)

# Reverse the order of the list items:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# copy
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
# copy
mylist = list(thislist)
print(mylist)

# Join two list:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Append list2 into list1:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)

# Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


class Country:

    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __repr__(self):
        return repr((self.name, self.population))


countries = [Country('India', 120), Country('China', 140)]
countries.append(Country('USA', 190))

countries.sort(key=attrgetter('population'), reverse=True)
print(max(countries, key=attrgetter('population')))
print(min(countries, key=attrgetter('population')))

numbers_length_four = [number for number in numbers if len(number) >= 4]
print(numbers_length_four)
