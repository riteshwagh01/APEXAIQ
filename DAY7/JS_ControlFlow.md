# Control Flow Statements

## Introduction

Control Flow Statements are one of the most important concepts in JavaScript. By default, JavaScript executes statements one after another in the order they are written. However, in real-world applications, we often need to make decisions, execute different blocks of code based on conditions, or repeat a set of instructions multiple times. This is where control flow statements become useful.

Control flow statements allow programmers to control the sequence of execution of a program. They make programs interactive, dynamic, and capable of handling different situations efficiently.

For example, when a user logs into a website, the program checks whether the username and password are correct before allowing access. Similarly, loops are used to display lists of products, process arrays, and repeat operations without writing the same code multiple times.

---

# Types of Control Flow Statements

JavaScript provides the following control flow statements:

- if Statement
- if...else Statement
- else if Ladder
- switch Statement
- for Loop
- while Loop
- do...while Loop
- for...in Loop
- for...of Loop
- break Statement
- continue Statement

---

# 3.1 `if` Statement

## Definition

The `if` statement is the simplest decision-making statement in JavaScript. It executes a block of code only when a specified condition evaluates to **true**. If the condition is **false**, the code inside the `if` block is skipped.

---

## Syntax

```javascript
if (condition) {

    // Statements to execute if condition is true

}
```

---

## Flow Diagram

```text
        Condition
            |
     ----------------
     |              |
   True          False
     |              |
 Execute Code    Skip Code
```

---

## Practical Example 1

```javascript
let age = 20;

if (age >= 18) {

    console.log("You are eligible to vote.");

}
```

---

## Output

```text
You are eligible to vote.
```

---

## Explanation

- A variable named `age` stores the value `20`.
- The condition `age >= 18` is checked.
- Since `20` is greater than or equal to `18`, the condition becomes **true**.
- Therefore, the statement inside the `if` block executes.

---

## Practical Example 2

```javascript
let temperature = 35;

if (temperature > 30) {

    console.log("It is a hot day.");

}
```

---

## Output

```text
It is a hot day.
```

---

## Applications

- Login validation
- Checking voting eligibility
- Checking age restrictions
- Verifying passwords
- Exam eligibility

---

## Advantages

- Simple to understand.
- Executes code only when required.
- Reduces unnecessary execution.

---

# 3.2 `if...else` Statement

## Definition

The `if...else` statement allows the program to execute one block of code when a condition is **true** and another block when the condition is **false**.

It is useful when there are only two possible outcomes.

---

## Syntax

```javascript
if (condition) {

    // True block

}
else {

    // False block

}
```

---

## Flow Diagram

```text
         Condition
             |
      -----------------
      |               |
    True           False
      |               |
 Execute IF      Execute ELSE
```

---

## Practical Example

```javascript
let marks = 30;

if (marks >= 35) {

    console.log("Pass");

}
else {

    console.log("Fail");

}
```

---

## Output

```text
Fail
```

---

## Explanation

- The variable `marks` contains the value `30`.
- The condition `marks >= 35` is checked.
- Since `30` is less than `35`, the condition becomes **false**.
- Therefore, the program executes the `else` block and displays **Fail**.

---

## Another Example

```javascript
let password = "admin123";

if (password == "admin123") {

    console.log("Login Successful");

}
else {

    console.log("Invalid Password");

}
```

---

## Output

```text
Login Successful
```

---

## Applications

- Login systems
- ATM PIN verification
- Pass or fail systems
- Payment success or failure

---

## Advantages

- Makes decision-making easier.
- Handles both true and false conditions.
- Improves program readability.

---

# 3.3 `else if` Ladder

## Definition

The `else if` ladder is used when there are multiple conditions to check. JavaScript evaluates each condition from top to bottom. As soon as one condition becomes **true**, the corresponding block executes and the remaining conditions are skipped.

---

## Syntax

```javascript
if (condition1) {

}
else if (condition2) {

}
else if (condition3) {

}
else {

}
```

---

## Flow Diagram

```text
Condition 1?
   |
True --> Execute Block 1
   |
False
   |
Condition 2?
   |
True --> Execute Block 2
   |
False
   |
Condition 3?
   |
True --> Execute Block 3
   |
False
   |
Execute Else Block
```

---

## Practical Example

