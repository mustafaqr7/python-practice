def decor(func):
    def inner():
        print("Before the function call.")
        func()
        print("After the function call.")
    return inner

def func():
    print("This is the original function.")

decorated_func = decor(func)
decorated_func()
