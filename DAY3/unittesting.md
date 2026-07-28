# Unit Testing

## What is Unit Testing?

Unit Testing is the process of testing **individual functions (units)** of a program to verify that they return the expected output.

Python provides a built-in module called **`unittest`** for writing unit tests.

First import it:

```python
import unittest
```

---

# Example 1: Without Unit Testing

Suppose you wrote a function.

```python
def add(a, b):
    return a + b

print(add(2, 3))
```

### Output

```text
5
```

### Question:

How do you know this function works for every input?

You manually test.

```python
print(add(2,3))
print(add(10,20))
print(add(-5,5))
print(add(100,200))
```

This becomes difficult if there are hundreds of functions.

So we use **Unit Testing**.

---

# Example 2: Using unittest

```python
import unittest

def add(a, b):
    return a + b


class TestAddition(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2,3), 5)


if __name__ == "__main__":
    unittest.main()
```

### Output

```text
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```

---

# Step-by-Step Explanation

## Step 1

Import unittest

```python
import unittest
```

This imports Python's built-in testing framework.

---

## Step 2

Create the function

```python
def add(a,b):
    return a+b
```

This is the function we want to test.

---

## Step 3

Create a test class

```python
class TestAddition(unittest.TestCase):
```

Every test class **must inherit**

```python
unittest.TestCase
```

This gives us testing methods like

- `assertEqual()`
- `assertTrue()`
- `assertFalse()`
- etc.

---

## Step 4

Create a test function

```python
def test_add(self):
```

Notice the name starts with

```python
test_
```

Why?

Because **`unittest` automatically runs every method whose name starts with `test`.**

---

## Step 5

Write the test

```python
self.assertEqual(add(2,3),5)
```

Meaning

```text
Expected Output = 5

Actual Output = add(2,3)
```

If both are equal

✅ Test Passes

Otherwise

❌ Test Fails

---

## Step 6

Run the tests

```python
if __name__ == "__main__":
    unittest.main()
```

This tells Python to execute all test methods.

---

# What if the Answer is Wrong?

Suppose

```python
def add(a,b):
    return a-b
```

Now run

```python
self.assertEqual(add(2,3),5)
```

### Output

```text
FAIL

AssertionError: -1 != 5
```

Meaning

```text
Expected = 5

Actual = -1
```

So the test fails immediately.

---

# Multiple Test Cases

```python
import unittest

def add(a,b):
    return a+b

class TestAddition(unittest.TestCase):

    def test_add1(self):
        self.assertEqual(add(2,3),5)

    def test_add2(self):
        self.assertEqual(add(10,20),30)

    def test_add3(self):
        self.assertEqual(add(-5,5),0)

if __name__=="__main__":
    unittest.main()
```

### Output

```text
...
----------------------------------------------------------------------
Ran 3 tests

OK
```

Three dots (`...`) mean

```text
Test 1 Passed

Test 2 Passed

Test 3 Passed
```

---

# Common Assertion Methods

## 1. assertEqual()

Checks whether two values are equal.

```python
self.assertEqual(10,10)
```

Pass ✅

```python
self.assertEqual(10,20)
```

Fail ❌

---

## 2. assertTrue()

Checks whether a condition is True.

```python
self.assertTrue(5>2)
```

Pass ✅

---

## 3. assertFalse()

Checks whether a condition is False.

```python
self.assertFalse(5<2)
```

Pass ✅

---

## 4. assertIn()

Checks whether an item exists.

```python
self.assertIn("a","apple")
```

Pass ✅

---

## 5. assertNotIn()

Checks whether an item does not exist.

```python
self.assertNotIn("z","apple")
```

Pass ✅

---

# Why Use Unit Testing?

Instead of doing

```python
print(add(2,3))
print(add(10,20))
print(add(100,200))
print(add(500,600))
```

you simply write tests once.

Whenever you modify your code,

```text
Run Tests

↓

Immediately know

Pass ✓

or

Fail ✗
```

---

# Interview Question

## Q. Why is the function name `test_add()` instead of `add_test()`?

### Answer:

Because the **`unittest` framework automatically discovers and executes methods whose names start with `test`.** If the method name doesn't start with `test`, it won't be run automatically.

---

# Interview Definition

> **Unit Testing is a software testing technique in which individual units (such as functions or methods) are tested independently using a testing framework like `unittest` to verify that they produce the expected results.**