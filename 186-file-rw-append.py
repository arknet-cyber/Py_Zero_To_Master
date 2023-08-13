# Files I/O

with open('185-filetest.txt', mode='w') as my_file:
    text = my_file.write('hey its me')
    print(text)