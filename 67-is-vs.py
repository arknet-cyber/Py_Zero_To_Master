# The equal sign == ( check for equality in value and does not check the location in the memory)
print('Checking == operation')
print('')
print(True == 1)
print(int('1') == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])
print('')

# IS check if the location in memory where this value is stored, is the same as the location
print('Checking is operation')
print('')
print(True is True)
print('1' is '1')
print([] is [])
print(10 is 10)
a = [1,2,3]
b = [1,2,3]
print(a is b)
