# 🏦 ATM Simulation — Python (Week 01 Final Project)

This project is the **final capstone of Week 01 (Fundamentals)**  
It uses only core programming concepts — no OOP, no libraries.

---

## 🎯 Concepts Used
- Variables
- Input & Output
- Operators
- Conditions (if / elif / else)
- Loops (while)
- Menu-driven logic

---

## 🔁 Program Flow

1. User enters PIN
2. If PIN is correct → show menu
3. User can:
   - Check balance
   - Deposit money
   - Withdraw money
   - Exit
4. Program runs until user exits

---

## 🧠 Core Logic

Input → Decision → Action → Output → Repeat

This is how **real programs work**.

---

## ▶ How to Run

```bash
python atm.py
```

## ✅ Learning Outcome
After this project, you should:
- Think in program flow
- Understand how loops control programs
- Be confident with conditions
- This project marks Foundation Complete ✅


---

## 3️⃣ `atm.py` 

```python
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
```
## 🚫 Strict Rules (don’t break these)
- ❌ No classes
- ❌ No functions
- ❌ No imports
- ✅ Only logic
This is FOUNDATION training, not shortcuts.

---
