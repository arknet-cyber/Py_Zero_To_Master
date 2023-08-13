import re

pattern = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
string = 'Andrei'
pattern2 = re.compile(r'[A-Za-z0-9$%#@]{8,}\d')
password = 'huiofewhoiuhwef7854^Y&*Y9'

a = pattern.search(string)
check = pattern2.fullmatch()
print(a)

# At least 8 char long
# contains any sort letters, numbers $%&#
# has to end with a number

