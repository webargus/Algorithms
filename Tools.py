
import random


def fill_random_array(a, n=50):

    for ix in range(int(3 + n * random.random())):
        x = int(100 * random.random())
        if x in a:
            ix -= 1
            continue
        a.append(x)














