# 📘 Day 05 — Conditional Statements
Week 01: Fundamentals

⏱ Time: 2–3 Hours  
🎯 Focus: Teach the program how to make decisions

---

## 🧠 Why Conditional Statements Matter

Until now, programs:
- Took input
- Did calculations
- Gave output

But they **could not decide**.

Real programs must answer questions like:
- Is the user eligible?
- Is the password correct?
- Is the number valid?

👉 Conditional statements make programs **intelligent**.

---

## ❓ What is a Condition?

A condition is an expression that evaluates to:
- `True`
- `False`

Example:
```python
age > 18
```
--- 

## 🔑 Types of Conditional Statements (Python)
1. if
2. if else
3. if elif else

---

## 1️⃣ if Statement
Used when one condition needs to be checked.

### Syntax
```python
if condition:
    statement
```
### Example
```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
```

---

## 2️⃣ if else Statement
Used when there are two possible outcomes.

### Syntax
```python
if condition:
    statement
else:
    statement
```
### Example
```python
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

---

## 3️⃣ if elif else Statement
Used when there are multiple conditions.

### Syntax
```python
if condition1:
    statement
elif condition2:
    statement
else:
    statement
```
### Example
```python
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
```

---

## 🔁 How Decision-Making Works
Flow:
```sql
Check condition → True? → Execute block
               → False? → Check next condition
```
Only one block executes.

## 🛠 Practice 1 — Positive, Negative or Zero
```python
num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")
```
## 🛠 Practice 2 — Simple Login Check
```python
password = input("Enter password: ")

if password == "admin123":
    print("Login successful")
else:
    print("Incorrect password")
```

---

## ❌ Common Beginner Mistakes (STOP THIS)

❌ Using = instead of ==
❌ Forgetting indentation
❌ Writing multiple if instead of elif
❌ Not testing all cases

Python logic depends on indentation.

---

## Task: Simple Calculator (Addition)
Steps:
1. Take numbers as input & store in variables
2. Take Operation as input & store
3. Perform arithmetic operations based on taken operation as input
4. Print the result