print("Calculator v0.2")


def calculator(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    elif op == "//":
        return num1 // num2  # floor division
    elif op == "%":
        return num1 % num2  # remainder
    else:
        return "Invalid operator"


while True:
    user_input = input("Would you like to perform calculation? (y/n): ")
    if user_input == "y":
        num1 = float(input("Enter the first number: "))
        op = input("Enter the operator (+, -, *, /, //, %): ")
        num2 = float(input("Enter the second number: "))
        result = calculator(num1, num2, op)
        print("Result:", result)
    else:
        break
