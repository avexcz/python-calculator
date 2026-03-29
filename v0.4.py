print("Calculator v0.4")

a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))


def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        print("Error: Division by zero is not defined.")
    else:
        return a / b


def remainder(a: int, b: int) -> int:
    return a % b


def power(a: int, b: int) -> int:
    return a**b


print("Addition: ", add(a, b))
print("Subtraction:", subtract(a, b))
print("Multiplication: ", multiply(a, b))
print("Division:", divide(a, b))
