# Part 2: Using Built-in Packages

import math  
# Function to generate N-length Fibonacci series
def fibonacci_series(n):
    fib = [0, 1]

    if n == 1:
        return [0]

    while len(fib) < n:
        next_num = fib[-1] + fib[-2]
        fib.append(next_num)

    return fib

# Factorial using math.factorial()
def factorial(n):
    return math.factorial(n)  

def main():
    n = int(input("Enter a number (N): "))

    fib_result = fibonacci_series(n)
    print(f"\nFibonacci series of length {n}:")
    print(fib_result)

    fact_result = factorial(n)
    print(f"\nFactorial of", n, "is:", fact_result)


if __name__ == "__main__":
    main()
