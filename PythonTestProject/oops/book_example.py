# class Book:
#     pass
#
# book1 = Book()
# book2 = Book()
# print(book1)
# print(book2)

class Book:

    def __init__(self, name, copies):
        self.name = name
        self.copies = copies


    def __repr__(self):
        return repr((self.name, self.copies))

    # def __str__(self):
    #     return str((self.name, self.copies))
    def increase_copies(self, how_much):
        self.copies+=how_much

    def decrease_copies(self, how_much):
        self.copies-=how_much

book1 = Book('Spring', 40)
book2 = Book('Python',33)
book1.increase_copies(10)
book2.decrease_copies(3)
print(book1)
print(book2)

class Country:

    def __init__(self, name='Default'):
        self.name =name
        print('Constructor 2')

    def instance_method(self):
        print('instance method')

def_country = Country()
india = Country('India')

print(def_country.name)
print(india.name)
print(india.instance_method())