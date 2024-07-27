from operator import attrgetter

marks = [23,45,56]
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

animals =['Cat', 'Dog']
animals.append('Fish')
print(animals)
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

for number in sorted(numbers, key=len, reverse=True):
    print(number)

class Country:

    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __repr__(self):
        return repr((self.name, self.population))

countries = [Country('India', 120), Country('China',140)]
countries.append(Country('USA',190))

countries.sort(key=attrgetter('population'), reverse=True)
print(max(countries, key=attrgetter('population')))
print(min(countries, key=attrgetter('population')))

numbers_length_four = [number for number in numbers if len(number)>=4]
print(numbers_length_four)