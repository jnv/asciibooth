# encoding: UTF-8
import random
from . import config

def sampler(source):
    def reshuffle():
        copy = list(source)
        random.shuffle(copy)
        return copy

    stack = reshuffle()
    lastitem = ''

    while True:
        try:
            item = stack.pop()
            if item == lastitem:
                item = stack.pop()
            yield item
            lastitem = item
        except IndexError:
            stack = reshuffle()
            continue

def incremental_chance(start=0.5, increment=0.01):
    current_chance = start

    while True:
        r = random.random()
        success = (r < current_chance)
        if success:
            current_chance = start
        else:
            current_chance += increment
        yield success


def status_generator():
    random_status = sampler(config.TWEET_MESSAGES)
    show_status = incremental_chance(start=config.TWEET_CHANCE_INITIAL, increment=config.TWEET_CHANCE_INCREMENT)

    fixed = config.TWEET_FIXED

    while True:
        status = ''
        if next(show_status):
            status = next(random_status) + " "
        yield "{status}{fixed}".format(status=status, fixed=fixed)

if __name__ == '__main__':
    gen = status_generator()
    for i in range(0, 20):
        print(next(gen))
