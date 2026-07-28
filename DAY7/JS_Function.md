# 4. Functions in JavaScript 

## Introduction

A function is a reusable block of code designed to perform a specific task. Instead of writing the same code multiple times, we can place it inside a function and call it whenever needed. Functions make programs modular, organized, reusable, and easier to maintain.

Functions are one of the core concepts of JavaScript and are widely used in web development. For example, when a user clicks a button, submits a form, or logs into a website, JavaScript functions are executed behind the scenes to perform the required operations.

---

# What is a Function?

A function is a named or unnamed block of code that executes only when it is called (invoked). It can accept input values called **parameters**, process them, and optionally **return** a result.

---

# Why Do We Use Functions?

Functions are used because they:

- Reduce code duplication.
- Improve code readability.
- Make programs modular.
- Simplify debugging and maintenance.
- Allow code reuse.
- Increase program efficiency.

---

# Advantages of Functions

- Reusable code.
- Easy to maintain.
- Improves readability.
- Reduces program size.
- Makes debugging easier.
- Supports modular programming.

---

# General Syntax of a Function

```javascript
function functionName(parameters){

    // Statements

    return value;

}
```

---

## Explanation

- `function` → Keyword used to create a function.
- `functionName` → Name of the function.
- `parameters` → Input values received by the function.
- `return` → Sends the result back to the caller (optional).

---

# 4.1 Function Declaration (Normal Function)

## Definition

A **Function Declaration**, also known as a **Normal Function**, is the most common way of creating a function in JavaScript. It is declared using the `function` keyword followed by a function name.

Function declarations are **hoisted**, which means they can be called even before they are defined in the code.

---

## Syntax

```javascript
function functionName(){

    // Code

}
```

---

## Practical Example 1

```javascript
function greet(){

    console.log("Welcome to JavaScript");

}

greet();
```

---

## Output

```text
Welcome to JavaScript
```

---

## Explanation

- A function named `greet()` is created.
- The function contains one `console.log()` statement.
- The function is executed when `greet()` is called.
- The output displayed is **"Welcome to JavaScript"**.

---

## Practical Example 2

```javascript
function displayMessage(){

    console.log("Learning JavaScript Functions");

}

displayMessage();
```

---

## Output

```text
Learning JavaScript Functions
```

---

## Applications

- Greeting messages.
- Displaying information.
- Printing reports.
- Executing repeated tasks.

---

# 4.2 Function with Parameters

## Definition

A **parameter** is a variable declared in the function definition that receives data when the function is called.

Parameters make functions flexible because the same function can work with different input values.

---

## Syntax

```javascript
function functionName(parameter1, parameter2){

    // Statements

}
```

---

## Practical Example

```javascript
function greet(name){

    console.log("Welcome " + name);

}

greet("Ritesh");
greet("Rahul");
greet("Amit");
```

---

## Output

```text
Welcome Ritesh
Welcome Rahul
Welcome Amit
```

---

## Explanation

- The function `greet()` accepts one parameter named `name`.
- Each time the function is called, a different value is passed.
- The parameter stores the received value and displays it.

---

## Another Example

```javascript
function multiply(a, b){

    console.log(a * b);

}

multiply(5,4);
multiply(8,6);
```

---

## Output

```text
20
48
```

---

## Explanation

- The function accepts two parameters.
- During each function call, different values are supplied.
- The multiplication result is printed.

---

## Applications

- Calculator programs.
- Student result systems.
- Banking applications.
- Form processing.

---

# 4.3 Function with Return Value

## Definition

A function can return a value using the **return** keyword. Instead of directly displaying the result, the function sends the value back to the place where it was called.

The returned value can then be stored in a variable, displayed, or used in another calculation.

---

## Syntax

```javascript
function functionName(){

    return value;

}
```

---

## Practical Example

```javascript
function add(a,b){

    return a+b;

}

let result = add(10,20);

console.log(result);
```

---

## Output

```text
30
```

---

## Explanation

