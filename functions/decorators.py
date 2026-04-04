# decorators.py
# we are trying to learn about decorators in Python. 
# Decorators are a powerful and flexible way to modify the behavior of functions 
# or classes without changing their source code. 
# They allow you to wrap another function in order to extend its behavior.

# Basic decorator example
def my_decorator(func):
    def wrapper():
        print("Something before the function runs")
        func()
        print("Something after the function runs  ")
    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()


print("\n--- With arguments ---")

# Decorator with arguments
def decorator_with_args(func):
    def wrapper(*args, **kwargs):
        print("Before function execution")
        result = func(*args, **kwargs)
        print("After function execution")
        return result
    return wrapper


@decorator_with_args
def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b


result = add(5, 3)
print("Result:", result)


print("\n--- Timing decorator ---")

# Real-world example: timing decorator
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.5f} seconds")
        return result
    return wrapper


@timer
def slow_function():
    time.sleep(1)
    print("Finished slow function")


slow_function()
