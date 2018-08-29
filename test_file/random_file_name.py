import random
import string
import time


def get_random_string(index):
    return ''.join(random.choice(string.ascii_letters + string.digits) for x in range(index))


mills = str(round(time.time() * 1000))
filename = '{}{}'.format(get_random_string(6), '{}{}'.format(mills, '.png'))
print(filename)
