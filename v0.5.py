print("=" * 50)
print("Calculator v0.5")
print("=" * 50)

import math


# addition
def add(a: float, b: float) -> float:
    return a + b


# subtraction
def subtract(a: float, b: float) -> float:
    return a - b


# multiplication
def multiply(a: float, b: float) -> float:
    return a * b


# division
def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Error: Division by zero is not defined.")
    return a / b


# floor division
def floor_divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Error: Division by zero is not defined.")
    return a // b


# remainder
def remainder(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Error: Division by zero is not defined.")
    return a % b


# power
def power(a: float, b: float) -> float:
    return a**b


# square root
def square_root(a: float) -> float:
    if a < 0:
        raise ValueError("Error: Cannot calculate square root of a negative number.")
    return math.sqrt(a)


# factorial
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Error: Factorial is not defined for negative numbers.")
    return math.factorial(n)


# logarithm
def logarithm(a: float, base: float = math.e) -> float:
    if a <= 0:
        raise ValueError("Error: Logarithm is only defined for positive numbers.")
    if base <= 0 or base == 1:
        raise ValueError("Error: Base must be positive and not equal to 1.")
    return math.log(a, base)


# Trigonometric functions
def sine(angle: float, degrees: bool = True) -> float:
    if degrees:
        angle = math.radians(angle)
    return math.sin(angle)


def cosine(angle: float, degrees: bool = True) -> float:
    if degrees:
        angle = math.radians(angle)
    return math.cos(angle)


def tangent(angle: float, degrees: bool = True) -> float:
    if degrees:
        angle = math.radians(angle)
    return math.tan(angle)


def display_menu():
    print("\n")
    print("OPERATIONS MENU")
    print("=" * 50)
    print("Basic Operations:")
    print("  1. Addition (+)")
    print("  2. Subtraction (-)")
    print("  3. Multiplication (*)")
    print("  4. Division (/)")
    print("  5. Floor Division (//)")
    print("  6. Remainder (%)")
    print("  7. Power (^)")
    print("\nAdvanced Operations:")
    print("  8. Square Root (√)")
    print("  9. Factorial (!)")
    print("  10. Logarithm (log)")
    print("\nTrigonometric Functions:")
    print("  11. Sine (sin)")
    print("  12. Cosine (cos)")
    print("  13. Tangent (tan)")
    print("\n  0. Exit")
    print("=" * 50)


def get_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def get_integer(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (0-13): ").strip()

        if choice == "0":
            print("\n Program Exited Successfully.")
            break

        try:
            if choice in ["1", "2", "3", "4", "5", "6", "7"]:
                # Binary operations (require two numbers)
                num1 = get_number("Enter the first number: ")
                num2 = get_number("Enter the second number: ")

                if choice == "1":
                    result = add(num1, num2)
                    print(f"\nResult: {num1} + {num2} = {result}")
                elif choice == "2":
                    result = subtract(num1, num2)
                    print(f"\nResult: {num1} - {num2} = {result}")
                elif choice == "3":
                    result = multiply(num1, num2)
                    print(f"\nResult: {num1} × {num2} = {result}")
                elif choice == "4":
                    result = divide(num1, num2)
                    print(f"\nResult: {num1} ÷ {num2} = {result}")
                elif choice == "5":
                    result = floor_divide(num1, num2)
                    print(f"\nResult: {num1} // {num2} = {result}")
                elif choice == "6":
                    result = remainder(num1, num2)
                    print(f"\nResult: {num1} % {num2} = {result}")
                elif choice == "7":
                    result = power(num1, num2)
                    print(f"\nResult: {num1} ^ {num2} = {result}")

            elif choice == "8":
                # Square root
                num = get_number("Enter the number: ")
                result = square_root(num)
                print(f"\nResult: √{num} = {result}")

            elif choice == "9":
                # Factorial
                num = get_integer("Enter a non-negative integer: ")
                result = factorial(num)
                print(f"\nResult: {num}! = {result}")

            elif choice == "10":
                # Logarithm
                num = get_number("Enter the number: ")
                base_input = input(
                    "Enter the base (press Enter for natural log): "
                ).strip()
                if base_input:
                    base = float(base_input)
                    result = logarithm(num, base)
                    print(f"\nResult: log_{base}({num}) = {result}")
                else:
                    result = logarithm(num)
                    print(f"\nResult: ln({num}) = {result}")

            elif choice in ["11", "12", "13"]:
                # Trigonometric functions
                angle = get_number("Enter the angle: ")
                unit = input("Is the angle in degrees? (y/n): ").strip().lower()
                degrees = unit != "n"

                if choice == "11":
                    result = sine(angle, degrees)
                    unit_str = "°" if degrees else " rad"
                    print(f"\nResult: sin({angle}{unit_str}) = {result}")
                elif choice == "12":
                    result = cosine(angle, degrees)
                    unit_str = "°" if degrees else " rad"
                    print(f"\nResult: cos({angle}{unit_str}) = {result}")
                elif choice == "13":
                    result = tangent(angle, degrees)
                    unit_str = "°" if degrees else " rad"
                    print(f"\nResult: tan({angle}{unit_str}) = {result}")

            else:
                print("\nInvalid choice! Please select a number between 0-13.")

        except ValueError as e:
            print(f"\n{e}")
        except Exception as e:
            print(f"\n An error occurred: {e}")


if __name__ == "__main__":
    main()
