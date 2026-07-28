# Parallelization using ThreadPoolExecutor

## What is Parallelization?

**Parallelization** is a technique in which **multiple tasks run at the same time** using multiple CPU cores or multiple threads.

Unlike **Concurrency**, where the CPU switches between tasks, **Parallelization** executes multiple tasks simultaneously (depending on hardware and the type of task).

---

# What is ThreadPoolExecutor?

`ThreadPoolExecutor` is a class provided by Python's **`concurrent.futures`** module.

It creates and manages a **pool of worker threads**, allowing multiple tasks to run concurrently without manually creating and managing threads.

Instead of creating threads one by one, `ThreadPoolExecutor` automatically handles them.

---

# Why Use ThreadPoolExecutor?

Without `ThreadPoolExecutor`, we need to:

- Create threads manually.
- Start each thread.
- Wait for each thread to finish.
- Manage multiple threads ourselves.

With `ThreadPoolExecutor`, Python does all of this automatically.

---

# Importing ThreadPoolExecutor

```python
from concurrent.futures import ThreadPoolExecutor
```

---

# How ThreadPoolExecutor Works

Suppose we have three tasks.

Without ThreadPoolExecutor:

```text
Create Thread 1

↓

Start Thread 1

↓

Create Thread 2

↓

Start Thread 2

↓

Create Thread 3

↓

Start Thread 3

↓

Wait for all threads
```

With ThreadPoolExecutor:

```text
Create ThreadPool

↓

Submit Tasks

↓

Executor assigns tasks to threads

↓

Tasks execute

↓

Executor waits for completion
```

Everything is managed automatically.

---

# Basic Syntax

```python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.submit(function_name, argument)
```

---

# Understanding the Syntax

```python
ThreadPoolExecutor(max_workers=3)
```

- Creates a pool containing **3 worker threads**.
- At most **3 tasks** can run simultaneously.

---

```python
executor.submit(function_name, argument)
```

- Submits a task to the thread pool.
- Returns a **Future** object.

A **Future** represents the result of a task that may complete later.

---

# Example 1: Running Multiple Tasks

```python
from concurrent.futures import ThreadPoolExecutor
import time

def task(name):
    print(f"{name} started")
    time.sleep(2)
    print(f"{name} completed")

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.submit(task, "Task 1")
    executor.submit(task, "Task 2")
    executor.submit(task, "Task 3")
```

### Possible Output

```text
Task 1 started
Task 2 started
Task 3 started

Task 2 completed
Task 1 completed
Task 3 completed
```

The completion order may change because tasks run independently.

---

# Step-by-Step Working

### Step 1

```python
with ThreadPoolExecutor(max_workers=3) as executor:
```

Creates a thread pool with **3 worker threads**.

---

### Step 2

```python
executor.submit(task, "Task 1")
```

Assigns **Task 1** to one thread.

---

### Step 3

```python
executor.submit(task, "Task 2")
```

Assigns **Task 2** to another thread.

---

### Step 4

```python
executor.submit(task, "Task 3")
```

Assigns **Task 3** to the remaining thread.

Since three workers are available, all three tasks begin together.

---

# Example 2: Downloading Files

```python
from concurrent.futures import ThreadPoolExecutor
import time

def download(file):
    print(f"Downloading {file}")
    time.sleep(3)
    print(f"{file} downloaded")

files = ["File1", "File2", "File3"]

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(download, files)
```

### Output

```text
Downloading File1
Downloading File2
Downloading File3

File1 downloaded
File2 downloaded
File3 downloaded
```

All downloads start together.

---

# submit() vs map()

## submit()

```python
executor.submit(function, argument)
```

- Submits one task at a time.
- Returns a **Future** object.
- Useful when tasks have different arguments.

---

## map()

```python
executor.map(function, iterable)
```

- Runs the same function for every item in an iterable.
- Simpler when processing a list of inputs.
- Returns results in the same order as the input.

---

# Real-Life Example

Imagine three customers at a bank.

### Without ThreadPoolExecutor

```text
One cashier

↓

Customer 1

↓

Customer 2

↓

Customer 3
```

---

### With ThreadPoolExecutor

```text
Three cashiers

↓

Customer 1 → Cashier 1

Customer 2 → Cashier 2

Customer 3 → Cashier 3
```

All customers are served simultaneously.

---

# When Should We Use ThreadPoolExecutor?

It is best suited for **I/O-bound tasks**, such as:

- Downloading files
- Uploading files
- Calling APIs
- Reading files
- Writing files
- Database queries
- Web scraping

---

# When Should We Avoid It?

`ThreadPoolExecutor` is **not ideal for CPU-intensive tasks**, such as:

- Image processing
- Video encoding
- Machine learning training
- Large mathematical calculations

For CPU-bound tasks, use **`ProcessPoolExecutor`** instead.

---

# Advantages

- Easy to use
- Automatically manages threads
- Cleaner code
- Better performance for I/O-bound tasks
- No manual thread management

---

# Limitations

- Not suitable for CPU-bound work because of Python's **Global Interpreter Lock (GIL)**.
- Too many threads can increase memory usage.
- Debugging concurrent code can be difficult.

---

# Difference Between Threading and ThreadPoolExecutor

