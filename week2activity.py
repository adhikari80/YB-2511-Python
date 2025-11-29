import math

class Calculator:

    # Recursive Fibonacci
    def fibonacci_recursive(self, n):
        if n <= 1:
            return n
        return self.fibonacci_recursive(n - 1) + self.fibonacci_recursive(n - 2)

    # Generate Fibonacci series of length n
    def fibonacci_series(self, n):
        return [self.fibonacci_recursive(i) for i in range(n)]

    # Factorial using math.factorial()
    def factorial(self, n):
        return math.factorial(n)


def main():
    calculator = Calculator()

    n = int(input("Enter a number (N): "))

    # Fibonacci
    fib_result = calculator.fibonacci_series(n)
    print(f"\nFibonacci series of length {n}:")
    print(fib_result)

    # Factorial
    fact_result = calculator.factorial(n)
    print(f"\nFactorial of", n, "is:", fact_result)


if __name__ == "__main__":
    main()
