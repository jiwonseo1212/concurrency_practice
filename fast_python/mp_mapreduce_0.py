from collections import defaultdict
import multiprocessing as mp

def map_reduce(my_input, mapper, reducer):
    with mp.Pool(2) as pool: #pool with two processes
        map_result = pool.map(mapper, my_input)
        distributor = defaultdict(list)
        for key, value in map_result:
            distributor[key].append(value)
        results = pool.map(reducer, distributor.items()) # the pool provides a synchronous map function
    return results

if __name__ == "__main__":
    words = "Python is great Python rocks".split(" ")
    emitter = lambda word : (word, 1)
    counter = lambda emitted: (emitted[0], sum(emitted[1]))

    map_reduce(words, emitter, counter)