print('Hello world')


def print_hello_world_twice():
    print('1')
    print('2')


def print_hello_world_multiple_times(times):
    for i in range(1, times):
        print('hello ' + i)


def print_squares_of_numbers(number):
    for i in range(1, number + 1, 1):
        print(i * i)


def print_multiplication_table(table, start, end):
    for i in range(start, end + 1):
        print(f"{table} X {i} = {table * i}")


def print_multiplication_table_default(table=4, start=1, end=10):
    for i in range(start, end + 1):
        print(f"{table} X {i} = {table * i}")
    print()


# print_multiplication_table_default()
# print_multiplication_table_default(5)
# print_multiplication_table_default(2,10,20)


# print_multiplication_table(8,1,10)
# print_hello_world_twice()
# print_hello_world_multiple_times(10)
# print_squares_of_numbers(10)

# no explicit return type in python methods.
def sum_of_two_numbers(n1, n2):
    sumn = n1 + n2
    return sumn


print(sum_of_two_numbers(1, 2))