- The function receives two numbers.
- It adds them together.
- The `return` statement sends the result back.
- The returned value is stored in the variable `result`.
- Finally, `30` is displayed.

---

## Another Example

```javascript
function square(number){

    return number * number;

}

console.log(square(7));
```

---

## Output

```text
49
```

---

## Explanation

- The function calculates the square of the given number.
- The value is returned to the caller.
- The `console.log()` function prints the returned value.

---

## Applications

- Mathematical calculations.
- Returning database results.
- Returning user details.
- API responses.

---

# 4.4 Function Expression

## Definition

A **Function Expression** is a function assigned to a variable. Unlike function declarations, function expressions are **not hoisted**, meaning they cannot be called before they are defined.

---

## Syntax

```javascript
const variableName = function(){

    // Code

};
```

---

## Practical Example

```javascript
const greet = function(){

    console.log("Hello Everyone");

};

greet();
```

---

## Output

```text
Hello Everyone
```

---

## Explanation

- A function is assigned to the variable `greet`.
- The variable behaves like a function.
- The function is executed using `greet()`.

---

## Another Example

```javascript
const multiply = function(a,b){

    return a*b;

};

console.log(multiply(6,7));
```

---

## Output

```text
42
```

---

## Explanation

- The function accepts two numbers.
- It multiplies them.
- The result is returned and printed.

---

## Applications

- Callback functions.
- Event handling.
- Dynamic programming.

---

# 4.5 Anonymous Function

## Definition

An **Anonymous Function** is a function without a name. It is commonly used as an argument to another function or assigned to a variable.

Anonymous functions are useful when a function is required only once.

---

## Syntax

```javascript
function(){

    // Code

}
```

---

## Practical Example 1

```javascript
setTimeout(function(){

    console.log("This message appears after 2 seconds.");

},2000);
```

---

## Output

```text
This message appears after 2 seconds.

(Displayed after 2 seconds.)
```

---

## Explanation

- `setTimeout()` accepts an anonymous function as its first argument.
- The function has no name.
- After 2 seconds, JavaScript automatically executes the anonymous function and prints the message.

---

## Practical Example 2

```javascript
const welcome = function(){

    console.log("Welcome to JavaScript");

};

welcome();
```

---

## Output

```text
Welcome to JavaScript
```

---

## Explanation

- An anonymous function is assigned to the variable `welcome`.
- The function is executed by calling the variable like a normal function.

---

# Difference Between Function Declaration and Function Expression

| Feature | Function Declaration | Function Expression |
|---------|----------------------|---------------------|
| Name Required | Yes | Usually assigned to a variable |
| Hoisting | Yes | No |
| Can Be Called Before Declaration | Yes | No |
| Syntax | `function greet(){}` | `const greet = function(){}` |

---

# Real-Life Example

```javascript
function calculateTotal(price, quantity){

    return price * quantity;

}

let total = calculateTotal(500,3);

console.log("Total Amount = ₹" + total);
```

---

## Output

```text
Total Amount = ₹1500
```

---

## Explanation

- The function `calculateTotal()` accepts the price and quantity of a product.
- It calculates the total amount by multiplying the two values.
- The `return` statement sends the result back.
- The returned value is stored in the variable `total` and displayed as **₹1500**.

---

# Summary

| Function Type | Description |
|--------------|-------------|
| Function Declaration | Standard named function created using the `function` keyword. |
| Function with Parameters | Accepts input values to perform different operations. |
| Function with Return Value | Returns a result using the `return` keyword. |
| Function Expression | A function stored inside a variable. |
| Anonymous Function | A function without a name, commonly used in callbacks. |

---

# Conclusion

Functions are one of the most important features of JavaScript. They help organize code into reusable blocks, making programs easier to read, maintain, and debug. In this part, we learned Function Declarations, Parameters, Return Values, Function Expressions, and Anonymous Functions, which form the foundation for advanced JavaScript programming.


# 4. Functions in JavaScript (Part 2)

## 4.6 Arrow Function

