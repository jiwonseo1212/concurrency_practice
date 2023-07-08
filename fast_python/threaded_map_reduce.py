from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor as Executor
from util import clock
@clock
def map_reduce_still_naive(my_input, mapper, reducer):
    with Executor() as executor:
        map_results = executor.map(mapper, my_input)
    
        distributor = defaultdict(list)

        for key, value in map_results:
            distributor[key].append(value)
        
        results = executor.map(reducer, distributor.items())
    return results
        

if __name__ == "__main__":
    words = "Python is great Python rocks".split(" ")
    emitter = lambda word : (word, 1)
    counter = lambda emitted: (emitted[0], sum(emitted[1]))

    print(list(map_reduce_still_naive(words, emitter, counter)))