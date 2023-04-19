t1 = 'cat', 'dog', 'python', 'mouse', 'camel'
t2 = 'help', 'crab', 'lobster', 'fish'
for a, *b, c in t1, t2:
    print(a, b, c)


# Code with notes again
# Task 1
# # new task
# # created two tuples
# t1 = 'cat', 'dog', 'python', 'mouse', 'camel'
# t2 = 'kelp', 'crab', 'lobster', 'fish'
# # for loop where
# for a, *b, c in t1, t2:
#    print(a, b, c)
# This created the range a, b,c and put all the variables in the middle within b because of the *.
# output:
# cat ['dog', 'python', 'mouse'] camel
# kelp ['crab', 'lobster'] fish