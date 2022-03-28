import os, time

os.system("clear")
filenames = ['chopper.gif']


def anime(filenames, delay=1, repeat=10):
    """

    :type filenames: object
    """
    frames = []

    for name in filenames:
        with open(name, 'r', encoding='utf-8') as f:
            frames.append(f.readlines())

    for i in range(repeat):
        for frame in frames:
            print("".join(frame))
            time.sleep(delay)
            os.system("clear")


anime(filenames, delay=0.1, repeat=10)


def outer():
    '''
    The code represents the following scenario. With the nonlocal x we basically chanage the parent function value  with the local function value
    '''
    x = 'local'

    def inner():
        nonlocal x
        x = 'nonlocal'
        print('inner:', x)

    inner()
    print('outer:', x)


outer()
print(outer.__doc__)
