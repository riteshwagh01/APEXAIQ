# Data Types and Operators in JavaScript

## Introduction

JavaScript is a **dynamically typed programming language**, which means you do not need to specify the data type of a variable while declaring it. The JavaScript engine automatically determines the type based on the assigned value.

Data types define the kind of value a variable can store, while operators are special symbols used to perform operations such as mathematical calculations, comparisons, and logical decisions.

Understanding data types and operators is essential because they are used in almost every JavaScript program.

---

# 1. Data Types in JavaScript

JavaScript data types are divided into two categories:

## 1. Primitive Data Types

Primitive data types store a single value.

- String
- Number
- Boolean
- Undefined
- Null
- BigInt
- Symbol

---

## 2. Non-Primitive (Reference) Data Types

Reference data types store collections of values.

- Object
- Array
- Function

---

# Primitive Data Types

## 1. String

### Definition

A **String** is a sequence of characters enclosed in single quotes (`' '`), double quotes (`" "`), or backticks (`` ` ` ``).

---

### Syntax

```javascript
let name = "Ritesh";
```

---

### Example

```javascript
let name = "Ritesh";

console.log(name);
console.log(typeof name);
```

---

### Output

```text
Ritesh
string
```

---

### Explanation

- The variable `name` stores text.
- `typeof` returns the data type of the variable.
- Since the value is text, the output is **string**.

---

## 2. Number

### Definition

The **Number** data type stores both integer and decimal values.

---

### Example

```javascript
let age = 21;
let percentage = 85.75;

console.log(age);
console.log(percentage);

console.log(typeof age);
```

---

### Output

```text
21
85.75
number
```

---

### Explanation

JavaScript stores both integers and decimal numbers using the **Number** data type.

---

## 3. Boolean

### Definition

A **Boolean** stores only two values:

- `true`
- `false`

It is mainly used for decision-making.

---

### Example

```javascript
let isPassed = true;

console.log(isPassed);

console.log(typeof isPassed);
```

---

### Output

```text
true
boolean
```

---

### Explanation

The variable `isPassed` contains either `true` or `false`, making it a Boolean value.

---

## 4. Undefined

### Definition

A variable that has been declared but not assigned any value has the data type **undefined**.

---

### Example

```javascript
let city;

console.log(city);

console.log(typeof city);
```

---

### Output

```text
undefined
undefined
```

---

### Explanation

The variable exists but no value has been assigned yet.

---

## 5. Null

### Definition

`null` represents an intentional absence of a value.

---

### Example

```javascript
let phone = null;

console.log(phone);

console.log(typeof phone);
```

---

### Output

```text
null
object
```

---

### Explanation

Although `typeof null` returns `"object"` due to a historical JavaScript behavior, `null` is considered a primitive data type.

---

## 6. BigInt

### Definition

**BigInt** is used to store integers larger than the maximum safe limit of the Number type.

---

### Example

```javascript
let largeNumber = 123456789012345678901234567890n;

console.log(largeNumber);

console.log(typeof largeNumber);
```

---

### Output

```text
123456789012345678901234567890n

bigint
```

---

### Explanation

The letter `n` at the end indicates that the value is a **BigInt**.

---

## 7. Symbol

### Definition

A **Symbol** creates a unique identifier.

---

### Example

```javascript
let id = Symbol("101");

console.log(id);

console.log(typeof id);
```

---

### Output

```text
Symbol(101)

symbol
```

---

### Explanation

Even if two Symbols have the same description, they are always unique.

---

# Non-Primitive Data Types

## 1. Object

### Definition

An object stores data as **key-value pairs**.

---

### Example

```javascript
let student = {
    name: "Ritesh",
    age: 21
};

console.log(student);

console.log(typeof student);
```

---

### Output

```text
{ name: 'Ritesh', age: 21 }

object
```

---

### Explanation

Objects are used to represent real-world entities with multiple related properties.

---

## 2. Array

### Definition

An array stores multiple values in a single variable.

---

### Example

```javascript
let colors = ["Red", "Blue", "Green"];

console.log(colors);

console.log(typeof colors);
```

---

### Output

```text
["Red","Blue","Green"]

object
```

---

### Explanation

Arrays are special types of objects designed to store ordered collections of data.

---

## 3. Function

### Definition

A function is a reusable block of code.

---

### Example

```javascript
function greet() {
    console.log("Welcome");
}

greet();

console.log(typeof greet);
```

---

### Output

```text
Welcome

function
```

---

### Explanation

Functions execute code whenever they are called and help avoid repetition.

---

# Operators in JavaScript

Operators perform operations on variables and values.

The main types of operators are:

- Arithmetic Operators
- Assignment Operators
- Comparison Operators
- Logical Operators
- Increment and Decrement Operators
- Ternary Operator

