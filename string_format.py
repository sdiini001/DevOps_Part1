# Dictionaries
# key : value
# Mercury : 57.91
planets = {'Mercury': 57.91, 'Venus': 108.2, 'Earth': 149.597870, 'Mars': 227.94}
print(planets)

# print(planets['Earth'])
# print(planets['Mars'])

# for loop used to step over all values in the list
# enumerate is used to count all values
# turns single item in to tuple
# so we create a second variable planet_number
# store 1 in the enumerate function in the planet.keys to start mercury as 1 instead of 0
# this makes it readable for non-developers
# for planet_number, item in enumerate(planets.keys(), 1):
#  # print(planet)
# #  print (planets[planet])
# # both combined is:
#     print(planet_number, item, planets[item], 'Gm')

# string format
for planet_number, item in enumerate(planets.keys(), 1):
    print("{:2d} {:<10s} {:06.2f} Gm".format(planet_number, item, planets[item]))


#  literal string interpolation
#   on "f" string
for planet_number, item in enumerate(planets.keys(), 1):
     print(f"{planet_number:2d} {item:<10s} {planets[item]:06.2f} Gm")

# slicing strings
message = "Goodbye Python"
print(message)

print(message[8:14])
print(message[8:])
print(message[-4:])

