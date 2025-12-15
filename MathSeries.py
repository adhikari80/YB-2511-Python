class MathSeries:
    """Combined MathSeries supporting both static recursive methods
    and instance-based convenience methods (when an `n` is provided).
    """
    def __init__(self, n=None):
        if n is not None and n < 0:
            raise ValueError("Number must be non-negative.")
        self.n = n

    # Static recursive implementations
    @staticmethod
    def factorial_recursive(n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if n in (0, 1):
            return 1
        return n * MathSeries.factorial_recursive(n - 1)

    @staticmethod
    def fibonacci_recursive(n):
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers.")
        if n == 0:
            return 0
        if n == 1:
            return 1
        return MathSeries.fibonacci_recursive(n - 1) + MathSeries.fibonacci_recursive(n - 2)

    @staticmethod
    def fibonacci_series(n):
        return [MathSeries.fibonacci_recursive(i) for i in range(n + 1)]

    # Instance methods using the stored `n`
    def factorial(self):
        if self.n is None:
            raise ValueError("Instance has no 'n'; provide n when constructing or use the static method.")
        return self._factorial(self.n)

    def _factorial(self, n):
        if n in (0, 1):
            return 1
        return n * self._factorial(n - 1)

    def fibonacci_series_instance(self):
        if self.n is None:
            raise ValueError("Instance has no 'n'; provide n when constructing or use the static method.")
        return [self._fibonacci(i) for i in range(self.n + 1)]

    def _fibonacci(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self._fibonacci(n - 1) + self._fibonacci(n - 2)


if __name__ == "__main__":
    n = int(input("Enter a number: "))

    # Static usage
    print("Factorial (recursive static):", MathSeries.factorial_recursive(n))
    print("Fibonacci (nth number static):", MathSeries.fibonacci_recursive(n))
    print(f"Fibonacci series (0 to {n}) static:", MathSeries.fibonacci_series(n))

    # Instance usage
    math_obj = MathSeries(n)
    print("Factorial (instance):", math_obj.factorial())
    print("Fibonacci Series (instance):", math_obj.fibonacci_series_instance())