### Definition

An **Arrow Function** is a shorter and more modern way of writing functions in JavaScript. It was introduced in **ECMAScript 6 (ES6)** in 2015. Arrow functions make the code cleaner, shorter, and easier to read.

Unlike normal functions, arrow functions do **not** have their own `this` keyword. Instead, they inherit `this` from the surrounding scope.

---

## Syntax

```javascript
const functionName = (parameters) => {

    // Statements

};
```

---

## Practical Example 1

```javascript
const greet = () => {

    console.log("Welcome to JavaScript");

};

greet();
```

---

## Output

```text
Welcome to JavaScript
```

---

## Explanation

- `greet` is an arrow function.
- It takes no parameters.
- When `greet()` is called, it prints **"Welcome to JavaScript"**.

---

## Practical Example 2

```javascript
const add = (a, b) => {

    return a + b;

};

console.log(add(15, 25));
```

---

## Output

```text
40
```

---

## Explanation

- The function accepts two parameters: `a` and `b`.
- It adds both numbers.
- The result is returned and displayed.

---

## Short Arrow Function

If there is only one statement, braces `{}` and the `return` keyword can be omitted.

```javascript
const square = number => number * number;

console.log(square(6));
```

---

## Output

```text
36
```

---

## Applications

- ReactJS development
- Event handling
- Callback functions
- Array methods (`map()`, `filter()`, etc.)

---

# 4.7 Immediately Invoked Function Expression (IIFE)

## Definition

An **Immediately Invoked Function Expression (IIFE)** is a function that executes immediately after it is created. It does not need to be called separately.

It is commonly used to avoid polluting the global scope.

---

## Syntax

```javascript
(function(){

    // Code

})();
```

---

## Practical Example

```javascript
(function(){

    console.log("IIFE Executed Successfully");

})();
```

---

## Output

```text
IIFE Executed Successfully
```

---

## Explanation

- The function is enclosed in parentheses.
- The second pair of parentheses `()` immediately invokes it.
- The function executes as soon as the program reaches it.

---

## Another Example

```javascript
(function(name){

    console.log("Welcome " + name);

})("Ritesh");
```

---

## Output

```text
Welcome Ritesh
```

---

## Applications

- Initializing applications.
- Protecting variables from the global scope.
- Creating private variables.

---

# 4.8 Callback Function

## Definition

A **Callback Function** is a function passed as an argument to another function. It is executed after the first function completes its task.

Callbacks are commonly used for asynchronous operations such as API requests, timers, and event handling.

---

## Syntax

```javascript
function first(callback){

    callback();

}
```

---

## Practical Example

```javascript
function greet(name, callback){

    console.log("Hello " + name);

    callback();

}

function message(){

    console.log("Welcome to JavaScript");

}

greet("Ritesh", message);
```

---

## Output

```text
Hello Ritesh
Welcome to JavaScript
```

---

## Explanation

- The function `greet()` accepts a callback function.
- It first prints **Hello Ritesh**.
- Then it executes the callback function `message()`.
- Finally, **Welcome to JavaScript** is displayed.

---

## Another Example

```javascript
setTimeout(function(){

    console.log("Executed after 3 seconds.");

},3000);
```

---

## Output

```text
Executed after 3 seconds.

(Displayed after 3 seconds.)
```

---

## Applications

- API calls
- Event listeners
- File handling
- Timers

---

# 4.9 Recursive Function

## Definition

A **Recursive Function** is a function that calls itself until a specified condition is met.

Recursion is useful for solving problems that can be divided into smaller sub-problems.

---

## Syntax

```javascript
function functionName(){

    functionName();

}
```

---

## Practical Example

```javascript
function countdown(number){

    if(number == 0){

        console.log("Finished");

        return;

    }

    console.log(number);

    countdown(number - 1);

}

countdown(5);
```

---

## Output

```text
5
4
3
2
1
Finished
```

---

## Explanation

- The function starts with `5`.
- It prints the current value.
- Calls itself with `number - 1`.
- Stops when the value reaches `0`.

