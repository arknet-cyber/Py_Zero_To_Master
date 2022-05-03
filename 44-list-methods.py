# List Methods

basket = [1,2,3,4,5]

#adding - modifies the list in place
basket.append(100)
new_list = basket
print(basket)
print(new_list)

#insert -  also modifies the list in place
basket.insert(2, 109)
new_list = basket
print(basket)

# extend -takes a iterable which we can iterate
basket.extend([4, 205])
new_list = basket
print(basket)

# removing
basket.pop() # pop removes an object from the end of the list
basket.pop(1) # or also remove a value from the index
print(basket)

basket.remove(4) # with remove method we remove a specified value from the list
print(basket)

basket.clear() # removes everything from the list
print(basket)