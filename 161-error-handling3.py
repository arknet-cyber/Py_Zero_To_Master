# Error Handling

while True:
    try: # we put our block under try to handle errors
        age = int(input('What is your age? '))
        10/age
        raise ValueError('hey sup?') # this is useful when we are using oir own attributes
    except ZeroDivisionError:
        print('really bro?')
        break
    else:
        print('thx')
        break
    finally:
        print('ok, I am finally done')
    print('can you hear me')