---

## Applications

- Factorial calculation.
- Searching algorithms.
- Tree traversal.
- Directory structures.

---

# 4.10 Generator Function

## Definition

A **Generator Function** is a special type of function that can pause its execution and resume later. It uses the `function*` syntax and the `yield` keyword.

Instead of returning all values at once, a generator produces values one at a time.

---

## Syntax

```javascript
function* generatorName(){

    yield value;

}
```

---

## Practical Example

```javascript
function* numbers(){

    yield 10;

    yield 20;

    yield 30;

}

let num = numbers();

console.log(num.next().value);

console.log(num.next().value);

console.log(num.next().value);
```

---

## Output

```text
10
20
30
```

---

## Explanation

- `function*` defines a generator function.
- Each `yield` pauses the function and returns a value.
- Calling `next()` resumes execution from where it stopped.
- Values are produced one by one instead of all at once.

## Applications

- Iterators
- Large data processing
- Lazy loading
- Data streaming

---

# Comparison of Function Types Covered in Part 2

| Function Type | Purpose | Example |
|--------------|---------|---------|
| Arrow Function | Shorter function syntax | `const add = (a, b) => a + b;` |
| IIFE | Executes immediately | `(function(){})();` |
| Callback Function | Passed to another function | `setTimeout()` |
| Recursive Function | Calls itself | `factorial()` |
| Generator Function | Produces values one by one | `function* demo(){}` |

---

# Real-Life Example

```javascript
function calculateBill(price, quantity, callback){

    let total = price * quantity;

    callback(total);

}

calculateBill(500, 3, function(total){

    console.log("Total Bill = ₹" + total);

});
```

---

## Output

```text
Total Bill = ₹1500
```

---

## Explanation

- The function `calculateBill()` receives the product price, quantity, and a callback function.
- It calculates the total bill by multiplying the price and quantity.
- The computed value (`1500`) is passed to the callback function.
- The callback function then prints **"Total Bill = ₹1500"**.
- This example demonstrates how callback functions allow one function to pass results to another function for further processing.

---

# Advantages of Functions Covered in Part 2

- Arrow functions provide shorter and cleaner syntax.
- IIFE prevents global namespace pollution.
- Callback functions make asynchronous programming possible.
- Recursive functions solve complex problems by breaking them into smaller parts.
- Generator functions improve memory efficiency by generating values one at a time.

---

# Disadvantages

- Arrow functions cannot be used as constructor functions.
- Excessive callbacks may lead to callback hell.
- Incorrect recursive functions can cause stack overflow.
- Generator functions are more difficult for beginners to understand.

---

# Summary

| Topic | Key Point |
|------|-----------|
| Arrow Function | Modern and concise function syntax introduced in ES6. |
| IIFE | Executes immediately after creation. |
| Callback Function | A function passed as an argument to another function. |
| Recursive Function | A function that calls itself until a base condition is met. |
| Generator Function | Produces values one at a time using `yield`. |

---

# Conclusion

Part 2 introduced modern and advanced JavaScript function concepts. Arrow Functions simplify syntax, IIFE helps avoid global scope pollution, Callback Functions enable asynchronous programming, Recursive Functions solve repetitive problems elegantly, and Generator Functions allow efficient, on-demand value generation. These concepts are widely used in modern JavaScript development, especially in frameworks like React, Node.js, and asynchronous programming.


# 4. Functions in JavaScript (Part 3)

## 4.11 Constructor Function

### Definition

A **Constructor Function** is a special type of function used to create multiple objects with similar properties and methods. It acts as a blueprint for creating objects. Constructor functions are called using the `new` keyword.

By convention, the name of a constructor function starts with a capital letter.

---

## Syntax

```javascript
function ConstructorName(parameter1, parameter2) {

    this.property1 = parameter1;
    this.property2 = parameter2;

}
```

---

## Practical Example

