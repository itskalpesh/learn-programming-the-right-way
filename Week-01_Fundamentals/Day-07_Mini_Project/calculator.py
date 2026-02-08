print("=== Simple Calculator ===")

while True:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Choose operation:")
    print("+  Addition")
    print("-  Subtraction")
    print("*  Multiplication")
    print("/  Division")
    print("%  Modulus")

    op = input("Enter operation: ")

    if op == '+':
        print("Result =", a + b)

    elif op == '-':
        print("Result =", a - b)

    elif op == '*':
        print("Result =", a * b)

    elif op == '/':
        if b != 0:
            print("Result =", a / b)
        else:
            print("Error: Division by zero")

    elif op == '%':
        print("Result =", a % b)

    else:
        print("Invalid operation")

    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() != 'y':
        print("Calculator closed.")
        break