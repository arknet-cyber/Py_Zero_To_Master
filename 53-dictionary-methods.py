# Dictionary

user = {
  'basket': [1,2,3],
  'greet': 'hello'
}

print(user.get('age', 55)) # "get" is a method which is trying to find out if the key 'age' exists in the dictionary. But, continuing between the brackets when we ask if 'age' exists, if doesnt exists, then we ask the number 55 to be used


user2 = dict(name='John') # using dict which is an builtin function
print(user2)