```javascript
let marks = 88;

if (marks >= 90) {

    console.log("Grade A");

}
else if (marks >= 75) {

    console.log("Grade B");

}
else if (marks >= 50) {

    console.log("Grade C");

}
else {

    console.log("Fail");

}
```

---

## Output

```text
Grade B
```

---

## Explanation

- The first condition checks whether marks are greater than or equal to `90`.
- Since `88` is not greater than or equal to `90`, the first condition is false.
- The second condition checks whether marks are greater than or equal to `75`.
- Since `88` satisfies this condition, the program prints **Grade B**.
- The remaining conditions are ignored.

---

## Applications

- Student grading systems
- Employee salary classification
- Income tax calculation
- Product discounts

---

## Advantages

- Supports multiple conditions.
- Easy to organize decision-making.
- Improves readability compared to multiple `if` statements.

---

# 3.4 `switch` Statement

## Definition

The `switch` statement is used to select one block of code from multiple options. It compares an expression with different `case` values. When a matching case is found, the corresponding block executes.

---

## Syntax

```javascript
switch (expression) {

    case value1:
        // code
        break;

    case value2:
        // code
        break;

    default:
        // code

}
```

---

## Flow Diagram

```text
          Expression
               |
     ---------------------
     |   |   |   |      |
   Case1 Case2 Case3 Default
```

---

## Practical Example

```javascript
let day = 3;

switch (day) {

    case 1:
        console.log("Monday");
        break;

    case 2:
        console.log("Tuesday");
        break;

    case 3:
        console.log("Wednesday");
        break;

    case 4:
        console.log("Thursday");
        break;

    default:
        console.log("Invalid Day");

}
```

---

## Output

```text
Wednesday
```

---

## Explanation

- The value of `day` is `3`.
- JavaScript compares it with each case.
- It matches `case 3`.
- The statement `console.log("Wednesday")` executes.
- The `break` statement stops further execution.

---

## Applications

- Menu-driven programs
- Calculator operations
- Selecting weekdays
- Language selection

---

## Advantages

- Cleaner than multiple `else if` statements.
- Easier to read.
- Faster for multiple fixed conditions.

---

# 3.5 `for` Loop

## Definition

The `for` loop is used when the number of iterations is known in advance. It repeatedly executes a block of code until a specified condition becomes false.

---

## Syntax

```javascript
for (initialization; condition; increment/decrement) {

    // code

}
```

---

## Working of `for` Loop

1. Initialization executes once.
2. The condition is checked.
3. If the condition is true, the loop body executes.
4. The increment/decrement statement updates the variable.
5. Steps 2–4 repeat until the condition becomes false.

---

## Practical Example

```javascript
for (let i = 1; i <= 5; i++) {

    console.log(i);

}
```

---

## Output

```text
1
2
3
4
5
```

---

## Explanation

- `i` starts from `1`.
- The condition `i <= 5` is checked.
- After each iteration, `i` increases by `1`.
- When `i` becomes `6`, the condition becomes false and the loop terminates.

---

## Applications

- Printing tables
- Displaying lists
- Processing arrays
- Repeating tasks

---

# 3.6 `while` Loop

## Definition

The `while` loop repeatedly executes a block of code as long as the specified condition remains true. It is useful when the number of iterations is not known in advance.

---

## Syntax

```javascript
while (condition) {

    // code

}
```

---

## Practical Example

```javascript
let i = 1;

while (i <= 5) {

    console.log(i);

    i++;

}
```

---

## Output

```text
1
2
3
4
5
```

---

## Explanation

- The variable `i` starts with the value `1`.
- The condition `i <= 5` is checked before each iteration.
- After printing the value of `i`, it is incremented by `1`.
- The loop continues until `i` becomes `6`, at which point the condition becomes false and the loop stops.

---

# 3.7 `do...while` Loop

## Definition

The `do...while` loop is similar to the `while` loop, but it guarantees that the loop body executes at least once, even if the condition is false.

---

## Syntax

```javascript
do {

    // code

} while (condition);
```

---

## Practical Example

```javascript
let i = 1;

do {

    console.log(i);

    i++;

} while (i <= 5);
```

---

## Output

```text
1
2
3
4
5
```

---

## Explanation

- The statements inside the `do` block execute first.
- After execution, the condition `i <= 5` is checked.
- If the condition is true, the loop repeats.
- If the condition becomes false, the loop terminates.

---

# Applications of Loops (`for`, `while`, `do...while`)

