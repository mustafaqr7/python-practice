# caching_decorator.py

# Caching decorator (memoization)

def cache(func):
    memory = {}

    def wrapper(*args):
        if args in memory:
            print(f"[CACHE] Returning cached result for {args}")
            return memory[args]

        print(f"[COMPUTE] Calculating result for {args}")
        result = func(*args)
        memory[args] = result
        return result

    return wrapper


@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print("\n--- Caching Decorator Example ---")
print("First call:", fibonacci(5))
print("Second call:", fibonacci(5))  # Uses cache