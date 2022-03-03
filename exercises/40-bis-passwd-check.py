username = input('Please input your username: ')
passwd = input('Please input your password: ')
counter = len(passwd)

user_passwd = ('*' * len(passwd))

print(f'Hi there {username}. Your password {user_passwd} is {counter} characters long')