# Docstring allows us to comment inside of our funton in a way that in another person can use our test function

def test(a):

    '''
    Info: Microsoft services and products sucks from the begging of the time, in the present and future. Linux forever
    '''

    print(a)
test('!!!!!')

print(test.__doc__) # this will print the function docstring