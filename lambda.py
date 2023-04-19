# compare two values, if the first value is bigger return 1 else if the
# second value is bigger return -1 and if the numbers are equal return 0
compare = lambda a, b: -1 if a < b else (+1 if a > b else 0)
# return 1
print("a>b", compare(42, 5))
# return -1
print("a>b", compare(5, 42))
# return 0
print("a>b", compare(5, 5))
# take in a list of numbers, add 1 to each number in list
# return a new list
source_list = [1, 2, 5]
new_list = list(map(lambda a: a+1, source_list))
print(new_list)

# Filter the list of numbers above and return a new list with
# Only the even numbers (so only return items where x /2 has remainder of 0)
filtered_list = list(filter(lambda x : x % 2 == 0, source_list))
print(filtered_list)


wordy_list = ["Dog", "Cat", "Rabbit", "Fox", "Deer"]
# filter a list of words and only return those which are
# 3 characters in length
# returns ['Dog', 'Cat', 'Fox']

filtered_words = list(filter(lambda x: len(x) == 3, wordy_list))
print(filtered_words)