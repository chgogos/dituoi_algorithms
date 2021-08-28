def fib(n, cache=None):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if cache is None:
        cache = {}

    result = fib(n - 1, cache) + fib(n - 2, cache)
    cache[n] = result
    return result
