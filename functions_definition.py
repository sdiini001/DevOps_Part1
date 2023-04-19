# import monday
# we use define to create our function
def say_hello():
    print('Hello')
    print('How are you today?')

# this is not part of function

# call (invoke function
# can call funstion as many times as you want

# say_hello()

# define a say hello to a name
def say_hello_to_name(firstname):
    print('Hello', firstname, '!')
    print('Your firstname is', firstname)

# say_hello_to_name('Rafa')
# say_hello_to_name('Mariam')

# print('This file is (function DEFINITIONS) is called', __name__)


def add(number1, number2):
    answer = number1 + number2
    return answer


# THE MAIN TRICK
# a test to see if this file is the __main__ entry point
# if it is run all the code


# drinks = ['water', 'apple-juice', 'milkshake']
# print(drinks)
# sorted_drinks = sorted(drinks)
#
# print(sorted_drinks)


if __name__ == "__main__":
    print('This file is (function DEFINITIONS) is called', __name__)
# call to invoke funxtions
    say_hello()
    say_hello()
    say_hello_to_name('Rafa')
    say_hello_to_name('Mariam')
    print(" I am the entrypoint")
    result = add(3,6)
    print(result)
    print('the result is', result)
    drinks = ['water', 'apple-juice', 'milkshake']
    print(drinks)
    sorted_drinks = sorted(drinks)

    print(sorted_drinks)
#
# else:
#     print('definitions is NOT the entrypoint')

# if it isn't only run some of the code