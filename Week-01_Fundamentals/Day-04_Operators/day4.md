# 📘 Day 04 — Operators
Week 01: Fundamentals

⏱ Time: 2–3 Hours  
🎯 Focus: Learn how programs perform calculations and make decisions

---

## 🧠 Why Operators Matter

Operators are what make programs **do something useful**.

Without operators:
- No calculations
- No comparisons
- No decisions

Operators = **thinking tools for the computer**

---

## 🔢 Types of Operators (Python)

We focus on **three main types** today:

1. Arithmetic Operators  
2. Relational (Comparison) Operators  
3. Logical Operators  

---

## 1️⃣ Arithmetic Operators

Used for mathematical calculations.

| Operator | Meaning |
|--------|--------|
| + | Addition |
| - | Subtraction |
| * | Multiplication |
| / | Division |
| % | Modulus (remainder) |

### Example
```python
a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)
print("Remainder =", a % b)
```
## 2️⃣ Relational (Comparison) Operators
Used to compare values.
Result is always True or False.

| Operator | Meaning               |
| -------- | --------------------- |
| ==       | Equal to              |
| !=       | Not equal to          |
| >        | Greater than          |
| <        | Less than             |
| >=       | Greater than or equal |
| <=       | Less than or equal    |

### Example
```python
a = int(input("Enter a: "))
b = int(input("Enter b: "))

print(a > b)
print(a < b)
print(a == b)
print(a != b)

```
## 3️⃣ Logical Operators
Used to combine conditions.

| Operator | Meaning                      |
| -------- | ---------------------------- |
| and      | Both conditions must be True |
| or       | At least one condition True  |
| not      | Reverse the result           |

```python
age = int(input("Enter age: "))

print(age > 18 and age < 60)
print(age < 18 or age > 60)
print(not age > 18)
```
## 🛠 Practice — Even or Odd Checker
```python
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```
This combines:
- Arithmetic operator (%)
- Relational operator (==)
- Logical decision

### Task: Simple Calculator (Addition)
Steps:
1. Take numbers as input & store in variables
2. Perform arithmetic operations
3. Print the result
   
👉 If you know C or Java, try it there.
Otherwise, Python is enough.