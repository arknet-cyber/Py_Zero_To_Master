# Dictionary

dictionary = { # dictionary is an unordered key value pair
  123: [1,2,3],
  True: 'hello',
  'x': 3
}

print(dictionary[123])

# Note!!! Dictionary keys needs to have a special property
# A key needs to be immutable, va lue which can't be changed

# A key ina dictionary needs to be unique
print()
print('The bellow result from ths script does show that the key needs to be unique becasue a key does hold a place in memory')
dictionary = { # dictionary is an unordered key value pair
  '123': [1,2,3],
  '123': 'hello'
}
print()
print(dictionary['123'])