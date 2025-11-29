class MathSeries:
    def __init__(self, n):
        if n < 0:
            raise ValueError("Number must be non-negative.")
        self.n = n

    def factorial(self):
        return self._factorial(self.n)

    def _factorial(self, n):
        if n in (0, 1):
            return 1
        return n * self._factorial(n - 1)

    def fibonacci_series(self):
        series = []
        for i in range(self.n + 1):
            series.append(self._fibonacci(i))
        return series

    def _fibonacci(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self._fibonacci(n - 1) + self._fibonacci(n - 2)


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    math_obj = MathSeries(n)

    print("Factorial (recursive):", math_obj.factorial())
    print("Fibonacci Series (recursive):", math_obj.fibonacci_series())
