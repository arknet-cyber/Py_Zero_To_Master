# List slicing (List are mutable)

amazon_cart = [
  'notebook', 
  'sunglasses',
  'toys',
  'grapes'
  ]
print(amazon_cart[0::])
print(amazon_cart[0::2])

# Swapping items in the lists

amazon_cart[0] = 'laptop'
print(amazon_cart)
print(amazon_cart[1:3])

# Using "copy" methods to copy a list
print()
ebay_cart = [
  'raspberry pi',
  'connectors',
  'cables',
  'terminals',
  'fuse'
]

ebay_cart[0] = 'pi_zero'
new_cart = ebay_cart[:]
new_cart[0] = 'tools'
print(new_cart)
print(ebay_cart)
print()

# Second method to copy a list

new2_cart = ebay_cart.copy()
new2_cart[4] = 'electrical'
print(new2_cart)