- Printing multiplication tables.
- Traversing arrays.
- Reading user input.
- Processing files.
- Displaying records from a database.
- Game development.
- Animations.

---

# Summary

| Statement | Purpose | Best Used When |
|-----------|---------|----------------|
| `if` | Execute code when a condition is true | Single condition |
| `if...else` | Execute one of two code blocks | Two possible outcomes |
| `else if` Ladder | Check multiple conditions | Multiple decision paths |
| `switch` | Select one block from many options | Fixed values or menu selection |
| `for` | Repeat code a fixed number of times | Number of iterations is known |
| `while` | Repeat while a condition is true | Number of iterations is unknown |
| `do...while` | Execute code at least once | Code must run before checking the condition |

---

# Conclusion

Control Flow Statements form the foundation of decision-making and repetition in JavaScript. Statements such as `if`, `if...else`, `else if`, and `switch` help programs make decisions based on different conditions, while loops like `for`, `while`, and `do...while` automate repetitive tasks. Mastering these statements enables developers to write efficient, interactive, and maintainable JavaScript applications.




# 3.8 `for...in` Loop

## Definition

The `for...in` loop is used to iterate over the **properties (keys)** of an object. It is mainly used with JavaScript objects because it returns the **property names (keys)** instead of the values.

Although `for...in` can also be used with arrays, it is **not recommended** because it returns array indexes instead of the actual elements.

---

## Syntax

```javascript
for (let key in object) {

    // code

}
```

---

## Flow Diagram

```text
      Object
        |
   Read First Key
        |
   Execute Code
        |
   Next Property?
   Yes ------> Repeat
        |
       No
        |
       End
```

---

## Practical Example 1 (Object)

```javascript
let student = {

    name: "Ritesh",
    age: 21,
    city: "Pune"

};

for (let key in student) {

    console.log(key + " : " + student[key]);

}
```

---

## Output

```text
name : Ritesh
age : 21
city : Pune
```

---

## Explanation

- The object `student` contains three properties.
- The variable `key` stores each property name.
- `student[key]` accesses the corresponding value.
- The loop continues until all properties have been visited.

---

## Practical Example 2 (Array)

```javascript
let fruits = ["Apple", "Mango", "Banana"];

for (let index in fruits) {

    console.log(index + " : " + fruits[index]);

}
```

---

## Output

```text
0 : Apple
1 : Mango
2 : Banana
```

---

## Explanation

- Here, `for...in` returns the indexes (`0`, `1`, `2`) of the array.
- Using the index, the corresponding element is accessed.
- Although it works, `for...of` is preferred for arrays.

---

## Applications

- Traversing object properties.
- Displaying employee information.
- Reading configuration settings.
- Accessing JSON object properties.

---

# 3.9 `for...of` Loop

## Definition

The `for...of` loop is used to iterate over the **values** of iterable objects such as arrays, strings, Sets, and Maps. Unlike `for...in`, it directly returns the **values** instead of indexes or keys.

---

## Syntax

```javascript
for (let value of iterable) {

    // code

}
```

---

## Flow Diagram

```text
      Array/String
           |
    Read First Value
           |
     Execute Code
           |
      Next Value?
      Yes ------> Repeat
           |
          No
           |
          End
```

---

## Practical Example 1 (Array)

```javascript
let fruits = ["Apple", "Mango", "Banana"];

for (let fruit of fruits) {

    console.log(fruit);

}
```

---

## Output

```text
Apple
Mango
Banana
```

---

## Explanation

- Each element of the array is stored in the variable `fruit`.
- The loop directly prints the values.
- No indexes are returned.

---

## Practical Example 2 (String)

```javascript
let name = "Ritesh";

for (let letter of name) {

    console.log(letter);

}
```

---

## Output

```text
R
i
t
e
s
h
```

---

## Explanation

- Strings are iterable objects.
- The loop reads one character at a time.
- Each character is displayed separately.

---

## Applications

- Traversing arrays.
- Reading characters from strings.
- Iterating through Sets.
- Iterating through Maps.

---

# Difference Between `for...in` and `for...of`

| Feature | `for...in` | `for...of` |
|----------|------------|------------|
| Returns | Keys or Indexes | Values |
| Mainly Used For | Objects | Arrays, Strings, Sets, Maps |
| Works with Objects | ✅ Yes | ❌ No (Objects are not directly iterable) |
| Works with Arrays | Yes (Indexes) | Yes (Values) |
| Best Practice | Objects | Arrays and other iterables |

