# Python Core Concepts (Part 1)

This README explains the following Python core topics in simple English with examples.

## Topics Covered

1. Python Memory Management
2. Object Identity, Mutability, and the Data Model
3. Descriptors and the Attribute Lookup Protocol
4. Metaclasses
5. The Global Interpreter Lock (GIL)
6. Threading vs Multiprocessing vs Asyncio

---

# 1. Python Memory Management

## What is Python Memory Management?

Memory management is the process of storing, using, and removing data from RAM while a Python program is running.

Unlike C or C++, Python automatically manages memory, so programmers don't need to manually allocate or free memory.

Python mainly uses:

- Reference Counting
- Garbage Collection (GC)

---

## Why is it Important?

Without memory management:

- Memory usage keeps increasing.
- Programs become slow.
- Memory leaks may occur.
- Applications may crash.

Python automatically prevents most of these issues.

---

## How Memory Works

Example

```python
x = 10
```

Python creates an integer object in memory.

```
Memory

10
↑
|
x
```

Here, `x` stores the reference (address) of the object, not the object itself.

---

## Reference Counting

Python keeps track of how many variables point to an object.

### Example

```python
x = 100
```

```
100
↑
|
x

Reference Count = 1
```

---

```python
y = x
```

```
      x
      |
      ↓
     100
      ↑
      |
      y

Reference Count = 2
```

---

```python
del x
```

```
100
↑
|
y

Reference Count = 1
```

---

```python
del y
```

Reference Count becomes **0**.

Python immediately removes the object from memory.

---

## Circular References

Example

```python
a = []
b = []

a.append(b)
b.append(a)
```

```
a → b
↑   ↓
└───┘
```

Even after

```python
del a
del b
```

both objects still reference each other.

Reference counting cannot delete them.

---

## Garbage Collector (GC)

Garbage Collector removes unreachable objects, including circular references.

```python
import gc

gc.collect()
```

---

## Private Heap

Python stores all objects in a special memory area called the **Private Heap**.

Only Python's Memory Manager can access this memory.

---

## Memory Pool

Python keeps a memory pool so it can reuse memory instead of asking the operating system every time.

This improves performance.

---

## Memory Flow

```
Create Object
      │
      ▼
Memory Allocated
      │
      ▼
Reference Count Increases
      │
      ▼
Reference Removed
      │
      ▼
Reference Count = 0
      │
      ▼
Object Deleted

OR

Circular Reference
      │
      ▼
Garbage Collector Removes It
```

---

## Interview Questions

### What is Python Memory Management?

Automatic management of RAM using Reference Counting and Garbage Collection.

### Why is Garbage Collection needed?

Because Reference Counting cannot remove circular references.

### Which module controls Garbage Collection?

```python
import gc
```

---

# 2. Object Identity, Mutability, and the Data Model

## What is Object Identity?

Every object created in Python has a unique identity.

You can check it using

```python
x = 10

print(id(x))
```

Example Output

```
140735820
```

The value may differ on every computer.

---

## What is Mutability?

Mutability means whether an object's value can be changed after creation.

### Mutable Objects

- list
- dictionary
- set
- bytearray

Example

```python
numbers = [1, 2, 3]

numbers.append(4)

print(numbers)
```

Output

```
[1, 2, 3, 4]
```

The original object changes.

---

### Immutable Objects

- int
- float
- string
- tuple
- frozenset

Example

```python
name = "Python"

name = name + "3"

print(name)
```

Output

```
Python3
```

Python creates a new object instead of modifying the old one.

---

## Data Model

Everything in Python is an object.

Even

```python
10
"Hello"
True
[]
{}
```

are objects.

Python objects contain

- Identity
- Type
- Value

---

## Special Methods

The data model uses magic methods.

Example

```python
class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

s = Student("Ritesh")

print(s)
```

Output

```
Ritesh
```

---

## Interview Questions

### Difference between Mutable and Immutable?

Mutable objects can change.

Immutable objects cannot.

### Which objects are immutable?

String, Integer, Float, Tuple, Boolean.

### Which function returns object identity?

```python
id()
```

---

# 3. Descriptors and the Attribute Lookup Protocol

## What is a Descriptor?

A descriptor is an object that controls how another object's attribute is accessed.

Descriptors are created using

- __get__()
- __set__()
- __delete__()

