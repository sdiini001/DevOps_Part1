# dictionaries
# key-value pairs
students_dictionary = {1: 'Rachel', 2:'Rafaella', 3:'weronica'}
print(students_dictionary)
print(type(students_dictionary))
# keys are 1, 2, 3
# values are rachel, rafaella, weronica
print(students_dictionary[1])

students_dictionary = {'one': 'Rachel', 'two':'Rafaella', 'three':'weronica'}
print(students_dictionary)
print(type(students_dictionary))

print(students_dictionary['three'])
# ?????
students_dictionary['four'] = 'steff'
# change item 1
students_dictionary['one'] = 'Aisha'





# sets
# sets are unique
# there are no duplicates in sets, but there is in dictionaries, tuples, lists
# they do not repeat values in the set
# they don't print sets in the order they are written/ not sequences
favourite_colours = {'green', 'blue', 'black', 'yellow','green'}
print(favourite_colours)
print(type(favourite_colours))
# print(favourite_colours[0]) not subscriptable

address = '736 Springfield Avenue'
print(address)

address = ', Springfield'
print(address)

address += '\tMA'
print(address)
