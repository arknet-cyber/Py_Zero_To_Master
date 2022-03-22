a = 10
def confusion(b):
    print(b)
    a = 90

confusion(300)

# A better way to do it
total = 0

def count():
    global total 
    total += 1 # here we use the total global function inside the local defined function
    return total

count()
count()
print(count())