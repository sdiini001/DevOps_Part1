# create string variable
line = 'root::0:0:superuser:/root:/bin/sh'
# create a list by splitting string elements on :
# split the line at :
elems = line.split(':')
# replace first item in the list with string avatar
elems[0] = 'avatar'
# replacing fourth-item superuser with the super-user (zero)
elems[4] = 'The super-user (zero)'
line = ':'.join(elems) # using method.join to create a string
print(line)