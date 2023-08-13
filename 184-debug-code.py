# debugging

#linting
#ide/ editor
#read errors
#pdb is a built in module

import pdb
def add(num1, num2):
    pdb.set_trace() # instead of using print (num1, num2)
    t = 4*5
    return num1 + num2

add(4, 'hdhdhff')