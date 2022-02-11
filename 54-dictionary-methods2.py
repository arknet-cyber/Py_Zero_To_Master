# Dictionary

user = {
  'basket': [1,2,3],
  'greet': 'hello',
  'age': 20
}

print('basket' in user)
print('size' in user)

print('age' in user.keys()) # we iterate over the keys
print('hello' in user.values()) # iterate over the values in the Dictionary
print(user.items()) # iterate over the items
print(user.clear())

user.clear()
print(user)


man = {
  'basket': [1,2,3],
  'greet': 'hello',
  'age': 20
}

man2 = man.copy()
print(man.clear())
print(man2)

print(man2.pop('age')) # 'pop' removes the key from the dictionary
print(man2)
print(man2.popitem())

print(man2.update({'age': 55}))
print(man2)