# Concurrent Password Strength Checker

A Python program that checks the strength of multiple passwords concurrently using `ThreadPoolExecutor`.

## Features
- Concurrent password checking
- Regex-based validation
- Strong, Medium, and Weak classification
- Exception handling
- List and dictionary comprehensions
- Unit testing

## Technologies
- Python 3
- Regex (`re`)
- ThreadPoolExecutor
- unittest

## Run
```bash
python password_checker.py
```

## Sample Output
```
admin123        -> Medium
Password@123    -> Strong
abc             -> Weak
```
