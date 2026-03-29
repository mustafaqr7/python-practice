def factorial(n):
    """Returns factorial of a number using recursion."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n <= 1:
        return 1
    return n * factorial(n-1)


def factorial_iterative(n):
    """Returns factorial using iteration."""
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"Factorial of {num} is {factorial(num)}")
