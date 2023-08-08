# We have imported the functons from the utility.py module
import utility
import shopping.shopping_cart

print(utility.multiply(2,3))

# The shopping cart in this case is a package becasue we have created a new folder
# Shopping is a package (folder) containing modules "shopping_cart.py"
print(shopping.shopping_cart.buy('apple')) 