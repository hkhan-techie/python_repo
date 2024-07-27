occurances = dict(a=1,b=2,c=3)
print(occurances)
occurances['d'] = 4
print(occurances)
occurances.get('d')
print(occurances.keys())
print(occurances.values())

for(key, value) in occurances.items():
    print(f'{key} {value}')