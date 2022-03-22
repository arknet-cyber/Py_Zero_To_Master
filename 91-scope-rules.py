a = 1

def confusion():
    a = 5
    return a

print(a)
print(confusion())

# 1  - start with local variable
# 2 - parent local Scope
# 3  - global Scope
# 4 - built in python function

a = 1

def parent():
    def confusion():
        return sum # in this case, sum is built in function
    return confusion()

print(parent())
print(a)