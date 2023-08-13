try:
    with open('187-sads.py', mode='r') as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print('file does not exist')
    raise err
except IOError as err:
    print ('io error')
    raise err