---

# 3.10 `break` Statement

## Definition

The `break` statement is used to immediately terminate a loop or a `switch` statement. Once `break` is executed, control moves to the first statement after the loop or switch.

---

## Syntax

```javascript
break;
```

---

## Practical Example

```javascript
for (let i = 1; i <= 10; i++) {

    if (i == 6) {

        break;

    }

    console.log(i);

}
```

---

## Output

```text
1
2
3
4
5
```

---

## Explanation

- The loop starts printing numbers from `1`.
- When `i` becomes `6`, the `break` statement is executed.
- The loop immediately terminates.
- Numbers `6` to `10` are not printed.

---

## Applications

- Searching for an item in an array.
- Exiting menus.
- Ending infinite loops safely.

---

# 3.11 `continue` Statement

## Definition

The `continue` statement skips the current iteration of a loop and immediately proceeds to the next iteration.

Unlike `break`, it does **not** terminate the loop.

---

## Syntax

```javascript
continue;
```

---

## Practical Example

```javascript
for (let i = 1; i <= 5; i++) {

    if (i == 3) {

        continue;

    }

    console.log(i);

}
```

---

## Output

```text
1
2
4
5
```

---

## Explanation

- The loop starts from `1`.
- When `i` becomes `3`, the `continue` statement skips that iteration.
- The loop continues with `4` and `5`.
- Therefore, `3` is not printed.

---

## Applications

- Skipping invalid records.
- Ignoring unwanted values.
- Processing only required data.

---

# Comparison of All Loops

| Loop | Purpose | Best Used When |
|------|---------|----------------|
| `for` | Repeat code a fixed number of times | Number of iterations is known |
| `while` | Repeat while a condition is true | Number of iterations is unknown |
| `do...while` | Execute at least once | Code must run before checking the condition |
| `for...in` | Iterate over object keys | Working with objects |
| `for...of` | Iterate over iterable values | Working with arrays, strings, Sets, and Maps |

---

# Real-Life Example

The following program displays employee information using `for...in` and prints employee skills using `for...of`.

```javascript
let employee = {

    id: 101,
    name: "Ritesh",
    department: "IT"

};

console.log("Employee Details");

for (let key in employee) {

    console.log(key + " : " + employee[key]);

}

let skills = ["HTML", "CSS", "JavaScript", "React"];

console.log("Employee Skills");

for (let skill of skills) {

    console.log(skill);

}
```

---

## Output

```text
Employee Details

id : 101
name : Ritesh
department : IT

Employee Skills

HTML
CSS
JavaScript
React
```

---

## Explanation

- The `employee` object stores information as key-value pairs.
- The `for...in` loop accesses each property (`id`, `name`, `department`) and prints both the key and its value.
- The `skills` array stores a list of technologies.
- The `for...of` loop directly retrieves each skill from the array and prints it.
- This example demonstrates that `for...in` is best suited for objects, while `for...of` is ideal for arrays and other iterable collections.

---

# Advantages of Control Flow Statements

- Makes programs dynamic and interactive.
- Supports decision-making based on conditions.
- Reduces code duplication using loops.
- Improves code readability and maintainability.
- Helps automate repetitive tasks.
- Enables efficient processing of arrays and objects.

---

# Disadvantages of Control Flow Statements

- Incorrect conditions can lead to logical errors.
- Infinite loops may occur if loop conditions are not updated properly.
- Deeply nested conditions can make code difficult to read and maintain.
- Excessive use of `break` and `continue` may reduce code clarity.

---

# Summary

| Topic | Key Point |
|--------|-----------|
| `for...in` | Iterates over object keys or array indexes |
| `for...of` | Iterates directly over iterable values |
| `break` | Terminates a loop immediately |
| `continue` | Skips the current iteration and continues the loop |
| Control Flow Statements | Help build efficient, dynamic, and maintainable programs |

---

# Conclusion

Control flow statements allow JavaScript programs to make decisions and repeat tasks efficiently. The `for...in` loop is best suited for objects, while the `for...of` loop is ideal for arrays and other iterable collections. The `break` statement is used to terminate loops early, whereas the `continue` statement skips specific iterations without ending the loop. Understanding these concepts helps developers write cleaner, more efficient, and more maintainable JavaScript code.