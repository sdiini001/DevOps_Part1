euro_as_unicode = "\u20ac"
print(euro_as_unicode)

euro_as_symbol_name = "\N{euro sign}"
print(euro_as_symbol_name)

pizza = "\N{Slice of pizza}"

print(pizza)


# print function is a variadic function
# it accepts a flexible(variable) number of args- argument
print('one', 'two', 'three')

print('one', 'two', 'three', sep='_', end=' .\t')
print('four', 'five', 'six', end= '\n\n')
print('seven', 'eight', 'nine')

# concatenation

address_parts = ['Bart Simpson', '742 Evergreen Terrace', 'Springfield', 'MA', 'USA']
# strings are immutable
# so python cannot put bar simpson in the empty string ' ' in address
# so python creates a new jar to place bar simpson to concatenate
# the previous ' ' (jar) in address becomes dirty and the one containing bart simpson is clean
# the next element in list '742..' cannot be put in bar simpson jar
# bar simpson jar has to be cleaned before '742..' can be added to jar
# leaves a lot of dirty jars

address = ''
# for loops love collections
# not efficient
# creating lots of new jar variables that need to be reclaimed
for part in address_parts:
    # print(part)
    address = address + part + '\n'

print(address)

sentence = 'Victoria shouted "BOO!" to the group'
print(sentence)

sentence = """Victoria's favourite drink is gin. It makes her say "Yum Yum"!"""

bart = address_parts[0].upper()
print(bart)

line = "I will not punch my sister.\n"
# line is a string operand
# 20 is int operand
# things on either side of an operand is called an operand
repeated_lines = line * 20 # operator overloading
print(repeated_lines)

# more efficient code
# no comma after USA
# no forever loops and empty string jars
print ("=" * 30)

concatenated_address = ",\n".join(address_parts)
print(concatenated_address)