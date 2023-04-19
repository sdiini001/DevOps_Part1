import calculator
x = 10
y = 2
add_result = calculator.add(x, y)
subtract_result = calculator.subtract(x, y)
multiply_result = calculator.multiply(number1=x, number2=y)
divide_result = calculator.divide(x, y)
print('The answers are:')
print(add_result, subtract_result, multiply_result, divide_result)
divide_using_default = calculator.divide(20)
print(divide_using_default)
multiply_result2 = calculator.multiply(number2=10, number1=3)
print(multiply_result2)
numbers = [25, 3]
add_result2 = calculator.add(numbers[0], numbers[1])
print(add_result2)
# calling add with a collection that should be unpacked
add_result3 = calculator.add(*numbers)
print(add_result3)
lots_answer = calculator.add_lots(1, 2, 8, 9)
print(lots_answer)
calculator.print_stuff(name='Bart', age=8, colour='Yellow', food='Bubble gum')
calculator.print_stuff('Marge', age=35, colour='Blue', food='Pizza')
print('one', 'two',  "three", end=".....",)
print("\n")
print('one', 'two', ".....", "three")
result = calculator.add_lots_with_message(5, 2, 4, message="Answer is:")
print(result)