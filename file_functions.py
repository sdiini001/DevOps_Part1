# create a function that opens a file for reading
# loops through the file
# prints the file contents
# processes a file
# file_handle = open('somefile.txt', 'r')
# for line in file_handle:
#     print(line, end='')


def print_file(filename):
    file_handle = open(filename, 'r')

    for line in file_handle:
        print(line, end='')

if __name__ == '__main__':
    print_file('somefile.txt')
    print('\n',  '#' * 30)
    print_file('another.txt')