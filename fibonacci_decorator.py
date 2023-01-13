from functools import cache, lru_cache

# Simple memoize decorator
def memoize(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            print("This number isn't cached yet")
            cache[n] = func(n)
        return cache[n]
    return wrapper

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Decorated with the simple memoize decorator
memoized_fibonacci = memoize(fibonacci)
# Decorated with the cache
cached_fibonacci = cache(fibonacci)
# Decorated with the lru_cache decorator
lru_cached_fibinacci = lru_cache(maxsize=128)(fibonacci)


print(memoized_fibonacci(12))
print(memoized_fibonacci(12))
print()
print(cached_fibonacci.cache_info())
print(cached_fibonacci(12))
print(cached_fibonacci(12))
print(cached_fibonacci.cache_info())
print()
print(lru_cached_fibinacci.cache_info())
print(lru_cached_fibinacci(12))
print(lru_cached_fibinacci(12))
print(lru_cached_fibinacci.cache_info())