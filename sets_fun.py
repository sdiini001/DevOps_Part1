names = {'Bob', 'Dave', ' Fred', 'Dave'}
print(names)

names_list = ['aisha', 'angel', 'dominique']
names_as_set = set(names_list)
print(names_as_set)

names_as_set.add('mariam')
names_as_set.remove('angel')

# print(names_as_set)
# names_as_set.pop()
# print(names_as_set)

second_Set = { 'rach', 'rafaella'}
# best understood as venn diagram
names_as_set.union(second_Set)
print(names_as_set)
#  learn how to exploit capabilities & uniqueness of sets
# aka difference
result = names_as_set.difference({'aisha', 'angel'})
print(result)

result = names_as_set.union(second_Set)
result = names_as_set | second_Set
print(result)