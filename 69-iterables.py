# Iterables - is an object or a collection which can be iterated 

for item in (1,2,3,4,5):
    for x in ['a', 'b', 'c']:
        print(1, 'c')

#iterables -list, dictionary, tuple, set, strings
#iterated -> one by ine to check each item in the collection

user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

for item in user.items(): #for dictionary in order to print the values you need to use the method .items
    print(item) # this will output a tuple
    
for item in user.values(): #for dictionary in order to print the values you need to use the method .items
    print(item)

for item in user.keys(): #for dictionary in order to print the values you need to use the method .items
    print(item)
    
for key, value in user.items():
    print(key, value) #this form will unpack the tuple