---

## Example

```python
class Demo:

    def __get__(self, instance, owner):
        print("Getting value")
        return 100

class Test:

    value = Demo()

t = Test()

print(t.value)
```

Output

```
Getting value
100
```

---

## Attribute Lookup Order

Whenever we write

```python
obj.name
```

Python searches in this order

```
1. Instance attributes

↓

2. Class attributes

↓

3. Parent classes

↓

4. Descriptors

↓

5. __getattr__()

↓

AttributeError
```

---

## Why are Descriptors Used?

They are used in

- Properties
- ORMs
- Validation
- Django Models
- SQLAlchemy

---

## Interview Questions

### Which methods create a descriptor?

```
__get__()

__set__()

__delete__()
```

---

# 4. Metaclasses

## What is a Metaclass?

A metaclass is a class that creates other classes.

```
Object
↓

Class

↓

Metaclass
```

Everything in Python is an object.

Every class is also an object.

Classes are created by a metaclass.

---

## Default Metaclass

Python uses

```python
type
```

---

## Example

```python
class Student:
    pass

print(type(Student))
```

Output

```
<class 'type'>
```

---

## Creating a Metaclass

```python
class MyMeta(type):
    pass

class Test(metaclass=MyMeta):
    pass
```

---

## Why Use Metaclasses?

- Validation
- Automatic registration
- Framework development
- API creation

---

## Interview Questions

### What creates classes in Python?

```
type
```

---

# 5. The Global Interpreter Lock (GIL)

## What is GIL?

GIL stands for

**Global Interpreter Lock**

It is a lock inside CPython that allows only one thread to execute Python bytecode at a time.

---

## Why Does Python Use GIL?

It protects memory from corruption.

Without GIL, two threads could modify the same object simultaneously.

---

## Example

```
Thread A

↓

Gets GIL

↓

Runs

↓

Releases GIL

↓

Thread B Runs
```

Only one thread executes Python code at any moment.

---

## Advantages

- Simpler memory management
- Prevents race conditions for many built-in operations

---

## Disadvantages

- CPU-bound multithreading doesn't scale well
- Only one thread executes Python bytecode at a time

---

## When Doesn't GIL Matter?

For I/O operations

Examples

- Downloading files
- Reading files
- API requests
- Database queries

Threads can wait for I/O while another thread runs.

---

## Interview Questions

### Does GIL block multiprocessing?

No.

Every process has its own Python interpreter and its own GIL.

---

# 6. Threading vs Multiprocessing vs Asyncio

## Threading

Multiple threads inside one process.

```
Process

├── Thread 1

├── Thread 2

└── Thread 3
```

### Best For

- Network calls
- File reading
- API requests
- Database operations

---

## Multiprocessing

Multiple independent processes.

```
CPU

├── Process 1

├── Process 2

└── Process 3
```

Each process has its own memory and its own GIL.

### Best For

- Image Processing
- Machine Learning
- Video Processing
- Scientific Computing

---

## Asyncio

Single thread handling many tasks using asynchronous programming.

```
Task 1

↓

Waiting

↓

Task 2

↓

Waiting

↓

Task 3
```

No extra threads are created.

---

## Comparison

| Feature | Threading | Multiprocessing | Asyncio |
|----------|-----------|----------------|----------|
| GIL | Yes | No | Yes |
| Memory | Shared | Separate | Shared |
| Best For | I/O Tasks | CPU Tasks | Massive I/O |
| Speed | Medium | High | Very High for I/O |

---

## Example (Threading)

```python
import threading

def hello():
    print("Hello")

t = threading.Thread(target=hello)

t.start()
t.join()
```

---

## Example (Multiprocessing)

```python
from multiprocessing import Process

def hello():
    print("Hello")

p = Process(target=hello)

p.start()
p.join()
```

---

## Example (Asyncio)

```python
import asyncio

async def hello():
    print("Hello")

asyncio.run(hello())
```

---

## Interview Questions

### Which is best for CPU-intensive tasks?

Multiprocessing

---

### Which is best for API calls?

Threading or Asyncio

---

### Which is best for thousands of concurrent network requests?

Asyncio

---

# Summary

