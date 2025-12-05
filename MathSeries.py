class MathSeries:
    # Recursive factorial
    @staticmethod
    def factorial_recursive(n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if n in (0, 1):
            return 1
        return n * MathSeries.factorial_recursive(n - 1)

    # Recursive Fibonacci (nth number)
    @staticmethod
    def fibonacci_recursive(n):
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers.")
        if n == 0:
            return 0
        if n == 1:
            return 1
        return MathSeries.fibonacci_recursive(n - 1) + MathSeries.fibonacci_recursive(n - 2)

    # Generate full Fibonacci series from 0 to n
    @staticmethod
    def fibonacci_series(n):
        return [MathSeries.fibonacci_recursive(i) for i in range(n + 1)]


# Main program
if __name__ == "__main__":
    n = int(input("Enter a number: "))

    print("Factorial (recursive):", MathSeries.factorial_recursive(n))
    print("Fibonacci (nth number):", MathSeries.fibonacci_recursive(n))
    print(f"Fibonacci series (0 to {n}):", MathSeries.fibonacci_series(n))

    print("Factorial (recursive):", math_obj.factorial())
    print("Fibonacci Series (recursive):", math_obj.fibonacci_series())
