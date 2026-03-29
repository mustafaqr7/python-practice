# lambda basics
square = lambda x: x * x
print(square(5))

# lambda with if-else
even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print(even_odd(7))

# lambda with map
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x*x, nums))
print(squares)

# lambda with filter
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)
