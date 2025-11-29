class MathOperations:
    # Method to calculate factorial
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)

    # Method to calculate fibonacci
    def fibonacci(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)


# Main section
if __name__ == "__main__":
    math_ops = MathOperations()   # Creating object of the class

    print("Choose an option:")
    print("1. Factorial")
    print("2. Fibonacci")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num = int(input("Enter a number to calculate factorial: "))
        print(f"Factorial of {num} is {math_ops.factorial(num)}")

    elif choice == 2:
        num = int(input("Enter the position of the Fibonacci number: "))
        print(f"Fibonacci number at position {num} is {math_ops.fibonacci(num)}")

    else:
        print("Invalid choice")