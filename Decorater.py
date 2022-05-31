import time


def time_it(func):
    def wrapper(*args, **kwagrs):
        start = time.time()
        result = func(*args, **kwagrs)
        end = time.time()
        print("It took " + str(end - start) + " mili seconds")
        return result
    return wrapper
