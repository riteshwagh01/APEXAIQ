# Regular Expressions (Regex)

Regular Expressions (Regex) are special patterns used to **search, match, extract, validate, and replace text**. They are widely used in data validation, text processing, web scraping, log analysis, and form validation.

Python provides built-in support for Regex through the **`re`** module.

---

# Why Use Regex?

Regex helps us to:

- Search for specific text in a string.
- Validate emails, phone numbers, and passwords.
- Extract required information from text.
- Replace unwanted text.
- Split strings based on patterns.

---

# Importing the Regex Module

```python
import re
```

---

# Basic Regex Functions

## 1. re.search()

Searches for the **first occurrence** of a pattern in a string.

### Syntax

```python
re.search(pattern, string)
```

### Example

```python
import re

text = "Python is easy to learn."

result = re.search("easy", text)

print(result)
```

### Output

```python
<re.Match object>
```

If the pattern is not found:

```python
None
```

---

## 2. re.findall()

Returns **all matches** as a list.

### Syntax

```python
re.findall(pattern, string)
```

### Example

```python
import re

text = "cat bat rat"

result = re.findall("at", text)

print(result)
```

### Output

```python
['at', 'at', 'at']
```

---

## 3. re.match()

Checks whether the pattern exists **only at the beginning** of the string.

### Example

```python
import re

text = "Python Programming"

result = re.match("Python", text)

print(result)
```

### Output

```python
<re.Match object>
```

If the string starts with another word:

```python
None
```

---

## 4. re.sub()

Replaces matched text with another string.

### Syntax

```python
re.sub(pattern, replacement, string)
```

### Example

```python
import re

text = "I like Java"

new_text = re.sub("Java", "Python", text)

print(new_text)
```

### Output

```python
I like Python
```

---

## 5. re.split()

Splits a string wherever the pattern matches.

### Example

```python
import re

text = "Apple,Banana,Mango"

result = re.split(",", text)

print(result)
```

### Output

```python
['Apple', 'Banana', 'Mango']
```

---

# Common Regex Symbols

| Symbol | Meaning | Example |
|---------|---------|---------|
| `.` | Matches any single character except a newline | `a.c` |
| `^` | Matches the beginning of a string | `^Hello` |
| `$` | Matches the end of a string | `Python$` |
| `*` | Matches zero or more occurrences | `ab*` |
| `+` | Matches one or more occurrences | `ab+` |
| `?` | Matches zero or one occurrence | `colou?r` |
| `[]` | Matches any one character inside the brackets | `[abc]` |
| `[^ ]` | Matches characters **not** inside the brackets | `[^0-9]` |
| `\d` | Matches any digit (0–9) | `\d+` |
| `\D` | Matches any non-digit | `\D+` |
| `\w` | Matches letters, digits, and underscore | `\w+` |
| `\W` | Matches non-word characters | `\W` |
| `\s` | Matches whitespace characters | `\s` |
| `\S` | Matches non-whitespace characters | `\S` |
| `\b` | Matches a word boundary | `\bword\b` |

---

# Practical Examples

## Example 1: Find Digits

```python
import re

text = "Age is 23"

result = re.findall(r"\d+", text)

print(result)
```

### Output

```python
['23']
```

**Explanation**

- `\d` → Matches a digit (0–9).
- `+` → One or more occurrences.

So, `\d+` matches one or more consecutive digits.

---

## Example 2: Find Words

```python
import re

text = "Python Java C++"

result = re.findall(r"\w+", text)

print(result)
```

### Output

```python
['Python', 'Java', 'C']
```

---

## Example 3: Find Email Pattern

```python
import re

text = "Contact us at abc@gmail.com"

email = re.findall(r"\S+@\S+", text)

print(email)
```

### Output

```python
['abc@gmail.com']
```

---

## Example 4: Extract a 10-Digit Phone Number

### Method 1: Using `\d{10}`

```python
import re

text = "My phone number is 9876543210."

number = re.findall(r"\d{10}", text)

print(number)
```

### Output

```python
['9876543210']
```

### Explanation

- `\d` → Matches a digit (0–9).
- `{10}` → Exactly 10 times.

Therefore,

```text
\d{10}
```

matches **exactly 10 consecutive digits**.

---

## What Happens If the String Contains 15 Digits?

Example

```python
import re

text = "123456789012345"

result = re.findall(r"\d{10}", text)

print(result)
```

### Output

```python
['1234567890']
```

**Explanation**

The regex `\d{10}` simply matches the **first 10 consecutive digits**. It does **not** check whether the number has extra digits after it.

---

## Extract Only a Valid Standalone 10-Digit Number

To ensure that only a complete 10-digit number is matched (and not part of a longer number), use **word boundaries (`\b`)**.

```python
import re

text = "123456789012345"

result = re.findall(r"\b\d{10}\b", text)

print(result)
```

### Output

```python
[]
```

The 15-digit number is ignored because it is **not** a standalone 10-digit number.

---

### Another Example

```python
import re

text = "Phone: 9876543210 and ID: 123456789012345"

result = re.findall(r"\b\d{10}\b", text)

print(result)
```

### Output

```python
['9876543210']
```

Only the valid standalone 10-digit phone number is matched.

---

## Example 5: Remove Extra Spaces

```python
import re

text = "Python     is      awesome"

result = re.sub(r"\s+", " ", text)

print(result)
```

### Output

```python
Python is awesome
```

---

# Difference Between Important Regex Functions

| Function | Purpose |
|----------|---------|
| `re.search()` | Finds the first occurrence of a pattern anywhere in the string |
| `re.match()` | Matches the pattern only at the beginning of the string |
| `re.findall()` | Returns all matches as a list |
| `re.sub()` | Replaces matched text with another string |
| `re.split()` | Splits the string wherever the pattern matches |

---

# Applications of Regex

- Email validation
- Phone number validation
- Password validation
- Form validation
- Web scraping
- Data cleaning
- Log file analysis
- Search and replace operations
- Extracting information from text

---

# Advantages of Regex

- Fast text searching
- Powerful pattern matching
- Reduces code complexity
- Easy to validate user input
- Useful in data processing and automation

---

# Summary

- Regex stands for **Regular Expression**.
- Python uses the **`re`** module for Regex operations.
- Regex is used to search, match, extract, replace, and validate text.
- `\d{10}` matches the **first 10 consecutive digits**, even if they are part of a longer number.
- `\b\d{10}\b` matches **only a standalone 10-digit number**, making it ideal for phone number validation.
- Common functions are `re.search()`, `re.match()`, `re.findall()`, `re.sub()`, and `re.split()`.
- Regex is widely used in email validation, phone number validation, text processing, and data extraction.