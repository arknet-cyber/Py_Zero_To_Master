#range
print(range(0, 100))

for number in range(0, 100):
    print(number)
    
for number in range(0, 10):
    print('email list')

for _ in range(0,10): # this shows that we don't care about what the variable is, but  need only to range
    print(_)

for _ in range(0,10, 2): # this 2 is steping over
    print(_)

for _ in range(3):
    print(list(range(10)))