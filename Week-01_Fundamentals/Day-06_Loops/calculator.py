while True:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    op=input("Enter operation (+, -, *, /, %): ")

    if op=='+':
        print("Addition =", a + b)
    elif op=='-':
        print("Subtraction =", a - b)
    elif op=='*':
        print("Multiplication =", a * b)
    elif op=='/':
        if b != 0:
            print("Division =", a / b)
        else:
            print("Error: Division by zero is not allowed.")
    elif op=='%':
        print("Remainder =", a % b)
    else:
        print("Invalid operation")
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() != 'y':
        print("Calculator closed.")
        break