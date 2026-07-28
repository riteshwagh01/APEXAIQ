# Concurrent Programming

## What is Concurrent Programming?

Concurrent programming is a technique in which a program handles **multiple tasks during the same period of time** instead of completing one task completely before starting the next.

In simple words:

> **Concurrency means handling multiple tasks together by switching between them whenever one task is waiting.**

It **does not necessarily mean all tasks are running at the exact same time**.

---

# Normal Programming (Sequential Programming)

Suppose you have three tasks:

- Download a file
- Read another file
- Send an email

In normal programming, the computer performs the tasks one after another.

```text
Download File
      ↓
Read File
      ↓
Send Email
```

If each task takes **5 seconds**, then the total execution time will be:

```text
5 + 5 + 5 = 15 seconds
```

The next task starts **only after** the previous task has finished.

---

# Concurrent Programming

Now suppose downloading a file takes **5 seconds**.

During those 5 seconds, the CPU is mostly waiting for data from the internet.

Instead of remaining idle, the CPU starts working on another task.

```text
Download File A (Waiting...)

        ↓

CPU starts Reading File

        ↓

Reading finishes

        ↓

CPU starts Sending Email

        ↓

Download completes
```

So, multiple tasks are making progress together.

This is called **Concurrency**.

---

# Real-Life Example

Imagine you are cooking.

## Without Concurrency

```text
Start boiling tea

↓

Stand and wait for 5 minutes

↓

Tea is ready

↓

Now start cutting vegetables
```

Here, you waste time while waiting.

---

## With Concurrency

```text
Start boiling tea

↓

While tea is boiling,
cut vegetables

↓

While vegetables cook,
prepare salad

↓

Everything gets completed faster.
```

You are **not doing all three tasks at the exact same second**, but you are **using your waiting time wisely**.

This is exactly how concurrent programming works.

---

# Another Example

Suppose you are downloading three movies.

## Without Concurrency

```text
Movie 1 Download

↓

Movie 2 Download

↓

Movie 3 Download
```

Total Time:

```text
10 + 10 + 10 = 30 minutes
```

---

## With Concurrency

```text
Movie 1 starts

↓

Movie 2 starts

↓

Movie 3 starts

↓

CPU switches between them while waiting for the internet
```

Total execution time becomes approximately:

```text
10 minutes
```

because downloading mainly involves waiting for network responses.

---

# Why Do We Need Concurrency?

Many tasks spend most of their time waiting.

Examples include:

- Internet response
- Reading files
- Database queries
- API requests
- User input

Instead of wasting CPU time during these waiting periods, concurrency allows the CPU to work on another task.

This improves the overall performance and responsiveness of the program.

---

# Important Point

Many beginners think:

> **Concurrency = Multiple tasks running at the same time**

This is **not always true**.

A better definition is:

> **Concurrency means multiple tasks make progress during the same period by switching between them whenever one task is waiting.**

Running multiple tasks **at the exact same time** is called **Parallel Programming**, which is a different concept.

---

# Simple Difference

## Sequential Programming

```text
Task A
   ↓
Task B
   ↓
Task C
```

One task finishes completely before the next one starts.

---

## Concurrent Programming

```text
Task A
   ↓
Task B
   ↓
Task A
   ↓
Task C
   ↓
Task B
```

The CPU continuously switches between tasks whenever one task is waiting.

---

# Where is Concurrent Programming Used?

Concurrent programming is commonly used in:

- Download managers
- Web browsers (multiple tabs)
- Chat applications (WhatsApp, Telegram)
- Web servers
- Online games
- Cloud applications
- File upload and download software

---

# Summary

- Concurrent programming allows multiple tasks to make progress during the same period of time.
- The CPU switches between tasks whenever one task is waiting.
- It improves responsiveness and better utilizes CPU resources.
- Concurrency is especially useful for **I/O-bound operations**, such as network requests, file handling, and API calls.
- Concurrency is **different from parallel programming** because tasks are not necessarily executed at the exact same time.