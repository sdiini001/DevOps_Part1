import functions_definition
# when you import a file,
# the file gets run by the interpreter

print('This file is (function CALLING) is called', __name__)

functions_definition.say_hello()

functions_definition.say_hello_to_name('Aisha')