from numpy import intersect1d
from pyrsistent import discard


my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}
print()
# Few methods for Sets
#print('How difference method works. Will show only the unique values in the first set comparing with the second sets')
#print(my_set.difference(your_set))
#print()
#
#print('How discard method works. In the bellow case we discard the last value')
#print(my_set.discard(5))
#print(my_set)
#print()
#
#print('How difference_update method works. It will only display the unique values from the first list comparing to the second list')
#print(my_set.difference_update(your_set))
#print(my_set)
#print()

print('How interesecton method works? Does display those values found in both lists')
print(my_set.intersection(your_set))
print(my_set & your_set)
print()

print('How the disjoint method works? Does give you a boolean response if the two list has anything in common')
print(my_set.isdisjoint(your_set))
print()

print('subset method does show if a certain set in one list does apear in the second list ')
print(my_set.issubset(your_set))
print()

print('Issuperset method. Does show if my set encompas yor set')
print(my_set.issuperset(your_set))
print()

print('The union method does combine the first list with the second list')
print(my_set.union(your_set))
print(my_set | your_set) # Is the same output as above