# Formatted strings


# This method is for python 3
name = 'Johny'
age = 55
print(f'hi {name}. You are {age} years old') 

# This method is for python2
car = 'Tesla'
km = 30000
print('This is my {} car and has {} km'.format('Tesla', '30000'))

# A different way to do it old fashion
name = 'Johny'
age = 55
print('hi {new_name}. You are {age} years old'.format(new_name='sally', age=100))