| Topic | Key Point |
|--------|-----------|
| Memory Management | Python automatically manages memory using Reference Counting and Garbage Collection. |
| Object Identity | Every object has a unique identity, type, and value. |
| Mutability | Mutable objects can change; immutable objects cannot. |
| Descriptors | Control how attributes are accessed using `__get__`, `__set__`, and `__delete__`. |
| Metaclasses | Classes that create other classes; default metaclass is `type`. |
| GIL | Allows only one thread to execute Python bytecode at a time in CPython. |
| Threading | Best for I/O-bound tasks. |
| Multiprocessing | Best for CPU-bound tasks; each process has its own GIL. |
| Asyncio | Best for handling many concurrent I/O tasks efficiently in a single thread. |


# Python Advanced Concepts - Part 2

## APIs, Networking, and Software Design

This document covers advanced Python topics related to concurrency, APIs, authentication, and REST API development.

## Topics Covered

1. Race Conditions and Thread-Safety
2. HTTP Session Management
3. Authentication Mechanisms
4. Building Resilient API Clients
5. REST API Design Principles
6. Custom Requests Adapters and Hooks


---

# 1. Race Conditions and Thread-Safety

## What is a Race Condition?

A race condition occurs when multiple threads access and modify the same shared resource at the same time, causing unexpected or incorrect results.

### Example:

```python
balance = 100

Thread 1:
balance = balance + 50

Thread 2:
balance = balance + 20
```

Expected output:

```
170
```

But because both threads may access the old value simultaneously, the result can be incorrect.

---

## Why Race Conditions Occur?

A simple operation like:

```python
balance += 10
```

actually contains multiple steps:

```
1. Read value
2. Add value
3. Store updated value
```

Another thread can interrupt during these steps.

---

# Thread Safety

## What is Thread Safety?

Thread safety means that a program continues to work correctly when multiple threads access shared data.

---

## Using Locks

Python provides locks to protect critical sections.

Example:

```python
import threading

lock = threading.Lock()

with lock:
    balance += 10
```

Only one thread can execute the protected code at a time.

---

## Synchronization Tools

Python provides:

- Lock
- RLock
- Semaphore
- Event
- Condition


---

# 2. HTTP Session Management

## What is HTTP Session Management?

HTTP is a stateless protocol.

It means the server does not remember previous requests.

Example:

```
Request 1 → Server
Request 2 → Server
Request 3 → Server
```

Each request is independent.

---

## Why Sessions are Required?

Example:

```
Login
  |
  ↓
Add Product
  |
  ↓
Checkout
```

The website needs to remember the user.

---

# Session Management Techniques

## 1. Cookies

Cookies are small data stored in the user's browser.

Example:

```
User_ID = 12345
```

---

## 2. Session ID

The server creates a unique session identifier.

Example:

```
Session_ID = abc123
```

The client sends this ID with future requests.

---

## 3. Token-Based Sessions

Modern applications use tokens.

Example:

```
Authorization:
Bearer token_value
```

Common token:

- JWT (JSON Web Token)


---

## Python Session Example

```python
import requests

session = requests.Session()

session.get("https://example.com")

session.post(
    "https://example.com/login",
    data={
        "username":"user",
        "password":"password"
    }
)
```

The session automatically manages cookies.


---

# 3. Authentication Mechanisms

## What is Authentication?

Authentication verifies the identity of a user.

Question:

```
Who are you?
```

Example:

```
Username + Password
```

---

# Types of Authentication

## 1. Basic Authentication

Username and password are sent with every request.

Example:

```
Authorization:
Basic username:password
```

---

## 2. Token Authentication

The server generates a token after login.

Flow:

```
User Login

↓

Server Generates Token

↓

Client Sends Token With Requests
```

---

## 3. JWT Authentication

JWT stands for:

```
JSON Web Token
```

Structure:

```
Header.Payload.Signature
```

Advantages:

- Stateless
- Fast
- Scalable


---

## 4. OAuth

OAuth allows users to access applications without sharing passwords.

Examples:

- Login with Google
- Login with GitHub


---

# Authentication vs Authorization

| Authentication | Authorization |
|---|---|
| Verifies identity | Verifies permissions |
| Who are you? | What can you access? |
| Login process | Access control |


---

# 4. Building Resilient API Clients

## What is an API Client?

An API client is a program that communicates with external services using APIs.

Examples:

- Payment API
- Weather API
- Database API


---

