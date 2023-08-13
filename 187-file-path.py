# Talking about relative path which can be "app/sad.py"
# The absolute path would be /User/home/app/sad.py or ../app/sad.py

with open('187-sad.py', mode='a') as my_file:
    text = my_file.write('hey its me')
    print(text)
