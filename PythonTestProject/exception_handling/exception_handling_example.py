try:
    i = 1
    number = 10 / i
except (ZeroDivisionError, ValueError):
    number = 0
else:
    print('else')
finally:
    print('finally')

print(number)

try:
    i = 0
    number1 = 10 / i
except ZeroDivisionError as error:
    # except ZeroDivisionError:
    print(error)
    # print("ZeroDivisionError")
    number1 = 0
else:
    print('else1')
finally:
    print('finally1')

print(number1)


def test(number, i):
    print("------test-----")
    try:
        return number / i
    except (ZeroDivisionError, ValueError):
        print("Error")
    finally:
        print('finally')
    return 0


print(test(10, 1))
print(test(10, 0))

try:
    f = open("demofile.txt")
    try:
        f.write("Demo data")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")
