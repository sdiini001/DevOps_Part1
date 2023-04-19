# range

for number in range(1, 4, 2):
    print(number)

one, two, three = range(1, 4)
# extended iterable unpacking
one, two, *three = range(1, 8)

print(one, two, three)

names = ["steff", "anum", "saynab"]
print(names)
print(names[2])
print(names[-1])
print(names[1:])
print(names[1:3])
del names[1:]

names +=['Aisha', ' Rafaella']
print(names)

names.extend(['Rachel', 'Indie'])
print(names)

# Adds to end of list
names.append('weronika')
names.append('Mariam')

names.insert(1,'Iman')

print(names)

names[:0] = ['Dominique', 'Deanne']
names.insert(0,'Angel')
print(names)
# .pop takes out last name
# shows which name was popped
popped_name = names.pop()
print(names)
print(popped_name)

names.pop(3)
print(names)

# to remove a specific name in long list
names.remove("Indie")
print(names)
names.insert(0, 'steff')
names.insert(7, 'steph')
where_is_steph = names.index('steph')
print(where_is_steph)
# what if both steff's had same spelling and you removed one
# which one would you remove
print(names)
names.remove('steff')
print(names)

# sorting list reverse  alphabetical order
names.sort(reverse=True)
print(names)

# it takes each item in list
# orders name according to length
names.sort(keys=len)
print(names)
sorted_names = sorted(names, reverse=True)
print(sorted_names)
