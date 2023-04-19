#  simple calculator
def add(number1, number2):
    return number1 + number2
# variadic function - collection as my parameter
# package all the args as one param
def add_lots(*numbers):
    answer = 0
    for n in numbers:
        answer += n # short hand
        # answer = answer + n # long hand
    return answer
def add_lots_with_message(*numbers, message):
    answer = 0
    for n in numbers:
        answer += n # short hand
    return message + " " + str(answer)
def subtract(number1, number2):
    return number1 - number2
def multiply(*, number1, number2):
    return number1 * number2
def divide(number1, number2=5):
    return number1 / number2
def print_stuff(name, age, colour, food):
    print(f"Your name is {name}")
    print(f"Your age is {age} years old")
    print("Your age is " + str(age) + " years old")
    print(f"Your favourite colour is {colour}")
    print(f"Your favourite food is {food}")
    print("Your favourite food is" + food)


# def print_stuff_Keywords(**info):
#     print(f"Your name is {info.name}")
#     print(f"Your age is {age} years old")
#     print("Your age is " + str(age) + " years old")
#     print(f"Your favourite colour is {colour}")
#     print(f"Your favourite food is {food}")
