# MRO - Method Resolution Order
# The algorithm of the MRO is called Depth First Search

class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B, C):
    pass

print(D.num)

#       A
#    /    \
#  /       \
# B         C
#  \       /
#   \    /
#     D

# Another example

class X: pass
class Y: pass
class Z: pass
class A(X,Y): pass
class B(Y,Z): pass
class M(B,A,Z): pass

print(M.__mro__) # we can use the MRO method  to check the structure of the multiple inheritance