# Why Build Resilient API Clients?

Networks can fail because of:

- Server downtime
- Slow responses
- Connection errors


A resilient API client handles these failures properly.

---

# Important Techniques

## 1. Timeout Handling

Never allow requests to wait forever.

Example:

```python
import requests

response = requests.get(
    url,
    timeout=5
)
```

---

## 2. Retry Mechanism

If a request fails, try again.

Example:

```
Request Failed

↓

Wait

↓

Retry
```

---

## 3. Exponential Backoff

Increasing delay between retries.

Example:

```
First retry  → 1 second

Second retry → 2 seconds

Third retry  → 4 seconds
```

---

## 4. Error Handling

Example:

```python
try:
    response = requests.get(url)

except Exception:
    print("Request failed")
```

---

## 5. Logging

Record failures and important events.

Example:

```
API Timeout
Payment Failed
Server Error
```


---

# 5. REST API Design Principles

## What is REST?

REST stands for:

```
Representational State Transfer
```

It is a standard approach for designing web APIs.


---

# REST Principles

## 1. Resource-Based URLs

Good:

```
GET /users
```

Bad:

```
GET /getUsers
```

---

## 2. HTTP Methods

### GET

Used to retrieve data.

Example:

```
GET /users
```

---

### POST

Used to create new data.

Example:

```
POST /users
```

---

### PUT

Used to update existing data.

Example:

```
PUT /users/1
```

---

### DELETE

Used to remove data.

Example:

```
DELETE /users/1
```

---

# 3. Stateless Communication

Every request should contain all required information.

---

# 4. HTTP Status Codes

| Code | Meaning |
|---|---|
| 200 | Success |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 404 | Not Found |
| 500 | Server Error |


---

# 5. JSON Response

Example:

```json
{
    "id":1,
    "name":"Ritesh"
}
```

---

# 6. Custom Requests Adapters and Hooks

## Requests Adapter

A requests adapter controls how HTTP requests are handled.

It is useful for:

- Retry configuration
- Connection pooling
- SSL settings
- Proxy configuration


---

## Example

```python
import requests
from requests.adapters import HTTPAdapter

session = requests.Session()

adapter = HTTPAdapter()

session.mount(
    "https://",
    adapter
)
```

---

# Request Hooks

## What are Hooks?

Hooks allow custom functions to run during request processing.

---

## Example

```python
import requests


def response_hook(response, *args, **kwargs):
    print(response.status_code)


requests.get(
    "https://example.com",
    hooks={
        "response": response_hook
    }
)
```

---

# Uses of Hooks

- Logging responses
- Monitoring requests
- Debugging
- Validation


---

# Summary

| Topic | Important Point |
|---|---|
| Race Condition | Happens when multiple threads modify shared data together |
| Thread Safety | Protects shared resources from incorrect access |
| HTTP Session | Maintains user state between requests |
| Cookies | Store client-side session information |
| Tokens | Used for secure authentication |
| JWT | Stateless authentication method |
| API Client | Communicates with external services |
| Retry | Handles temporary failures |
| REST API | Standard API design approach |
| HTTP Methods | Define operations on resources |
| Adapter | Customizes HTTP request behavior |
| Hooks | Executes custom logic during requests |

---

# Python Advanced Concepts - Part 3

## Object-Oriented Design, SOLID Principles, and Data Modeling

This README covers advanced Python software design concepts used to build clean, scalable, and maintainable applications.

---

# Topics Covered

1. SOLID Principles in Python
2. Design Patterns in Python
3. Composition vs Inheritance
4. Dataclasses vs NamedTuples vs Pydantic Models

---

# 1. SOLID Principles in Python

## What are SOLID Principles?

SOLID principles are five object-oriented design principles that help developers write:

- Clean code
- Maintainable code
- Flexible applications
- Testable software

SOLID stands for:

```
S - Single Responsibility Principle
O - Open/Closed Principle
L - Liskov Substitution Principle
I - Interface Segregation Principle
D - Dependency Inversion Principle
```

---

# 1. Single Responsibility Principle (SRP)

## Definition

A class should have only one responsibility.

A class should do only one type of work.

---

## Bad Example

```python
class User:

    def save_user(self):
        print("Saving user")

    def send_email(self):
        print("Sending email")
```

Problem:

