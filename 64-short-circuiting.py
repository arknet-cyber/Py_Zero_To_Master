# Short Circuiting

is_Friend = True
is_User = True

print(is_Friend and is_User)

if is_Friend and is_User:
    print('best friends')

# Short circuiting we can use it when we use "or" instead of "and"

if is_Friend or is_User:
    print('best friends')