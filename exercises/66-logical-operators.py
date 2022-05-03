is_magician = False
is_expert = True

# check if magician and expert: "you are a master magician"
if not(is_magician) and is_expert:
    print('You are a master magician')


# check if magician but not expert: "at least you're getting there"
if not(is_magician) and is_expert:
    print('at least you getting there')

# if you're not a magician: "You need magic powers"
if not(is_magician):
    print('you need magic powers')

# Answers to the exercise
if is_expert and is_magician:
    print('You are a master magician')

elif is_magician and not is_expert:
    print('at least you getting there')

elif not is_magician:
    print('you need magic powers')







