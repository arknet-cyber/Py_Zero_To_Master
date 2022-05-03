is_old = bool('hello')
is_licensed = bool(5)

print(bool('hello')) # This is truthy because the bool is True
print(bool(5)) # This is truthy because the bool is True

print(bool('')) # This is Flasey
print(bool(0)) # This is Flasey
print(bool(None))

# Truthy and Falsey

#if is_old and is_licensed:
#    print('go and drive a Tesla')
#if is_old:
#    print ('you are old enough to drive this file')
#elif is_licensed:
#    print('you can drive now')
#else:
#    print('check')

password = '123'
username = 'john'

if password and username:
    print('nice')