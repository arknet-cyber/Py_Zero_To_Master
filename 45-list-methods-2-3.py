# List Methods

basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']

print(basket.index('d', 0, 5))

print('d' in basket)

print(basket.count('d'))

basket.sort()
print(basket)

print(sorted(basket)) 

print()
print('New Basket sort')
new_basket = basket[:] # [:] this copy the list or we can use .copy() method
new_basket.sort()
print(new_basket)


print()
print('Revert')
basket1 = ['w', 'r', 'c', 'h', 'b', 'v', 'a']
basket1.sort()
basket1.reverse()
print(basket1)