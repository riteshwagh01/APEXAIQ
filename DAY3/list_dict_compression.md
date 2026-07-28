# List Comprehension and Dictionary Comprehension

List comprehension and dictionary comprehension are Python features that allow you to create lists and dictionaries in a concise and readable way. They reduce the amount of code compared to traditional loops.

---

# List Comprehension

## Definition

**List comprehension** is a concise way to create a new list by applying an expression to each element of an iterable (such as a list, tuple, string, or range).

---

## Basic Syntax

```python
new_list = [expression for item in iterable]
```

Let's understand every part.

```python
square = [num * num for num in range(5)]
```

Break it down:

```text
[num * num      for      num      in      range(5)]

Expression      Loop   Variable    Iterable
```

| Part | Meaning |
|------|---------|
| Expression | What should be stored in the new list |
| `for` | Loop |
| `num` | Current element |
| `range(5)` | Collection to iterate |

---

## Step-by-Step Working

Code

```python
square = [num * num for num in range(5)]
```

Python internally performs

```python
square = []

for num in range(5):
    square.append(num * num)
```

### Iteration

| num | num × num | Added to List |
|----:|----------:|---------------|
| 0 | 0 | `[0]` |
| 1 | 1 | `[0, 1]` |
| 2 | 4 | `[0, 1, 4]` |
| 3 | 9 | `[0, 1, 4, 9]` |
| 4 | 16 | `[0, 1, 4, 9, 16]` |

Final Output

```python
[0, 1, 4, 9, 16]
```

---

## Example 1: Square Numbers

### Without List Comprehension

```python
numbers = [1, 2, 3, 4]

result = []

for i in numbers:
    result.append(i * i)

print(result)
```

### With List Comprehension

```python
numbers = [1, 2, 3, 4]

result = [i * i for i in numbers]

print(result)
```

### Output

```python
[1, 4, 9, 16]
```

---

## Example 2: Double Every Number

```python
numbers = [2, 4, 6]

double = [i * 2 for i in numbers]

print(double)
```

### Output

```python
[4, 8, 12]
```

---

## Example 3: Convert Strings to Uppercase

```python
names = ["ram", "shyam", "amit"]

upper = [name.upper() for name in names]

print(upper)
```

### Output

```python
['RAM', 'SHYAM', 'AMIT']
```

---

## Example 4: Find Length of Words

```python
words = ["Python", "Java", "C"]

length = [len(word) for word in words]

print(length)
```

### Output

```python
[6, 4, 1]
```

---

# List Comprehension with Condition

## Syntax

```python
new_list = [expression for item in iterable if condition]
```

Example

```python
numbers = [1, 2, 3, 4, 5, 6]

even = [i for i in numbers if i % 2 == 0]

print(even)
```

### Output

```python
[2, 4, 6]
```

### Working

| Number | Condition (`i % 2 == 0`) | Added? |
|-------:|--------------------------|--------|
| 1 | False | No |
| 2 | True | Yes |
| 3 | False | No |
| 4 | True | Yes |
| 5 | False | No |
| 6 | True | Yes |

---

## Another Example

Find numbers greater than 50.

```python
numbers = [20, 45, 67, 90, 34]

result = [i for i in numbers if i > 50]

print(result)
```

### Output

```python
[67, 90]
```

---

# List Comprehension with if-else

## Syntax

```python
[expression_if_true if condition else expression_if_false for item in iterable]
```

Example

```python
numbers = [1, 2, 3, 4, 5]

result = ["Even" if i % 2 == 0 else "Odd" for i in numbers]

print(result)
```

### Output

```python
['Odd', 'Even', 'Odd', 'Even', 'Odd']
```

---

# Nested List Comprehension

### Normal Loop

```python
matrix = []

for i in range(2):
    for j in range(3):
        matrix.append((i, j))
```

### Using List Comprehension

```python
matrix = [(i, j) for i in range(2) for j in range(3)]

print(matrix)
```

### Output

```python
[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]
```

---

# Advantages of List Comprehension

- Less code
- Easy to read
- Faster than traditional loops (in many cases)
- Cleaner syntax

---

# Dictionary Comprehension

## Definition

**Dictionary comprehension** is a concise way to create dictionaries by generating key-value pairs in a single line of code.

---

## Basic Syntax

```python
new_dict = {key: value for item in iterable}
```

Example

```python
square = {i: i * i for i in range(5)}

print(square)
```

### Output

```python
{
    0: 0,
    1: 1,
    2: 4,
    3: 9,
    4: 16
}
```

---

## How It Works

Python converts

```python
{i: i * i for i in range(5)}
```

into

```python
square = {}

for i in range(5):
    square[i] = i * i
```

---

## Example 1: Store Square of Numbers

```python
square = {i: i * i for i in range(1, 6)}

print(square)
```

### Output

```python
{
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25
}
```

---

## Example 2: Word Length

```python
words = ["Python", "Java", "C"]

length = {word: len(word) for word in words}

print(length)
```

### Output

```python
{
    'Python': 6,
    'Java': 4,
    'C': 1
}
```

---

## Example 3: Number and Cube

```python
cube = {i: i ** 3 for i in range(1, 6)}

print(cube)
```

### Output

```python
{
    1: 1,
    2: 8,
    3: 27,
    4: 64,
    5: 125
}
```

---

# Dictionary Comprehension with Condition

## Syntax

```python
{key: value for item in iterable if condition}
```

Example

```python
square = {i: i * i for i in range(10) if i % 2 == 0}

print(square)
```

### Output

```python
{
    0: 0,
    2: 4,
    4: 16,
    6: 36,
    8: 64
}
```

Only even numbers are included.

---

## Example Using Strings

```python
names = ["Ram", "Shyam", "Amit"]

result = {name: name.upper() for name in names}

print(result)
```

### Output

```python
{
    'Ram': 'RAM',
    'Shyam': 'SHYAM',
    'Amit': 'AMIT'
}
```

---

# Difference Between List and Dictionary Comprehension

| Feature | List Comprehension | Dictionary Comprehension |
|---------|---------------------|--------------------------|
| Creates | List | Dictionary |
| Brackets | `[]` | `{}` |
| Stores | Values only | Key-value pairs |
| Syntax | `[expression for item in iterable]` | `{key: value for item in iterable}` |

### Example

**List**

```python
[i * i for i in range(5)]
```

Output

```python
[0, 1, 4, 9, 16]
```

**Dictionary**

```python
{i: i * i for i in range(5)}
```

Output

```python
{
    0: 0,
    1: 1,
    2: 4,
    3: 9,
    4: 16
}
```

---

# When Should You Use Comprehension?

## Use Comprehension When

- You want to create a new list or dictionary from an existing iterable.
- The logic is simple (e.g., applying a function or filtering items).

## Avoid Comprehension When

- The logic becomes too complex or deeply nested, reducing readability.
- You need multiple independent operations or side effects (such as printing or writing to a file).

---

