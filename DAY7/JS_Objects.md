# 6. Objects and Their Methods (Part 1)

## Introduction

An **Object** is one of the most important data structures in JavaScript. It is used to store data in the form of **key-value pairs**. Unlike arrays, where elements are accessed using indexes, object properties are accessed using their **keys** (property names).

Objects can store different types of values such as strings, numbers, Boolean values, arrays, functions, and even other objects. They are widely used in JavaScript because they represent real-world entities such as students, employees, products, cars, bank accounts, and users.

For example, instead of storing a student's details in separate variables, all related information can be grouped into a single object.

## Why Do We Use Objects?

Objects are used because they:

1. Store related data together.
2. Represent real-world entities.
3. Improve code organization.
4. Allow easy access to properties.
5. Support methods (functions inside objects).

## Advantages of Objects

1. Store multiple related values.
2. Easy to access using property names.
3. Dynamic in nature.
4. Can contain functions (methods).
5. Improve code readability.
6. Widely used in web development.

## General Syntax of an Object

```javascript
let objectName = {
    key1: value1,
    key2: value2,
    key3: value3
};
```

---

## 6.1 Creating Objects

### Definition
An object is created using curly braces `{}`. Each property consists of a key and a value, separated by a colon (`:`).

### Syntax
```javascript
let student = {
    name: "Ritesh",
    age: 21,
    course: "Computer Science"
};
```

### Practical Example 1
```javascript
let student = {
    name: "Ritesh",
    age: 21,
    city: "Pune"
};

console.log(student);
```

**Output**
```
{ name: 'Ritesh', age: 21, city: 'Pune' }
```

**Explanation**
1. A student object is created.
2. It contains three properties.
3. Each property has a key and a corresponding value.

### Practical Example 2
```javascript
let car = {
    brand: "Toyota",
    model: "Innova",
    year: 2024
};

console.log(car);
```

**Output**
```
{ brand: 'Toyota', model: 'Innova', year: 2024 }
```

### Applications
1. Student records.
2. Employee details.
3. Product information.
4. Banking applications.

---

## 6.2 Accessing Object Properties

### Definition
Object properties can be accessed in two ways:

1. Dot Notation (`.`)
2. Bracket Notation (`[]`)

### Syntax
```javascript
// Dot Notation
objectName.propertyName;

// Bracket Notation
objectName["propertyName"];
```

### Practical Example
```javascript
let employee = {
    name: "Rahul",
    salary: 45000,
    department: "IT"
};

console.log(employee.name);
console.log(employee["salary"]);
```

**Output**
```
Rahul
45000
```

**Explanation**
1. `employee.name` accesses the name property.
2. `employee["salary"]` accesses the salary property.
3. Both notations return the property value.

### Applications
1. Reading user information.
2. Displaying product details.
3. Fetching employee records.

---

## 6.3 Adding New Properties

### Definition
New properties can be added to an object at any time using dot notation or bracket notation.

### Syntax
```javascript
objectName.newProperty = value;
```

### Practical Example
```javascript
let student = {
    name: "Ritesh",
    age: 21
};

student.city = "Pune";

console.log(student);
```

**Output**
```
{ name: 'Ritesh', age: 21, city: 'Pune' }
```

**Explanation**
1. Initially, the object has two properties.
2. A new property `city` is added.
3. The updated object is displayed.

### Applications
1. Adding user information.
2. Updating customer profiles.
3. Expanding product details.

---

## 6.4 Updating Object Properties

### Definition
The value of an existing property can be modified by assigning a new value.

### Syntax
```javascript
objectName.propertyName = newValue;
```

### Practical Example
```javascript
let student = {
    name: "Ritesh",
    age: 21
};

student.age = 22;

console.log(student);
```

**Output**
```
{ name: 'Ritesh', age: 22 }
```

**Explanation**
1. The `age` property originally contains 21.
2. It is updated to 22.
3. The object reflects the new value.

