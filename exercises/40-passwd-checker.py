# Passwd checker

username = input('Username: ')
passwd = input('Password: ')
chars = '*' * len(passwd)
pass_len = len(passwd)

print(f'Hi {username}. Your password {chars} is {pass_len} characters long ')

# or

print(f'Hi {username}. Your password {chars} is {len(passwd)} characters long ')