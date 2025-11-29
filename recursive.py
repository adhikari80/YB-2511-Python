# Part 1
# Recursive function to compute Fibonacci number at position n
def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Recursive function to compute factorial of n
def factorial_recursive(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


# Function to generate N-length Fibonacci series using recursion
def fibonacci_series(n):
    if n <= 0:
        return []
    series = [fibonacci_recursive(i) for i in range(n)]
    return series


# Main program
def main():
    n = int(input("Enter a number (N): "))

    # Generate Fibonacci series
    fib_result = fibonacci_series(n)
    print(f"\nFibonacci series of length {n}:")
    print(fib_result)

    # Compute factorial
    fact_result = factorial_recursive(n)
    print(f"\nFactorial of {n} is: {fact_result}")


# Run the program
if __name__ == "__main__":
    main()
