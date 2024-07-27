class Test1:
    def method(self): print('Test1')

class Test2:
    def method(self): print('Test2')

    def method2(self): print('Test3')

tests = [Test1(), Test2()]

for test in tests:
    test.method()