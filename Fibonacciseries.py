# Part 1
# Function to generate N-length Fibonacci series
def fibonacci_series(n):
    # The first two Fibonacci numbers
    fib = [0, 1]

    # If the user requests only 1 number
    if n == 1:
        return [0]

    # Generate Fibonacci series up to N terms
    while len(fib) < n:
        next_num = fib[-1] + fib[-2]  # sum of last two numbers
        fib.append(next_num)

    return fib


# Function to compute factorial of N
def factorial(n):
    result = 1
    # Multiply numbers from 1 to N
    for i in range(1, n + 1):
        result *= i
    return result


# Main program to run the functions
def main():
    #  input
    n = int(input("Enter a number (N): "))

    # Generate Fibonacci
    fib_result = fibonacci_series(n)
    print(f"\nFibonacci series of length {n}:")
    print(fib_result)

    # Compute factorial
    fact_result = factorial(n)
    print(f"\nFactorial of", n, "is:", fact_result)


# Run the program
if __name__ == "__main__":
    main()
