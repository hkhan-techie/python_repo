x = "awesome"


def myfunc():
    print("Python is " + x)


myfunc()


def myfunc2():
    x = "fantastic"
    print("Python is " + x)


myfunc2()
print("Python is " + x)


def myfunc3():
    global x
    x = "fantastic"


myfunc3()

print("Python is " + x)
