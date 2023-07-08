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

def report_progress(futures, tag, callback):
    done = 0
    num_jobs = len(futures)
    while num_jobs > done:
        for fut in futures:
            if fut.done():
                done += 1
        sleep(0.5)
        if callback:
            callback(tag, done, num_jobs - done)

def map_reduce_less_naive(my_input, mapper, reducer, callback=None):
    with Executor(max_workers=2) as executor:
        futures = async_map(executor, mapper, my_input)
        report_progress(futures, "map", callback)
        distributor = defaultdict(list)
        map_results = map(lambda f : f.result(), futures)
        for key, value in map_results:
            distributor[key].append(value)
            futures = async_map(executor, reducer, distributor.items())
            report_progress(futures, "reduce", callback)
            results = map(lambda f : f.result(), futures)

        return results
    
def reporter(tag, done, not_done):
    print(f"Operation {tag} : {done}/ {done+ not_done}")

words = "Python is great Python rocks".split(" ")
emitter = lambda word : (word, 1)
counter = lambda emitted: (emitted[0], sum(emitted[1]))

list(map_reduce_less_naive(words, emitter, counter, reporter))
# with Executor(max_workers=4) as executor:
#     words = "Python is great Python rocks".split(" ")
#     maps = map_less_naive(executor, words, emitter)
#     print(maps[-1])
#     not_done = 1
#     while not_done > 0:
#         not_done = 0
#         for fut in maps:
#             not_done += 1 if not fut.done() else 0
#             sleep(1)
#         print(f"Still not finalized : {not_done}")

