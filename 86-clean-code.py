# clean code

def is_even(num):
    if num % 2 == 0:
        return True
    elif num % 2 != 0: # also we can write simple "else: return False" and is cleaner code
        return False

print(is_even(50))

# A cleaner way to do it
def is_even(num):
    return num % 2 == 0 

print(is_even(50))