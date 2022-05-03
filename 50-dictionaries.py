# Dictionary

dictionary = { # dictionary is an unordered key value pair
  'a': 1,
  'b': 2,
  'x': 3
}

# print(dictionary.sort())
print(dictionary['b'])

dictionary = { # There are also different type of dictionaries 
  'a': [1,2,3],
  'b': 'hello',
  'x': True
}

my_list = [
  {
    'a': [1,2,3],
    'b': 'hello',
    'x': True
  },
  {
    'a': [4,5,6],
    'b': 'hello',
    'x': True
  }
]

print(my_list[0]['a'][2])

print(dictionary['a'][1])