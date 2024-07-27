class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __repr__(self):
        return repr((self.name, self.address))


class Student(Person):
    def __init__(self, name, address, college, degree):
        super().__init__(name, address)
        self.college = college
        self.degree = degree

    def __repr__(self):
        return repr((super().__repr__(), self.college, self.degree))


person = Person('Hidayath', 'Tumkur')
student = Student('Azan', 'Tumkur', 'ABC', 'PUC')

print(person)
print(student)
