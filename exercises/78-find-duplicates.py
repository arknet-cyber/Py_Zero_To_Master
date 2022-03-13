# Exercise; Find for duplicates in list:
my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

import collections
print(
    [
        item for item,
        count in collections.Counter(my_list).items()
        if count > 1
    ]
)

#the course answer
duplicates = []
for value in my_list:
    if my_list.count(value) > 1:
        duplicates.append(value)
        
print(duplicates)