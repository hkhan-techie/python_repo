i = 1
while i < 5:
    print(i)
    i += 1

# while and break
i = 1
while i < 5:
    print(i)
    if i == 3:
        break
    i += 1

# while and continue
i = 1
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# while and else
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
