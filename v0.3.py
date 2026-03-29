print("Calculator v0.3")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Reminder")

usr_input = input("Enter your choice (1-5): ")
print(usr_input)

a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))


if usr_input == "1":
    print("Addition: ", a + b)
elif usr_input == "2":
    print("Subtraction: ", a - b)
elif usr_input == "3":
    print("Multiplication: ", a * b)
elif usr_input == "4":
    if b == 0:
        print("Error: Division by zero is not defined.")
    else:
        print("Division: ", a / b)
elif usr_input == "5":
    print("Reminder: ", a % b)
else:
    print("Invalid operator")