### Applications
1. Updating salaries.
2. Editing user profiles.
3. Modifying product prices.

---

## 6.5 Deleting Object Properties

### Definition
The `delete` keyword removes a property from an object permanently.

### Syntax
```javascript
delete objectName.propertyName;
```

### Practical Example
```javascript
let employee = {
    name: "Rahul",
    salary: 45000,
    city: "Mumbai"
};

delete employee.city;

console.log(employee);
```

**Output**
```
{ name: 'Rahul', salary: 45000 }
```

**Explanation**
1. The property `city` is removed.
2. The remaining properties stay unchanged.

### Applications
1. Removing outdated information.
2. Deleting inactive users.
3. Cleaning unnecessary data.

---

## 6.6 Object Methods

### Definition
A method is a function stored inside an object. Methods allow objects to perform actions using their own data.

### Syntax
```javascript
let objectName = {
    methodName: function(){
        // code
    }
};
```

### Practical Example
```javascript
let student = {
    name: "Ritesh",

    greet: function(){
        console.log("Welcome " + this.name);
    }
};

student.greet();
```

**Output**
```
Welcome Ritesh
```

**Explanation**
1. `greet()` is a method inside the object.
2. `this.name` refers to the object's name property.
3. Calling `student.greet()` prints the greeting.

### Applications
1. Banking operations.
2. User authentication.
3. Shopping cart calculations.
4. Employee management.

### Real-Life Example
```javascript
let product = {
    id: 101,
    name: "Laptop",
    price: 55000,

    display: function(){
        console.log("Product Name: " + this.name);
        console.log("Price: ₹" + this.price);
    }
};

product.display();
```

**Output**
```
Product Name: Laptop
Price: ₹55000
```

**Explanation**
1. A `product` object stores product details.
2. The `display()` method prints the product name and price.
3. `this` refers to the current object, allowing access to its properties.

---

## Conclusion (Part 1)

In this section, we learned the fundamentals of JavaScript objects, including:

1. Creating objects.
2. Accessing properties.
3. Adding, updating, and deleting properties.
4. Creating object methods.

Objects are essential for representing real-world entities and organizing related data in JavaScript. Understanding these basics provides a strong foundation for working with more advanced object methods.

# 6. Objects and Their Methods (Part 2)

## 6.7 `this` Keyword

### Definition
The `this` keyword refers to the current object that is executing the method. It is mainly used inside object methods to access the object's own properties and methods.

Using `this` makes the code reusable because it always refers to the object that calls the method.

### Syntax
```javascript
let objectName = {
    property: value,

    method: function(){
        console.log(this.property);
    }
};
```

### Practical Example
```javascript
let employee = {
    name: "Ritesh",
    department: "IT",

    display: function(){
        console.log("Employee Name: " + this.name);
        console.log("Department: " + this.department);
    }
};

employee.display();
```

**Output**
```
Employee Name: Ritesh
Department: IT
```

**Explanation**
1. `this.name` refers to the name property of the employee object.
2. `this.department` refers to the department property.
3. `display()` prints both values.

### Applications
1. Object methods.
2. Banking applications.
3. Employee management systems.
4. Shopping cart calculations.

---

## 6.8 `Object.keys()` Method

### Definition
The `Object.keys()` method returns an array containing all the property names (keys) of an object.

### Syntax
```javascript
Object.keys(objectName);
```

### Practical Example
```javascript
let student = {
    name: "Ritesh",
    age: 21,
    city: "Pune"
};

console.log(Object.keys(student));
```

**Output**
```
["name", "age", "city"]
```

**Explanation**
1. The method reads all property names.
2. It returns them as an array.

### Applications
1. Listing object properties.
2. Dynamic table generation.
3. Object traversal.

---

## 6.9 `Object.values()` Method

### Definition
The `Object.values()` method returns an array containing all the values of an object.

### Syntax
```javascript
Object.values(objectName);
```

### Practical Example
```javascript
let student = {
    name: "Ritesh",
    age: 21,
    city: "Pune"
};

console.log(Object.values(student));
```

