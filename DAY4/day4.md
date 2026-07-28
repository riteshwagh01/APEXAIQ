# Coding Standards

Coding standards (also called **coding conventions** or **coding guidelines**) are a set of rules and best practices that developers follow while writing code. Their purpose is to make code **readable, consistent, maintainable, and easier to debug**, especially when multiple people work on the same project.

---

## Why are Coding Standards Important?

- Improve code readability.
- Make collaboration easier.
- Reduce bugs and errors.
- Simplify maintenance and future updates.
- Help new developers understand the code quickly.

---

## Common Coding Standards

### 1. Meaningful Variable and Function Names

❌ **Bad**

```python
a = 10
b = 20
c = a + b
```

✅ **Good**

```python
price = 10
tax = 20
total_price = price + tax
```

---

### 2. Proper Indentation

Use consistent indentation (**Python uses 4 spaces**).

✅ **Good**

```python
if age >= 18:
    print("Eligible")
```

❌ **Bad**

```python
if age >= 18:
print("Eligible")
```

---

### 3. Follow Naming Conventions (Python – PEP 8)

#### Variables and Functions (`snake_case`)

```python
student_name

def calculate_total():
    pass
```

#### Classes (`PascalCase`)

```python
class StudentDetails:
    pass
```

#### Constants (`UPPER_CASE`)

```python
MAX_USERS = 100
```

---

### 4. Write Comments Only When Necessary

✅ **Good**

```python
# Calculate GST amount
gst = price * 0.18
```

❌ **Bad**

```python
# Add two numbers
result = a + b
```

---

### 5. Keep Functions Small

Each function should perform **one specific task**.

```python
def calculate_area(radius):
    return 3.14 * radius * radius
```

---

### 6. Avoid Duplicate Code

❌ **Bad**

```python
print("Welcome")
print("Welcome")
print("Welcome")
```

✅ **Good**

```python
for _ in range(3):
    print("Welcome")
```

---

### 7. Handle Errors Properly

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid integer.")
```

---

### 8. Use Blank Lines for Readability

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b
```

---

### 9. Remove Unused Code and Imports

❌ **Bad**

```python
import math

x = 10
```

If `math` is not used, remove the import statement.

---

### 10. Maintain Consistent Formatting

Use the same quotation style, spacing, and indentation throughout the project.

```python
name = "Ritesh"
age = 21

print(f"{name} is {age} years old.")
```

---

# Python Coding Standards (PEP 8)

Python developers generally follow **PEP 8**, which recommends:

- Use **4 spaces** for indentation.
- Keep line length around **79–88 characters**.
- Use **snake_case** for variables and functions.
- Use **PascalCase** for class names.
- Use **UPPER_CASE** for constants.
- Leave **two blank lines** between top-level functions and classes.
- Write **one import per line**.
- Maintain proper spacing around operators and commas.

---

# Example

## Without Coding Standards

```python
x=10
y=20
z=x+y
print(z)
```

## With Coding Standards

```python
first_number = 10
second_number = 20

total = first_number + second_number

print(total)
```