```javascript
function Student(name, age, course) {

    this.name = name;
    this.age = age;
    this.course = course;

}

let student1 = new Student("Ritesh", 21, "Computer Science");
let student2 = new Student("Rahul", 22, "Information Technology");

console.log(student1);
console.log(student2);
```

---

## Output

```text
Student {
  name: 'Ritesh',
  age: 21,
  course: 'Computer Science'
}

Student {
  name: 'Rahul',
  age: 22,
  course: 'Information Technology'
}
```

---

## Explanation

- The `Student` constructor function is created.
- The `new` keyword creates a new object.
- `this` refers to the newly created object.
- Each object stores its own values.

---

## Applications

- Creating student records.
- Employee management systems.
- Product catalogs.
- Library management systems.

---

# 4.12 Higher-Order Function

## Definition

A **Higher-Order Function** is a function that either:

- Accepts another function as an argument.
- Returns another function.

Higher-order functions make code more reusable and flexible.

---

## Example 1: Passing a Function

```javascript
function greet(name){

    return "Hello " + name;

}

function display(callback){

    console.log(callback("Ritesh"));

}

display(greet);
```

---

## Output

```text
Hello Ritesh
```

---

## Explanation

- `greet()` returns a greeting message.
- `display()` accepts another function as its argument.
- `display()` calls `greet()` and prints the returned value.

---

## Example 2: Returning a Function

```javascript
function multiply(num){

    return function(value){

        return value * num;

    };

}

let double = multiply(2);

console.log(double(5));
```

---

## Output

```text
10
```

---

## Explanation

- `multiply()` returns another function.
- `double` stores the returned function.
- Calling `double(5)` multiplies `5` by `2`.

---

## Applications

- Array methods (`map`, `filter`, `reduce`)
- Event handling
- Functional programming
- Middleware in frameworks

---

# 4.13 Default Parameters

## Definition

Default parameters allow a function parameter to have a predefined value if no value is passed during the function call.

---

## Syntax

```javascript
function functionName(parameter = defaultValue){

}
```

---

## Example

```javascript
function greet(name = "Guest"){

    console.log("Welcome " + name);

}

greet();

greet("Ritesh");
```

---

## Output

```text
Welcome Guest
Welcome Ritesh
```

---

## Explanation

- If no argument is passed, `"Guest"` is used.
- If an argument is passed, it replaces the default value.

---

## Applications

- Optional parameters.
- User-friendly function design.
- Form handling.

---

# 4.14 Rest Parameters

## Definition

The **Rest Parameter** allows a function to accept any number of arguments. It is represented by three dots (`...`).

The arguments are stored as an array.

---

## Syntax

```javascript
function functionName(...parameter){

}
```

---

## Example

```javascript
function sum(...numbers){

    let total = 0;

    for(let number of numbers){

        total += number;

    }

    return total;

}

console.log(sum(10,20));

console.log(sum(10,20,30));

console.log(sum(10,20,30,40));
```

---

## Output

```text
30
60
100
```

---

## Explanation

- All arguments are collected into the `numbers` array.
- The `for...of` loop adds each number.
- The total is returned.

---

## Applications

- Shopping cart totals.
- Calculator applications.
- Dynamic input handling.


# 4.15 Spread Operator with Functions

## Definition

The **Spread Operator (`...`)** expands an array or iterable into individual values. It is commonly used when passing array elements as function arguments.

The spread operator can also be used to copy arrays, merge arrays, and pass multiple values to functions.

---

## Syntax

```javascript
functionName(...array);
```

---

## Practical Example

```javascript
function add(a, b, c){

    return a + b + c;

}

let numbers = [10, 20, 30];

console.log(add(...numbers));
```

---

## Output

```text
60
```

---

## Explanation

- The array `numbers` contains three values.
- The spread operator (`...`) expands the array into individual values.
- The function receives `10`, `20`, and `30` as separate arguments.
- The sum of these values is returned.

---

## Applications

- Passing arrays as function arguments.
- Copying arrays.
- Merging arrays.
- Creating shallow copies of arrays and objects.

