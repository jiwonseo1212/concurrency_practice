from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor as Executor

def async_map(executor, mapper, data):
    futures = []
    for datum in data:
        futures.append(executor.submit(mapper, datum))
    return futures

def map_less_naive(executor, my_input, mapper):
    map_results = async_map(executor, mapper, my_input)
    return map_results


from time import sleep

def emitter(word):
    sleep(10)
    return word, 1

with Executor(max_workers=4) as executor:
    words = "Python is great Python rocks".split(" ")
    maps = map_less_naive(executor, words, emitter)
    print(maps[-1])
    not_done = 1
    while not_done > 0:
        not_done = 0
        for fut in maps:
            not_done += 1 if not fut.done() else 0
            sleep(1)
        print(f"Still not finalized : {not_done}")