**Output**
```
["Ritesh", 21, "Pune"]
```

**Explanation**
1. The method extracts all values.
2. The values are stored in a new array.

### Applications
1. Displaying values.
2. Exporting data.
3. Data processing.

---

## 6.10 `Object.entries()` Method

### Definition
The `Object.entries()` method returns an array containing both keys and values as nested arrays.

### Syntax
```javascript
Object.entries(objectName);
```

### Practical Example
```javascript
let student = {
    name: "Ritesh",
    age: 21
};

console.log(Object.entries(student));
```

**Output**
```
[
  ["name", "Ritesh"],
  ["age", 21]
]
```

**Explanation**
1. Each property becomes a separate array.
2. The first value is the key.
3. The second value is the corresponding value.

### Applications
1. Looping through objects.
2. Converting objects into arrays.
3. Displaying key-value pairs.

---

## 6.11 `Object.assign()` Method

### Definition
The `Object.assign()` method copies properties from one or more source objects into a target object.

It is commonly used to merge objects or create a copy of an object.

### Syntax
```javascript
Object.assign(targetObject, sourceObject);
```

### Practical Example
```javascript
let person = {
    name: "Ritesh"
};

let details = {
    age: 21,
    city: "Pune"
};

let result = Object.assign({}, person, details);

console.log(result);
```

**Output**
```
{ name: 'Ritesh', age: 21, city: 'Pune' }
```

**Explanation**
1. An empty object `{}` is used as the target.
2. Properties from both objects are copied.
3. A new merged object is created.

### Applications
1. Merging user profiles.
2. Copying objects.
3. Updating configuration settings.

---

## 6.12 `Object.freeze()` Method

### Definition
The `Object.freeze()` method prevents an object from being modified.

After freezing an object:
1. New properties cannot be added.
2. Existing properties cannot be changed.
3. Existing properties cannot be deleted.

### Syntax
```javascript
Object.freeze(objectName);
```

### Practical Example
```javascript
let student = {
    name: "Ritesh"
};

Object.freeze(student);

student.name = "Rahul";

console.log(student);
```

**Output**
```
{ name: 'Ritesh' }
```

**Explanation**
1. The object is frozen.
2. Attempting to change `name` has no effect.
3. The original value remains unchanged.

### Applications
1. Application settings.
2. Constant configuration objects.
3. Security-sensitive data.

---

## 6.13 `Object.seal()` Method

### Definition
The `Object.seal()` method prevents adding or deleting properties, but it allows modification of existing property values.

### Syntax
```javascript
Object.seal(objectName);
```

### Practical Example
```javascript
let student = {
    name: "Ritesh",
    age: 21
};

Object.seal(student);

student.age = 22;
student.city = "Pune";
delete student.name;

console.log(student);
```

**Output**
```
{ name: 'Ritesh', age: 22 }
```

**Explanation**
1. `age` is updated successfully.
2. `city` cannot be added.
3. `name` cannot be deleted.
4. Only existing values can be modified.

### Applications
1. Protecting object structure.
2. Configuration objects.
3. User profile management.

---

## Comparison of Object Methods

| Method | Purpose | Returns |
|---|---|---|
| `Object.keys()` | Returns property names | Array |
| `Object.values()` | Returns property values | Array |
| `Object.entries()` | Returns key-value pairs | Array |
| `Object.assign()` | Copies or merges objects | Object |
| `Object.freeze()` | Prevents all modifications | Frozen Object |
| `Object.seal()` | Prevents adding/deleting properties | Sealed Object |

---

## Real-Life Example
```javascript
let employee = {
    id: 101,
    name: "Ritesh",
    department: "IT"
};

console.log("Keys:");
console.log(Object.keys(employee));

console.log("Values:");
console.log(Object.values(employee));

console.log("Entries:");
console.log(Object.entries(employee));
```

