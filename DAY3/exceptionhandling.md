# Exception Handling

## What is Exception Handling?

Exception Handling is a technique used to handle **runtime errors** so that the program does **not crash** and continues executing normally.

Python uses the following keywords for exception handling:

- `try`
- `except`
- `else`
- `finally`
- `raise`

---

# Why Do We Need Exception Handling?

## Without Exception Handling

```python
num = 10

print(num / 0)

print("Program Finished")
```

### Output

```text
ZeroDivisionError: division by zero
```

The program stops immediately.

---

## With Exception Handling

```python
try:
    num = 10
    print(num / 0)

except ZeroDivisionError:
    print("Cannot divide by zero.")

print("Program Finished")
```

### Output

```text
Cannot divide by zero.
Program Finished
```

### Explanation

```python
try:
```

Put the code that **may cause an exception** inside the `try` block.

```python
except ZeroDivisionError:
```

If a `ZeroDivisionError` occurs, Python jumps to this block.

```python
print("Program Finished")
```

The program continues normally after handling the exception.

---

# Flow of try-except

```text
Program Starts

↓

try Block

↓

Error?

↓

No --------------------→ Skip except

↓

Yes

↓

except Block

↓

Continue Program
```

---

# Example 1: Handling ZeroDivisionError

```python
try:
    num = 20
    result = num / 0
    print(result)

except ZeroDivisionError:
    print("Division by zero is not allowed.")
```

### Output

```text
Division by zero is not allowed.
```

---

# Example 2: Handling ValueError

Suppose the user enters text instead of a number.

```python
try:
    age = int(input("Enter Age: "))
    print(age)

except ValueError:
    print("Please enter numbers only.")
```

### Input

```text
abc
```

### Output

```text
Please enter numbers only.
```

### Explanation

```python
int("abc")
```

cannot convert `"abc"` into an integer, so Python raises a `ValueError`.

---

# Example 3: Handling IndexError

```python
try:
    numbers = [10,20,30]

    print(numbers[5])

except IndexError:
    print("Index does not exist.")
```

### Output

```text
Index does not exist.
```

---

# Example 4: Handling FileNotFoundError

```python
try:
    file = open("data.txt")

except FileNotFoundError:
    print("File not found.")
```

### Output

```text
File not found.
```

---

# Handling Multiple Exceptions

A program can have multiple `except` blocks.

```python
try:
    number = int(input("Enter Number: "))
    print(10 / number)

except ValueError:
    print("Invalid Input.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

## Case 1

### Input

```text
abc
```

### Output

```text
Invalid Input.
```

---

## Case 2

### Input

```text
0
```

### Output

```text
Cannot divide by zero.
```

---

# Using a Generic Exception

Sometimes we don't know which exception may occur.

```python
try:
    number = int(input("Enter Number: "))
    print(10 / number)

except Exception as e:
    print("Error:", e)
```

### Input

```text
0
```

### Output

```text
Error: division by zero
```

Here,

```python
Exception as e
```

stores the actual error inside `e`.

---

# else Block

The `else` block runs **only if no exception occurs**.

```python
try:
    number = int(input("Enter Number: "))

except ValueError:
    print("Invalid Number")

else:
    print("Square =", number * number)
```

### Input

```text
5
```

### Output

```text
Square = 25
```

### Input

```text
abc
```

### Output

```text
Invalid Number
```

---

# finally Block

The `finally` block **always executes**, whether an exception occurs or not.

```python
try:
    print(10 / 2)

except ZeroDivisionError:
    print("Error")

finally:
    print("Program Ended")
```

### Output

```text
5.0
Program Ended
```

Even if an error occurs:

```python
try:
    print(10 / 0)

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Program Ended")
```

### Output

```text
Cannot divide by zero
Program Ended
```

---

# raise Keyword

We can create our own exception using `raise`.

```python
age = int(input("Enter Age: "))

if age < 18:
    raise ValueError("Age must be at least 18.")

print("Eligible")
```

### Input

```text
15
```

### Output

```text
ValueError: Age must be at least 18.
```

---

# Complete Example

```python
try:
    number = int(input("Enter Number: "))
    result = 100 / number

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")

else:
    print("Result =", result)

finally:
    print("Thank You")
```

## Case 1

### Input

```text
20
```

### Output

```text
Result = 5.0
Thank You
```

---

## Case 2

### Input

```text
0
```

### Output

```text
Division by zero is not allowed.
Thank You
```

---

## Case 3

### Input

```text
abc
```

### Output

```text
Please enter numbers only.
Thank You
```

---

# Execution Flow

```text
Program Starts

↓

try

↓

Exception?

↓

No

↓

else

↓

finally

↓

Program Ends
```

OR

```text
Program Starts

↓

try

↓

Exception

↓

except

↓

finally

↓

Program Ends
```

---

# Common Exceptions

| Exception | Reason |
|-----------|--------|
| `ZeroDivisionError` | Dividing by zero |
| `ValueError` | Invalid input |
| `TypeError` | Wrong data type |
| `IndexError` | Invalid list index |
| `KeyError` | Dictionary key not found |
| `FileNotFoundError` | File does not exist |
| `NameError` | Variable not defined |

---

# Interview Definition

> **Exception Handling is a mechanism in Python that uses `try`, `except`, `else`, `finally`, and `raise` to detect and handle runtime errors, preventing the program from crashing and allowing it to continue executing normally.**