| Threading | ThreadPoolExecutor |
|-----------|--------------------|
| Threads are created manually | Threads are managed automatically |
| More code | Less code |
| Manual start and join | Automatic management |
| Better control | Easier to use |
| Suitable for custom thread handling | Suitable for most I/O-bound applications |

---

# Summary

- **Parallelization** means executing multiple tasks at the same time.
- **ThreadPoolExecutor** is a high-level API for managing multiple threads.
- It is available in Python's **`concurrent.futures`** module.
- Use **`submit()`** to run individual tasks.
- Use **`map()`** to run the same function on multiple inputs.
- It is best for **I/O-bound operations** like downloads, uploads, API calls, and file handling.
- For **CPU-bound tasks**, prefer **`ProcessPoolExecutor`**.


# ThreadPoolExecutor Implementation in Python

First import the module:

```python
from concurrent.futures import ThreadPoolExecutor
import time
```

---

# Step 1: Create a Function

Suppose this function downloads a file.

```python
import time

def download(file):
    print(f"Downloading {file}...")
    time.sleep(3)
    print(f"{file} Download Complete")
```

Here,

- `time.sleep(3)` simulates a task that takes 3 seconds.
- In real applications, this could be downloading a file or calling an API.

---

# Step 2: Create ThreadPoolExecutor

```python
with ThreadPoolExecutor(max_workers=3) as executor:
    pass
```

### Explanation

```python
ThreadPoolExecutor(max_workers=3)
```

- Creates a pool of **3 worker threads**.
- Maximum **3 tasks** can run at the same time.

`with` automatically closes the thread pool after all tasks are finished.

---

# Method 1: Using submit()

## Syntax

```python
executor.submit(function_name, argument)
```

Example

```python
from concurrent.futures import ThreadPoolExecutor
import time

def download(file):
    print(f"Downloading {file}")
    time.sleep(3)
    print(f"{file} Downloaded")

with ThreadPoolExecutor(max_workers=3) as executor:

    executor.submit(download, "File1")
    executor.submit(download, "File2")
    executor.submit(download, "File3")
```

### Output (Order may vary)

```text
Downloading File1
Downloading File2
Downloading File3

File2 Downloaded
File1 Downloaded
File3 Downloaded
```

---

# How submit() Works

### Line 1

```python
executor.submit(download, "File1")
```

Thread 1 starts

```text
Thread 1 → download("File1")
```

---

### Line 2

```python
executor.submit(download, "File2")
```

Thread 2 starts

```text
Thread 2 → download("File2")
```

---

### Line 3

```python
executor.submit(download, "File3")
```

Thread 3 starts

```text
Thread 3 → download("File3")
```

Since there are **3 worker threads**, all three tasks start together.

---

# Method 2: Using map()

Suppose you already have a list of files.

```python
files = ["File1", "File2", "File3"]
```

Instead of calling `submit()` three times,

use `map()`.

```python
from concurrent.futures import ThreadPoolExecutor
import time

def download(file):
    print(f"Downloading {file}")
    time.sleep(3)
    print(f"{file} Downloaded")

files = ["File1", "File2", "File3"]

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(download, files)
```

Output

```text
Downloading File1
Downloading File2
Downloading File3

File1 Downloaded
File2 Downloaded
File3 Downloaded
```

---

# submit() vs map()

### submit()

```python
executor.submit(download, "File1")
executor.submit(download, "File2")
executor.submit(download, "File3")
```

Useful when every task is different.

---

### map()

```python
files = ["File1", "File2", "File3"]

executor.map(download, files)
```

Useful when the **same function** has to run on multiple values.

---

# Example: Squares of Numbers

```python
from concurrent.futures import ThreadPoolExecutor

def square(n):
    print(n * n)

numbers = [1, 2, 3, 4, 5]

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(square, numbers)
```

Output

```text
1
4
9
16
25
```

---

# Example: API Calls

```python
from concurrent.futures import ThreadPoolExecutor
import time

def api(user):
    print(f"Fetching data for User {user}")
    time.sleep(2)
    print(f"Completed User {user}")

users = [101, 102, 103, 104]

with ThreadPoolExecutor(max_workers=2) as executor:
    executor.map(api, users)
```

### Working

```text
Thread 1 → User 101

Thread 2 → User 102

↓

After one thread finishes

↓

Thread 1 → User 103

Thread 2 → User 104
```

Only **2 threads** exist because

```python
max_workers=2
```

---

# Meaning of max_workers

```python
ThreadPoolExecutor(max_workers=3)
```

means only **3 threads** are available.

Suppose there are 5 tasks.

```text
Task1
Task2
Task3
Task4
Task5
```

Execution

```text
Thread1 → Task1

Thread2 → Task2

Thread3 → Task3

↓

After Thread1 becomes free

↓

Thread1 → Task4

↓

After Thread2 becomes free

↓

Thread2 → Task5
```

Only 3 tasks run simultaneously.

The remaining tasks wait until a thread becomes free.

---

# Interview Tip

- **`submit()`** → Use for individual tasks. It returns a **Future** object.
- **`map()`** → Use when applying the same function to multiple inputs.
- **`max_workers`** → Specifies the maximum number of worker threads that can run tasks concurrently.