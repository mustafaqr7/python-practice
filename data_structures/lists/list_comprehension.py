# Traditional way to create a list of squares from a list of numbers using a for loop and append method.
# numbers = [1, 2, 3, 4]
# squares = []

# for n in numbers:
#     squares.append(n * n)

# print(squares)


numbers = [1, 2, 3, 4]
squares = [n * n for n in numbers]

print(squares)