---

# 1. Arithmetic Operators

These operators perform mathematical calculations.

| Operator | Meaning |
|----------|----------|
| + | Addition |
| - | Subtraction |
| * | Multiplication |
| / | Division |
| % | Modulus (Remainder) |
| ** | Exponentiation |

---

### Example

```javascript
let a = 20;
let b = 10;

console.log(a + b);
console.log(a - b);
console.log(a * b);
console.log(a / b);
console.log(a % b);
console.log(a ** 2);
```

---

### Output

```text
30
10
200
2
0
400
```

---

### Explanation

Each operator performs its corresponding mathematical operation.

---

# 2. Assignment Operators

These operators assign values to variables.

| Operator | Example |
|----------|----------|
| = | x = 10 |
| += | x += 5 |
| -= | x -= 2 |
| *= | x *= 3 |
| /= | x /= 2 |

---

### Example

```javascript
let x = 10;

x += 5;
console.log(x);

x *= 2;
console.log(x);

x -= 10;
console.log(x);
```

---

### Output

```text
15
30
20
```

---

### Explanation

Assignment operators combine assignment with arithmetic operations, making code shorter.

---

# 3. Comparison Operators

These compare two values and return either `true` or `false`.

| Operator | Meaning |
|----------|----------|
| == | Equal |
| === | Strict Equal |
| != | Not Equal |
| !== | Strict Not Equal |
| > | Greater Than |
| < | Less Than |
| >= | Greater Than or Equal |
| <= | Less Than or Equal |

---

### Example

```javascript
let a = 20;
let b = 10;

console.log(a > b);
console.log(a < b);
console.log(a == b);
console.log(a != b);
console.log(a === 20);
```

---

### Output

```text
true
false
false
true
true
```

---

### Explanation

Comparison operators are mainly used in conditions such as `if` statements and loops.

---

# 4. Logical Operators

Logical operators combine or invert Boolean values.

| Operator | Meaning |
|----------|----------|
| && | AND |
| \|\| | OR |
| ! | NOT |

---

### Example

```javascript
let age = 22;
let hasLicense = true;

console.log(age >= 18 && hasLicense);

console.log(age < 18 || hasLicense);

console.log(!hasLicense);
```

---

### Output

```text
true
true
false
```

---

### Explanation

- `&&` returns `true` only if both conditions are true.
- `||` returns `true` if at least one condition is true.
- `!` reverses the Boolean value.

---

# 5. Increment and Decrement Operators

These increase or decrease a variable's value by one.

---

### Example

```javascript
let count = 5;

count++;
console.log(count);

count--;
console.log(count);
```

---

### Output

```text
6
5
```

---

### Explanation

- `++` adds one to the variable.
- `--` subtracts one from the variable.

---

# 6. Ternary Operator

## Definition

The ternary operator is a shorthand way of writing an `if...else` statement.

---

### Syntax

```javascript
condition ? value1 : value2;
```

---

### Example

```javascript
let age = 20;

let result = age >= 18 ? "Eligible to Vote" : "Not Eligible";

console.log(result);
```

---

### Output

```text
Eligible to Vote
```

---

### Explanation

Since the condition `age >= 18` is true, the first value is returned.

---

# Real-Life Example

```javascript
let studentName = "Ritesh";
let marks = 82;

let result = marks >= 35 ? "Pass" : "Fail";

console.log("Student:", studentName);
console.log("Marks:", marks);
console.log("Result:", result);
```

---

### Output

```text
Student: Ritesh
Marks: 82
Result: Pass
```

---

### Explanation

- `studentName` is a **String**.
- `marks` is a **Number**.
- The ternary operator checks whether the student has passed.
- Since the marks are greater than or equal to **35**, the result displayed is **Pass**.

---

# Applications

- Store different types of information such as text, numbers, and Boolean values.
- Perform mathematical calculations.
- Compare values for decision-making.
- Build conditions in loops and `if` statements.
- Develop interactive web applications.

---

# Summary

| Topic | Description |
|--------|-------------|
| Primitive Data Types | String, Number, Boolean, Undefined, Null, BigInt, Symbol |
| Non-Primitive Data Types | Object, Array, Function |
| Arithmetic Operators | Perform mathematical calculations |
| Assignment Operators | Assign and update variable values |
| Comparison Operators | Compare values and return Boolean results |
| Logical Operators | Combine or invert conditions |
| Increment/Decrement | Increase or decrease values by one |
| Ternary Operator | Short form of `if...else` |

---

# Conclusion

Data types and operators are the foundation of JavaScript programming. Data types define what kind of values variables can store, while operators allow you to manipulate, compare, and evaluate those values. Understanding these concepts is essential for writing efficient, readable, and interactive JavaScript applications.