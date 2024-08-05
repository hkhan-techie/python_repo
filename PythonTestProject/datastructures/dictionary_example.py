occurrences = dict(a=1, b=2, c=3)
print(occurrences)
occurrences['d'] = 4
print(occurrences)
occurrences.get('d')
print(occurrences.keys())
print(occurrences.values())

for (key, value) in occurrences.items():
    print(f'{key} {value}')