The class is handling two responsibilities:

- Saving user data
- Sending emails

---

## Better Example

```python
class User:

    def save_user(self):
        print("Saving user")


class EmailService:

    def send_email(self):
        print("Sending email")
```

Now each class has one responsibility.

---

# 2. Open/Closed Principle (OCP)

## Definition

Software should be:

- Open for extension
- Closed for modification

New features should be added without changing existing code.

---

Example:

```python
class Payment:

    def pay(self):
        pass


class CreditCard(Payment):

    def pay(self):
        print("Credit Card Payment")


class UPI(Payment):

    def pay(self):
        print("UPI Payment")
```

New payment methods can be added easily.

---

# 3. Liskov Substitution Principle (LSP)

## Definition

Child classes should be replaceable with their parent classes without breaking the program.

---

Example:

```python
class Bird:

    def fly(self):
        pass


class Sparrow(Bird):

    def fly(self):
        print("Flying")
```

Sparrow can replace Bird.

---

# 4. Interface Segregation Principle (ISP)

## Definition

A class should not be forced to implement methods it does not use.

---

Bad Example:

```python
class Animal:

    def fly(self):
        pass

    def swim(self):
        pass
```

A fish does not need the fly method.

---

Better Design:

```python
class FlyingAnimal:

    def fly(self):
        pass


class SwimmingAnimal:

    def swim(self):
        pass
```

---

# 5. Dependency Inversion Principle (DIP)

## Definition

High-level modules should not depend directly on low-level modules.

They should depend on abstractions.

---

Example:

Bad:

```
Application → MySQL Database
```

Better:

```
Application

     ↓

Database Interface

     ↓

MySQL / PostgreSQL
```

---

# Benefits of SOLID Principles

- Better code organization
- Easy maintenance
- Less dependency
- Easier testing
- Scalable applications


---

# 2. Design Patterns in Python

## What are Design Patterns?

Design patterns are reusable solutions for commonly occurring software problems.

They provide standard ways to design applications.

---

# Types of Design Patterns

```
1. Creational Patterns
2. Structural Patterns
3. Behavioral Patterns
```

---

# 1. Singleton Pattern

## Definition

Singleton ensures that only one object of a class exists.

---

Example:

```python
class Singleton:

    instance = None

    def __new__(cls):

        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance
```

---

Uses:

- Database connection
- Configuration manager
- Logger


---

# 2. Factory Pattern

## Definition

Factory pattern creates objects without exposing the creation logic.

---

Example:

```python
class Dog:

    def speak(self):
        return "Bark"


class Cat:

    def speak(self):
        return "Meow"


class AnimalFactory:

    def create(animal):

        if animal == "dog":
            return Dog()

        return Cat()
```

---

Uses:

- Object creation
- Framework development

---

# 3. Observer Pattern

## Definition

Observer pattern allows one object to notify multiple objects when a change occurs.

---

Example:

```
YouTube Channel

        |

        |

 Subscribers

        |

 Notification
```

---

Uses:

- Event systems
- Notifications
- GUI applications

---

# 4. Strategy Pattern

## Definition

Strategy pattern allows selecting different algorithms during runtime.

---

Example:

```python
class Payment:

    def pay(self):
        pass


class UPI(Payment):

    def pay(self):
        print("UPI Payment")


class Card(Payment):

    def pay(self):
        print("Card Payment")
```

---

Uses:

- Payment systems
- Sorting algorithms
- Authentication methods


---

# Benefits of Design Patterns

- Reusable solutions
- Better architecture
- Cleaner code
- Industry-standard practices


---

# 3. Composition vs Inheritance

# Inheritance

## Definition

Inheritance allows one class to use properties and methods of another class.

Relationship:

```
IS-A Relationship
```

Example:

```
Dog IS-A Animal
```

---

Example:

```python
class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):

    def bark(self):
        print("Barking")


dog = Dog()

dog.eat()
dog.bark()
```

---

## Advantages

- Code reuse
- Easy extension
- Simple hierarchy

---

## Problems

- Tight coupling
- Difficult changes
- Complex hierarchy


---

# Composition

## Definition

Composition means creating a class using objects of another class.

Relationship:

```
HAS-A Relationship
```

Example:

```
Car HAS-A Engine
```

---

Example:

