"""return a number between 0 and 1 with two decimal places"""
import random

def random_float():
    return round(random.random(), 2)

""" if larger than 0.5, return true else return false"""
def random_bool():
    return random_float() > 0.5

"""if true then print hooray else print boo"""
def random_boolean_print():
    if random_bool():
        print("hooray")
    else:
        print("boo")

print(random_boolean_print())