---

# 4.16 Function Scope

## Definition

**Scope** determines where a variable can be accessed within a program.

JavaScript provides three main types of scope:

- Global Scope
- Local (Function) Scope
- Block Scope

---

# A. Global Scope

## Definition

Variables declared outside any function are called **global variables**. They can be accessed from anywhere in the program.

### Example

```javascript
let college = "ABC College";

function showCollege(){

    console.log(college);

}

showCollege();
```

---

### Output

```text
ABC College
```

---

### Explanation

- `college` is declared outside the function.
- Therefore, it belongs to the global scope.
- Any function can access it.

---

# B. Local (Function) Scope

## Definition

Variables declared inside a function can only be accessed within that function.

### Example

```javascript
function display(){

    let name = "Ritesh";

    console.log(name);

}

display();

// console.log(name); // Error
```

---

### Output

```text
Ritesh
```

---

### Explanation

- `name` exists only inside the `display()` function.
- Trying to access it outside the function results in an error.

---

# C. Block Scope

## Definition

Variables declared using `let` or `const` inside a block `{}` are accessible only within that block.

### Example

```javascript
if(true){

    let age = 21;

    console.log(age);

}

// console.log(age); // Error
```

---

### Output

```text
21
```

---

### Explanation

- `age` is declared inside the `if` block.
- It cannot be accessed outside the block.

---

# Comparison of Function Types

| Function Type | Description |
|--------------|-------------|
| Function Declaration | Standard named function |
| Function Expression | Function assigned to a variable |
| Anonymous Function | Function without a name |
| Arrow Function | Shorter ES6 syntax |
| IIFE | Executes immediately |
| Callback Function | Passed as an argument |
| Recursive Function | Calls itself |
| Generator Function | Produces values using `yield` |
| Constructor Function | Creates objects using `new` |
| Higher-Order Function | Accepts or returns functions |

---

# Real-Life Example

```javascript
function calculateSalary(basicSalary, bonus = 0){

    return basicSalary + bonus;

}

let employee1 = calculateSalary(30000, 5000);

let employee2 = calculateSalary(25000);

console.log("Employee 1 Salary = ₹" + employee1);

console.log("Employee 2 Salary = ₹" + employee2);
```

---

## Output

```text
Employee 1 Salary = ₹35000
Employee 2 Salary = ₹25000
```

---

## Explanation

- The `calculateSalary()` function calculates the total salary.
- The `bonus` parameter has a default value of `0`.
- Employee 1 receives a bonus, so the total salary becomes **₹35,000**.
- Employee 2 does not receive a bonus, so the default value is used, resulting in **₹25,000**.

---

# Applications of Functions

- Form validation
- User authentication
- Calculator applications
- Banking systems
- E-commerce websites
- Event handling
- Data processing
- API integration
- Game development
- Automation scripts

---

# Advantages of Functions

- Promote code reusability.
- Reduce code duplication.
- Improve readability.
- Simplify debugging and maintenance.
- Support modular programming.
- Make programs easier to test.

---

# Disadvantages of Functions

- Too many small functions can make code difficult to follow.
- Recursive functions may cause stack overflow if not implemented correctly.
- Function calls introduce a small performance overhead.
- Poorly named functions reduce code readability.

---

# Summary

| Topic | Description |
|--------|-------------|
| Constructor Function | Creates multiple objects using the `new` keyword. |
| Higher-Order Function | Accepts or returns another function. |
| Default Parameters | Assigns default values to parameters. |
| Rest Parameters | Accepts any number of arguments as an array. |
| Spread Operator | Expands an array into individual values. |
| Function Scope | Defines where variables can be accessed. |

---

# Conclusion

Functions are one of the most important building blocks of JavaScript. They make programs modular, reusable, and easier to maintain. In this chapter, we explored different types of functions such as constructor functions, higher-order functions, default parameters, rest parameters, the spread operator, and function scope. Mastering these concepts helps developers write clean, efficient, and scalable JavaScript applications.