print(("Python Calculator v0.6").center(50, "-"))

# ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"


def add(a, b):
    result = a + b
    print(GREEN + f"Addition Result: {result}" + RESET)


def subtract(a, b):
    result = a - b
    print(RED + f"Subtraction Result: {result}" + RESET)


def multiply(a, b):
    result = a * b
    print(YELLOW + f"Multiplication Result: {result}" + RESET)


def divide(a, b):
    if b == 0:
        print(RED + "Error: Division by zero!" + RESET)
    else:
        result = a / b
        print(BLUE + f"Division Result: {result}" + RESET)


# Main program
print(
    GREEN
    + "1. Add\n"
    + RED
    + "2. Subtract\n"
    + YELLOW
    + "3. Multiply\n"
    + BLUE
    + "4. Divide"
    + RESET
)

choice = input("Enter choice (1/2/3/4): ")

num1: float = float(input("Enter first number: "))
num2: float = float(input("Enter second number: "))

if choice == "1":
    add(num1, num2)
elif choice == "2":
    subtract(num1, num2)
elif choice == "3":
    multiply(num1, num2)
elif choice == "4":
    divide(num1, num2)
else:
    print(RED + "Invalid choice!" + RESET)