**Output**
```
Keys:
["id", "name", "department"]

Values:
[101, "Ritesh", "IT"]

Entries:
[
  ["id", 101],
  ["name", "Ritesh"],
  ["department", "IT"]
]
```

**Explanation**
1. `Object.keys()` returns all property names.
2. `Object.values()` returns all property values.
3. `Object.entries()` returns each property as a key-value pair inside a nested array.
4. These methods are useful for iterating over objects and processing object data dynamically.

---

## Conclusion (Part 2)

In this section, we learned about advanced object features, including:

1. The `this` keyword.
2. `Object.keys()`
3. `Object.values()`
4. `Object.entries()`
5. `Object.assign()`
6. `Object.freeze()`
7. `Object.seal()`

These methods simplify object manipulation, data retrieval, object copying, and controlling modifications. They are widely used in modern JavaScript applications to write clean, secure, and maintainable code.

# 6. Objects and Their Methods (Part 3)

## 6.14 Object Destructuring

### Definition
Object Destructuring is an ES6 feature that allows us to extract properties from an object and store them directly into variables. It makes the code shorter, cleaner, and easier to read.

### Syntax
```javascript
let {property1, property2} = objectName;
```

### Practical Example
```javascript
let student = {
    name: "Ritesh",
    age: 21,
    city: "Pune"
};

let {name, age, city} = student;

console.log(name);
console.log(age);
console.log(city);
```

**Output**
```
Ritesh
21
Pune
```

**Explanation**
1. The object contains three properties.
2. Destructuring assigns the values directly to variables.
3. No need to write `student.name`, `student.age`, etc.

### Applications
1. API responses.
2. ReactJS components.
3. User profile management.
4. Cleaner code.

---

## 6.15 Spread Operator with Objects

### Definition
The Spread Operator (`...`) copies or merges object properties into a new object.

It creates a shallow copy of an object.

### Syntax
```javascript
let newObject = {...oldObject};
```

### Practical Example
```javascript
let student = {
    name: "Ritesh",
    age: 21
};

let details = {
    city: "Pune"
};

let result = {
    ...student,
    ...details
};

console.log(result);
```

**Output**
```
{
  name: 'Ritesh',
  age: 21,
  city: 'Pune'
}
```

**Explanation**
1. `...student` copies all properties.
2. `...details` adds another property.
3. A new merged object is created.

### Applications
1. Copying objects.
2. Merging objects.
3. Updating state in React.

---

## 6.16 `JSON.stringify()` Method

### Definition
The `JSON.stringify()` method converts a JavaScript object into a JSON string.

JSON stands for JavaScript Object Notation.

### Syntax
```javascript
JSON.stringify(objectName);
```

### Practical Example
```javascript
let student = {
    name: "Ritesh",
    age: 21
};

let jsonData = JSON.stringify(student);

console.log(jsonData);
```

**Output**
```
{"name":"Ritesh","age":21}
```

**Explanation**
1. The object is converted into a JSON string.
2. It can now be stored or transmitted over a network.

### Applications
1. Sending data to APIs.
2. Local storage.
3. File storage.

---

## 6.17 `JSON.parse()` Method

### Definition
The `JSON.parse()` method converts a JSON string into a JavaScript object.

### Syntax
```javascript
JSON.parse(jsonString);
```

### Practical Example
```javascript
let jsonData = '{"name":"Ritesh","age":21}';

let student = JSON.parse(jsonData);

console.log(student);
```

**Output**
```
{ name: 'Ritesh', age: 21 }
```

**Explanation**
1. The JSON string is converted into an object.
2. Properties can now be accessed using dot notation.

### Applications
1. Receiving API responses.
2. Reading JSON files.
3. Data exchange.

---

## 6.18 `hasOwnProperty()` Method

### Definition
The `hasOwnProperty()` method checks whether an object contains a specific property.

It returns either `true` or `false`.

### Syntax
```javascript
objectName.hasOwnProperty("propertyName");
```

