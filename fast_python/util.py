import time
from loguru import logger

def clock(func):
    def clocked(*args):
        t0 = time.time()
        result = func(*args)
        elapsed = time.time() - t0
        name = func.__name__
        # arg_str = ', '.join(repr(arg) for arg in args)
        logger.info('[%0.8fs] %s' % (elapsed, name))
        return result
    return clocked
