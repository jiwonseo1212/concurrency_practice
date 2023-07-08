from collections import defaultdict
from util import clock

@clock
def map_reduce_ultra_naive(my_input, mapper, reducer):
    map_results = map(mapper, my_input)

    shuffler = defaultdict(list) #set default value as a list

    for key, value in map_results:
        shuffler[key].append(value)

    return map(reducer, shuffler.items())


if __name__ == "__main__":
    words = "Python is great Python rocks".split(" ")
    emitter = lambda word : (word, 1)
    counter = lambda emitted: (emitted[0], sum(emitted[1]))

    list(map_reduce_ultra_naive(words, emitter, counter))