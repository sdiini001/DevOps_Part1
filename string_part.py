text = 'hello world'
# counts number of o's
# method
print(text.count('o'))
# if statement starts with 'hell' print "It's hell in there"
# method
if text.startswith('hell'):
    print("It's hell in there")
# checks if there are just alphabet characters
# space does not count as alpha character
# so no numbers
# method
if text.isalpha():
    print('string is all alpha')
# tab, enter, new line
# no printable outputs
text = ' \t\r\n'
# checks if the previous text is just space or contains characters
# print whitespace as  there are no characters to print
# method
if text.isspace():
    print('string is whitespace')