#A decorator is a function that modifies or enhances another 
# function or class without changing its source code.

def outer(func):
    def inner():
        print("I'm sleeping")
        func()
        print("I'm getting up")

    return inner

@outer
def sleep():
    import random
    import time
    print("sleeping......")
    time.sleep(random.randint(1,5))

sleep()
