# 📘 Day 06 — Loops
Week 01: Fundamentals

⏱ Time: 2–3 Hours  
🎯 Focus: Repeat logic, control program flow

---

## 🧠 Why Loops Matter (READ THIS CAREFULLY)

Without loops:
- Program runs **once**
- User makes a mistake → program **dies**
- Real apps ❌

With loops:
- Program repeats
- User can retry
- Program becomes **usable**

---

## 🔁 What is a Loop?

A loop allows code to run **again and again** until a condition is met.

In Python, today we learn:
- `while` loop

---

## 🔑 Core Rule (VERY IMPORTANT)

Condition controls the loop.  
If condition never becomes false → ❌ infinite loop.

---

## 🧩 Syntax — while loop

```python
while condition:
    # code to repeat
```
## Example:
```python
count = 1
while count <= 5:
    print(count)
    count += 1
```
### ⚠️ Infinite Loop Example (DON’T DO THIS)
```python
while True:
    print("Hello")
```

## Task: Simple Calculator (Addition)
Steps:
1. Take numbers as input & store in variables
2. Take Operation as input & store
3. Perform arithmetic operations based on taken operation as input
4. Print the result
5. take user choise y/n as input for continue run or exit
6. If yes them Calculator runs multiple times until User can exit safely