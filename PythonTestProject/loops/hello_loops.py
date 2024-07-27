x1 = input('Enter the first number ')
x = int(x1)

x2 = input('Enter the Second number ')
y = int(x2)

print(('1- Add'))
print(('2- Subtract'))
print(('3- Multiply'))
print(('4- Divide'))
x3 = input('Enter your choice ')

choice = int(x3)

if choice == 1:
    print(f'Sum of {x} + {y} = {x + y}')
elif choice == 2:
    print(f'Subtract of {x} - {y} = {x - y}')
elif choice == 3:
    print(f'Product of {x} * {y} = {x * y}')
else:
    print(f'Division of {x} / {y} = {x / y}')

for ch in 'Hello world':
    print(ch)

for item in (3, 9, 7):
    print(item)

i = 1
while i * i < 100:
    print(f" square of i is {i * i}")
    i = i + 1

## do while implementation just like java

number = int(input('Enter number: '))
while number >= 0:
    print(f'cube is {number ** 3}')
    number = int(input('Enter number: '))