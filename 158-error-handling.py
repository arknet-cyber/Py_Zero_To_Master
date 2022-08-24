# Error Handling

while True:
    try: # we put our block under try to handle errors
        age = int(input('What is your age? '))
        10/age
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('really bro?')
    else:
        print('thx')
        break