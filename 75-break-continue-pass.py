my_list = [1,2,3]
for item in my_list:
    print(item)
    break

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    break



my_list = [1,2,3]
for item in my_list:
    continue
    print(item)

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    continue

my_list = [1,2,3]
for item in my_list:
    # thinking about it 
    pass #pass to the next line. this is useful when you test something 
    print(item)

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    pass