```python
class Engine:

    def start(self):
        print("Engine Started")


class Car:

    def __init__(self):
        self.engine = Engine()


car = Car()

car.engine.start()
```

---

## Advantages

- Loose coupling
- Flexible design
- Easy testing


---

# Inheritance vs Composition

| Inheritance | Composition |
|---|---|
| IS-A relationship | HAS-A relationship |
| Tight coupling | Loose coupling |
| Parent-child structure | Object combination |
| Less flexible | More flexible |

---

# 4. Dataclasses vs NamedTuple vs Pydantic Models

These are used for storing structured data in Python.

---

# Dataclasses

## Definition

Dataclasses are classes designed mainly for storing data.

Introduced in Python 3.7.

---

Example:

```python
from dataclasses import dataclass


@dataclass
class Student:

    name: str
    age: int


student = Student("Ritesh",21)

print(student)
```

Output:

```
Student(name='Ritesh', age=21)
```

---

Features:

- Automatic __init__()
- Automatic __repr__()
- Easy comparison
- Less boilerplate


---

# NamedTuple

## Definition

NamedTuple is an immutable tuple with named fields.

---

Example:

```python
from collections import namedtuple


Student = namedtuple(
    "Student",
    ["name","age"]
)


student = Student(
    "Ritesh",
    21
)

print(student.name)
```

---

Features:

- Immutable
- Memory efficient
- Lightweight


---

# Pydantic Models

## Definition

Pydantic is used for:

- Data validation
- Data parsing
- API models

Commonly used with FastAPI.

---

Example:

```python
from pydantic import BaseModel


class Student(BaseModel):

    name: str
    age: int


student = Student(
    name="Ritesh",
    age=21
)
```

---

## Validation Example

```python
Student(
    name="Ritesh",
    age="abc"
)
```

Pydantic raises an error because age must be an integer.

---

# Comparison Table

| Feature | Dataclass | NamedTuple | Pydantic |
|---|---|---|---|
| Mutable | Yes | No | Yes |
| Validation | No | No | Yes |
| Performance | Fast | Very Fast | Medium |
| Main Use | Data Objects | Fixed Data | API Models |
| Type Checking | Basic | Basic | Strong |

---

# When To Use?

## Dataclass

Use for:

- Employee records
- Product details
- Configuration objects


## NamedTuple

Use for:

- Coordinates
- Constants
- Fixed values


## Pydantic

Use for:

- REST APIs
- JSON validation
- User input validation


---

# Final Summary

| Topic | Key Point |
|---|---|
| SOLID | Principles for clean object-oriented design |
| SRP | One class should have one responsibility |
| OCP | Extend functionality without modifying code |
| LSP | Child class should replace parent class |
| ISP | Avoid unnecessary methods |
| DIP | Depend on abstractions |
| Design Patterns | Reusable software solutions |
| Inheritance | IS-A relationship |
| Composition | HAS-A relationship |
| Dataclass | Simple data storage |
| NamedTuple | Immutable lightweight structure |
| Pydantic | Data validation model |

---

# Python Advanced Concepts - Part 4

# Testing, Performance, Security, and Code Quality

This README covers advanced Python concepts related to testing, optimization, security, dependency management, and maintaining high-quality Python applications.

---

# Topics Covered

1. Unit Testing Strategies
2. Mocking External Dependencies
3. Property-Based Testing
4. Static Analysis and Type Checking
5. Profiling Python Code
6. Common Performance Pitfalls
7. Caching Strategies
8. JSON Parsing and Validation Pitfalls
9. Serialization Formats Compared
10. Virtual Environments and Dependency Management
11. Secure Credential Handling
12. Logging Best Practices
13. Test Driven Development (TDD)

---

# 1. Unit Testing Strategies

## What is Unit Testing?

Unit testing is the process of testing individual parts of a program independently.

A unit can be:

- Function
- Method
- Class

The main goal is to verify that each component works correctly.

---

## Example

Function:

```python
def add(a, b):
    return a + b
```

Test:

```python
def test_add():

    result = add(2, 3)

    assert result == 5
```

---

# Testing Frameworks in Python

Common testing frameworks:

- unittest
- pytest

---

## pytest Example

Install:

```bash
pip install pytest
```

Test file:

```
test_math.py
```

Example:

