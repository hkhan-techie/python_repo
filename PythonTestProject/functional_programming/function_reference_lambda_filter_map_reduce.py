import statistics
from functools import reduce


def multiply_by_2(data):
    return data * 2


def do_this_and_print(func, data):
    print(func(data))


do_this_and_print(multiply_by_2, 120)

func_example_reference = multiply_by_2
print(func_example_reference(24))

do_this_and_print(lambda data: data * 2, 125)
do_this_and_print(lambda data: data * 3, 125)
do_this_and_print(lambda data: data ** 3, 125)
do_this_and_print(lambda data: len(data), 'test')

# Filter implementation

numbers = [1, 89, 54, 35]
oddFilteredNumbers = list(filter(lambda x: x % 2 == 1, numbers))
print(oddFilteredNumbers)
print(list(filter(lambda x: x % 2 == 0, numbers)))

words = ['Apple', 'Ant', 'Bat']
print(list(filter(lambda x: x.endswith('at'), words)))
print(list(filter(lambda x: len(x) == 3, words)))

# Map implementation

print(list(map(lambda x: x.upper(), words)))

print(list(map(lambda x: x * x, range(1, 11))))

# Reduce implementation
numbers = [3, 15, 12, 10]
print(reduce(lambda x, y: x + y, numbers))
print(reduce(lambda x, y: x * y, numbers))
print(reduce(lambda x, y: max(x, y), numbers))
print(reduce(lambda x, y: min(x, y), numbers))

print(reduce(lambda x, y: x if len(x) > len(y) else y, words))

# combine filter, map, reduce implementation example

numbers = [3, 7, 8, 15, 24, 35, 46]

print(reduce(lambda x, y: x + y, map(lambda x: x * x, filter(lambda x: x % 2 == 0, numbers))))

# Other complex examples

months = [('Jan', 31), ('Feb', 28), ('Mar', 31)]
tuple_ex = ('Dec', 31)
print(tuple_ex[0], tuple_ex[1])
print(sum(map(lambda x: x[1], months)))
print(reduce(lambda x, y: x if x[1] < y[1] else y, months))
print(reduce(lambda x, y: x if x[1] < y[1] else y, months)[0])

marks = [10,20,40,60]

print('mean :',statistics.mean(marks))
