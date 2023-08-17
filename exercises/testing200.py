import unittest
import random

def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('you are ok')
            return True

    else:
        print('try again')
        return False

if __name__ == '__main__':
    answer = random.randint(1,10)
    while True:
        try:
            guess = int(input('gues a number 1~10: '))
            if (run_guess(guess, answer)):
                break
        except ValueError:
            print('different one')
            continue
