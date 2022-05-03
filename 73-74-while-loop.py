# while loops are more powerfull than for loops
i = 0
while i < 50:
    print(i)
    i += 1
else:
    print('I am done')


# difference between for loops and while loops
# with for loops you can iterate once through the list 
# with while loops you can iterate  as you  like for

my_list = [1,2,3]
for item in my_list:
    print(item)


i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

# the correct way to do it is 
while True:
    response = input('say something: ')
    if (response == 'bye'):
        break


