# import functions_definition
#
# functions_definition.say_hello_to_name('Jenna')
# functions_definition.say_hello_to_name('Shona')
# functions_definition.say_hello_to_name('Conrad')
# Looks like our function
# don't know where it came from
# can overwrite your other code that includes say_hello_to_name
# namespace pollution
# USE WITH CAUTION
from functions_definition import say_hello_to_name
say_hello_to_name('Everyone')
say_hello_to_name('Matt')

# * imports everything, bad habit
# from functions_definition import *