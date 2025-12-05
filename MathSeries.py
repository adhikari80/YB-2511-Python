<<<<<<< HEAD
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
=======
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
>>>>>>> 23a8239742a0c333cd4dbf543fe0bb2f12d32430
