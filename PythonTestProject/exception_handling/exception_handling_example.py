try:
    i=1
    number =10/i
except (ZeroDivisionError, ValueError):
    number =0
else:
    print('else')
finally:
    print('finally')

print(number)

try:
    i=0
    number1 =10/i
except ZeroDivisionError as error:
    print(error)
    number1 =0
else:
    print('else1')
finally:
    print('finally1')

print(number1)