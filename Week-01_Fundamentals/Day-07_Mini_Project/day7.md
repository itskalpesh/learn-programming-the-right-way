# 📘 Day 07 — Mini Project (Calculator System)
Week 01: Fundamentals

⏱ Time: 2–3 Hours  
🎯 Focus: Apply everything learned in Week 01 to build a real program

---

## 🧠 Why Day 07 Matters

Until now, you learned:
- Variables
- Input & Output
- Operators
- Conditions
- Loops

Day 07 is NOT about learning something new.  
Day 07 is about **connecting everything together**.

👉 This is how real programmers learn.

---

## 🛠 Mini Project Overview

### Project Name:
**Menu-Driven Calculator (CLI)**

### What this project proves:
- You understand program flow
- You can handle user input
- You can make decisions
- You can repeat logic
- You can exit cleanly

---

## 📋 Features Required (MANDATORY)

Your calculator MUST:
- Take two numbers as input
- Ask user for operation
- Perform calculation
- Repeat until user exits
- Handle invalid operations
- Prevent division by zero

If any feature is missing → project is incomplete.

---

## 🧩 Project Logic (READ THIS)
Start program
↓
Show menu
↓
Take input
↓
Perform operation
↓
Show result
↓
Ask to continue
↓
Exit or repeat

---

## ✅ Final Project Code (Reference Implementation)

```python
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
```
## 🧠 What You Learned in Week 01 (IMPORTANT)

✔ How programs think
✔ How data flows
✔ How decisions are made
✔ How repetition works
✔ How to build a usable CLI program

This is real progress, not tutorial hopping.

---

## ❌ Common Mistakes (DON’T DO THIS)

❌ Copying code without running
❌ Not testing wrong inputs
❌ Skipping edge cases
❌ Jumping to frameworks now

Foundations come first.