```python
def multiply(a, b):
    return a * b


def test_multiply():

    assert multiply(2, 3) == 6
```

Run test:

```bash
pytest
```

---

# Types of Testing

## Unit Testing

Tests individual functions or classes.

Example:

```
Function → Test
```

---

## Integration Testing

Tests multiple components together.

Example:

```
Application + Database
```

---

## End-to-End Testing

Tests the complete user workflow.

Example:

```
Login → Product Selection → Payment
```

---

# Benefits

- Finds bugs early
- Improves reliability
- Makes code changes safer

---

# 2. Mocking External Dependencies

## What is Mocking?

Mocking replaces real external services with fake objects during testing.

External dependencies include:

- APIs
- Databases
- File systems
- Email services

---

## Why Use Mocking?

Example:

Testing a payment system.

Instead of calling a real payment API:

```
Application

     ↓

Real Payment API
```

Use:

```
Application

     ↓

Fake Payment API
```

---

# Mock Example

```python
from unittest.mock import Mock


payment = Mock()

payment.process()

payment.process.assert_called_once()
```

---

# Mocking API Calls

```python
from unittest.mock import patch


@patch("requests.get")
def test_api(mock_get):

    mock_get.return_value.status_code = 200
```

---

# Advantages

- Faster tests
- No dependency on external systems
- Predictable results

---

# 3. Property-Based Testing

## What is Property-Based Testing?

Property-based testing checks whether a rule remains true for many automatically generated inputs.

Instead of testing only fixed values, it tests many possible cases.

---

Example:

Normal testing:

```python
add(2,3) == 5
```

Property testing:

```
For all numbers:

a + b = b + a
```

---

# Hypothesis Library

Install:

```bash
pip install hypothesis
```

Example:

```python
from hypothesis import given
from hypothesis.strategies import integers


@given(
    integers(),
    integers()
)

def test_addition(a, b):

    assert a+b == b+a
```

---

# Benefits

- Finds hidden bugs
- Tests thousands of cases automatically
- Useful for complex logic

---

# 4. Static Analysis and Type Checking

## Static Analysis

Static analysis checks code without executing it.

It detects:

- Programming mistakes
- Security issues
- Code style problems

---

# Popular Tools

- pylint
- flake8
- ruff

---

Example:

```python
x = "10"

print(x + 5)
```

Static analyzers can detect type problems.

---

# Type Checking

Type checking verifies that variables contain expected data types.

Example:

```python
def add(
    a: int,
    b: int
) -> int:

    return a + b
```

---

# Tool

```
mypy
```

Run:

```bash
mypy file.py
```

---

# Benefits

- Reduces errors
- Improves readability
- Helps large projects

---

# 5. Profiling Python Code

## What is Profiling?

Profiling measures the performance of a Python program.

It helps identify:

- Slow functions
- CPU usage
- Memory problems

---

# Profiling Tools

## cProfile

Built-in Python profiler.

Example:

```bash
python -m cProfile program.py
```

---

## timeit

Measures execution time.

Example:

```python
import timeit


print(
    timeit.timeit(
        "sum(range(100))",
        number=1000
    )
)
```

---

# Optimization Process

```
Find Problem

↓

Measure Performance

↓

Optimize Code

↓

Measure Again
```

---

# 6. Common Performance Pitfalls

## 1. Unnecessary Loops

Bad:

```python
result = []

for i in range(100000):
    result.append(i)
```

Better:

```python
result = [
    i for i in range(100000)
]
```

---

## 2. Repeated Calculations

Bad:

```python
for user in users:
    calculate()
```

Better:

Store calculated values and reuse them.

---

## 3. Wrong Data Structures

List search:

```
O(n)
```

Set search:

```
O(1)
```

---

## 4. Too Many Database Requests

Bad:

```
1000 users

↓

1000 queries
```

Better:

```
One optimized query
```

---

# 7. Caching Strategies

## What is Caching?

Caching stores frequently used data temporarily to improve speed.

---

Without Cache:

```
Request

↓

Database

↓

Response
```

With Cache:

```
Request

↓

Cache

↓

Fast Response
```

---

# Types of Cache

## 1. In-Memory Cache

Stores data in RAM.

Example:

```python
cache = {}
```

---

## 2. LRU Cache

Least Recently Used cache.

Example:

```python
from functools import lru_cache


@lru_cache
def square(n):

    return n*n
```