### Practical Example
```javascript
let student = {
    name: "Ritesh",
    age: 21
};

console.log(student.hasOwnProperty("name"));
console.log(student.hasOwnProperty("city"));
```

**Output**
```
true
false
```

**Explanation**
1. `"name"` exists in the object.
2. `"city"` does not exist.

### Applications
1. Form validation.
2. Checking object properties.
3. Data verification.

---

## 6.19 `Object.hasOwn()` Method

### Definition
The `Object.hasOwn()` method checks whether an object has a specified property. It is a modern alternative to `hasOwnProperty()` (introduced in ES2022).

### Syntax
```javascript
Object.hasOwn(objectName, "propertyName");
```

### Practical Example
```javascript
let employee = {
    id: 101,
    name: "Rahul"
};

console.log(Object.hasOwn(employee, "id"));
console.log(Object.hasOwn(employee, "salary"));
```

**Output**
```
true
false
```

**Explanation**
1. `"id"` exists in the object.
2. `"salary"` is not found.

### Applications
1. Property validation.
2. API response checking.
3. Configuration verification.

---

## Comparison of Object Methods

| Method | Purpose | Returns |
|---|---|---|
| `Object.keys()` | Returns property names | Array |
| `Object.values()` | Returns property values | Array |
| `Object.entries()` | Returns key-value pairs | Array |
| `Object.assign()` | Copies/Merges objects | Object |
| `Object.freeze()` | Prevents all modifications | Frozen Object |
| `Object.seal()` | Prevents adding/removing properties | Sealed Object |
| `JSON.stringify()` | Converts object to JSON string | String |
| `JSON.parse()` | Converts JSON string to object | Object |
| `hasOwnProperty()` | Checks property existence | Boolean |
| `Object.hasOwn()` | Modern property check | Boolean |

---

## Real-Life Example
```javascript
let user = {
    id: 101,
    name: "Ritesh",
    email: "ritesh@gmail.com"
};

// Convert object to JSON
let jsonData = JSON.stringify(user);
console.log(jsonData);

// Convert JSON back to object
let objectData = JSON.parse(jsonData);
console.log(objectData);

// Check property
console.log(Object.hasOwn(objectData, "email"));
```

**Output**
```
{"id":101,"name":"Ritesh","email":"ritesh@gmail.com"}

{ id: 101, name: 'Ritesh', email: 'ritesh@gmail.com' }

true
```

**Explanation**
1. The `user` object stores user information.
2. `JSON.stringify()` converts it into a JSON string for storage or transmission.
3. `JSON.parse()` converts the JSON string back into a JavaScript object.
4. `Object.hasOwn()` checks whether the `email` property exists and returns `true`.

---

## Applications of Objects

1. Student Management Systems.
2. Employee Records.
3. Banking Applications.
4. E-commerce Websites.
5. User Authentication.
6. Inventory Management.
7. Social Media Applications.
8. API Response Handling.
9. Configuration Settings.
10. Game Development.

---

## Advantages of Objects

1. Store related data together.
2. Represent real-world entities.
3. Easy to access using property names.
4. Can contain methods.
5. Dynamic and flexible.
6. Support nested structures.
7. Improve code organization.

---

## Disadvantages of Objects

1. Searching through large objects may require additional logic.
2. Deeply nested objects can become difficult to manage.
3. Copying objects incorrectly may create shared references.
4. Objects consume more memory than simple variables.

---

## Final Conclusion

Objects are one of the most powerful features of JavaScript because they allow developers to organize related data and behavior in a structured way. Features such as:

1. Object methods.
2. The `this` keyword.
3. Destructuring.
4. The spread operator.
5. JSON methods.
6. Built-in methods like `Object.keys()`, `Object.values()`, `Object.entries()`, `Object.assign()`, `Object.freeze()`, and `Object.seal()`.

...make objects flexible and easy to work with. A solid understanding of objects is essential for developing modern JavaScript applications, as they are widely used in APIs, web development, databases, and real-world software systems.