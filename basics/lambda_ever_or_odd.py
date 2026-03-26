# lambda function example

# Define a lambda function that checks if a number is even or odd

is_even_or_odd = lambda x: "Even" if x % 2 == 0 else "Odd"


# Example usage:
if __name__ == "__main__":
    print(is_even_or_odd(4))  # Output: Even
    print(is_even_or_odd(7))  # Output: Odd
    print(is_even_or_odd(0))  # Output: Even