---

## 3. Distributed Cache

Used in large applications.

Examples:

- Redis
- Memcached

---

# Benefits

- Faster response
- Less database load
- Better scalability

---

# 8. JSON Parsing and Validation Pitfalls

## What is JSON?

JSON is a data exchange format commonly used in APIs.

Example:

```json
{
    "name":"Ritesh",
    "age":21
}
```

---

# Common Problems

## Missing Fields

```json
{
"name":"Ritesh"
}
```

Age is missing.

---

## Wrong Data Types

```json
{
"age":"twenty"
}
```

Expected:

```
integer
```

---

## Invalid JSON

Wrong:

```json
{
"name":"Ritesh",
}
```

Extra comma creates an error.

---

# Validation Tools

- Pydantic
- Marshmallow
- JSON Schema

---

# 9. Serialization Formats Compared

## What is Serialization?

Serialization converts objects into a format that can be stored or transferred.

Example:

```
Python Object

↓

JSON

↓

Network
```

---

# Common Formats

| Format | Features |
|---|---|
| JSON | Human readable and widely used |
| Pickle | Python object serialization |
| XML | Structured document format |
| MessagePack | Faster binary format |
| Protocol Buffers | High performance format |

---

# JSON Example

```python
import json


data = {
    "name":"Ritesh"
}


json_data = json.dumps(data)
```

---

# Pickle Example

```python
import pickle


pickle_data = pickle.dumps(data)
```

---

# 10. Virtual Environments and Dependency Management

## What is Virtual Environment?

A virtual environment creates an isolated Python environment for a project.

---

Without Virtual Environment:

```
Project A

Package Conflict

Project B
```

---

With Virtual Environment:

```
Project A
   |
 Own Packages


Project B
   |
 Own Packages
```

---

# Creating Environment

```bash
python -m venv env
```

---

Activate:

Windows:

```bash
env\Scripts\activate
```

Linux:

```bash
source env/bin/activate
```

---

# Dependency Management

Tools:

- pip
- requirements.txt
- Poetry

Create requirements:

```bash
pip freeze > requirements.txt
```

---

# 11. Secure Credential Handling

## Never Store Passwords Directly

Bad:

```python
password = "123456"
```

---

Better:

Use environment variables.

```python
import os


password = os.getenv("PASSWORD")
```

---

# Best Practices

- Use environment variables
- Use secret managers
- Never upload secrets to GitHub
- Rotate credentials regularly

---

# 12. Logging Best Practices

## What is Logging?

Logging records application events.

Examples:

- Errors
- Warnings
- Information

---

# Python Logging Example

```python
import logging


logging.basicConfig(
    level=logging.INFO
)


logging.info(
    "Application Started"
)
```

---

# Logging Levels

| Level | Purpose |
|---|---|
| DEBUG | Detailed information |
| INFO | Normal events |
| WARNING | Possible issue |
| ERROR | Error occurred |
| CRITICAL | Serious failure |

---

# Best Practices

- Avoid excessive print statements
- Add timestamps
- Store logs properly
- Never log passwords

---

# 13. Test Driven Development (TDD)

## What is TDD?

Test Driven Development is a method where developers write tests before writing the actual code.

---

# TDD Cycle

```
RED

Write failing test

↓

GREEN

Write code to pass test

↓

REFACTOR

Improve code
```

---

Example:

## Step 1: Write Test

```python
def test_add():

    assert add(2,3) == 5
```

---

## Step 2: Write Code

```python
def add(a,b):

    return a+b
```

---

# Benefits of TDD

- Better code quality
- Fewer bugs
- Easier maintenance
- Confidence during changes

---

# Final Summary

| Topic | Key Point |
|---|---|
| Unit Testing | Tests individual components |
| Mocking | Replaces external systems during testing |
| Property Testing | Tests multiple generated inputs |
| Static Analysis | Finds issues without execution |
| Type Checking | Verifies correct data types |
| Profiling | Measures performance |
| Caching | Stores frequently used data |
| JSON Validation | Prevents invalid data handling |
| Serialization | Converts objects into transferable formats |
| Virtual Environment | Creates isolated project environments |
| Credential Handling | Protects sensitive information |
| Logging | Tracks application activities |
| TDD | Tests are written before code |

---

