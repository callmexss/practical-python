# timethis.py
import time


def timethis(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('%s.%s: %f' % (func.__module__, func.__name__, end-start))
    return wrapper



@timethis
def cooldown(n):
    while n > 0:
        n -= 1


@timethis
def iter_test(n):
    for i in range(n):
        pass
    

if __name__ == "__main__":
    # cooldown(100000000)
    iter_test(100000000)
