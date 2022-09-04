# Error Handling

def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print('please enter numbers' + err)

print(sum('1',2))


#another example which can help us better understand the error


def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(err)

print(sum('1',2))