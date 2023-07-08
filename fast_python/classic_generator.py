def subcoroutine():
    print("Subcoroutine")
    x = yield 1
    print("Recv: " + str(x))
    x = yield 2
    print("Recv: " + str(x))

def coroutine():
    _i = subcoroutine()
    _x = next(_i)
    while True:
        _s = yield _x

        if _s is None:
            _x = next(_i)
        else:
            _x = _i.send(_s)


if __name__ == "__main__":
    x = coroutine()
    next(x)
    next(x)
    next(x)
    # x.send(10)
    # x.send(20)