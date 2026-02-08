balance = 1000
correct_pin = "1234"

print("🏦 Welcome to ATM")

pin = input("Enter your PIN: ")

if pin != correct_pin:
    print("❌ Incorrect PIN. Access denied.")
else:
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            print("💰 Current Balance:", balance)

        elif choice == "2":
            amount = int(input("Enter deposit amount: "))
            if amount > 0:
                balance += amount
                print("✅ Amount deposited.")
            else:
                print("❌ Invalid amount.")

        elif choice == "3":
            amount = int(input("Enter withdrawal amount: "))
            if amount <= 0:
                print("❌ Invalid amount.")
            elif amount > balance:
                print("❌ Insufficient balance.")
            else:
                balance -= amount
                print("✅ Please collect your cash.")

        elif choice == "4":
            print("👋 Thank you for using the ATM.")
            break

        else:
            print("❌ Invalid option. Try again.")