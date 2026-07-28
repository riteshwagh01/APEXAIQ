# 7. DOM (Document Object Model) – Part 1

## Introduction

The **Document Object Model (DOM)** is a programming interface provided by web browsers that represents an HTML document as a **tree-like structure**. Each HTML element becomes an object (node) that JavaScript can access and manipulate.

Using the DOM, JavaScript can:

1. Access HTML elements.
2. Change content dynamically.
3. Modify CSS styles.
4. Add or remove elements.
5. Handle user interactions such as button clicks, keyboard input, and mouse events.

The DOM is one of the most important concepts in JavaScript because it connects JavaScript with HTML and CSS, allowing developers to create dynamic and interactive web pages.

## Why Do We Use DOM?

DOM is used because it allows JavaScript to:

1. Access HTML elements.
2. Modify webpage content.
3. Change CSS styles dynamically.
4. Create interactive websites.
5. Respond to user actions.
6. Add or remove HTML elements.

## Advantages of DOM

1. Makes web pages interactive.
2. Allows dynamic content updates.
3. Easy manipulation of HTML elements.
4. Supports event handling.
5. Improves user experience.

## DOM Tree Structure

Consider the following HTML document:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Website</title>
</head>
<body>
    <h1>Hello World</h1>
    <p>Welcome to JavaScript</p>
</body>
</html>
```

The DOM Tree looks like:

```
Document
│
└── html
    ├── head
    │     └── title
    │
    └── body
          ├── h1
          └── p
```

**Explanation**
1. `document` is the root object.
2. `html` is the main element.
3. `head` and `body` are child elements.
4. `title`, `h1`, and `p` are descendants.

---

## 7.1 `getElementById()`

### Definition
The `getElementById()` method selects an HTML element using its unique `id`.

It returns a single element.

### Syntax
```javascript
document.getElementById("idName");
```

### HTML Example
```html
<h1 id="heading">Welcome</h1>
```

### JavaScript Example
```javascript
let heading = document.getElementById("heading");

console.log(heading);
```

**Output**
```html
<h1 id="heading">Welcome</h1>
```

**Explanation**
1. JavaScript searches for the element with id `"heading"`.
2. It returns that HTML element.

### Applications
1. Updating headings.
2. Reading form values.
3. Login forms.

---

## 7.2 `getElementsByClassName()`

### Definition
This method selects all elements having the specified class name.

It returns an **HTMLCollection**.

### Syntax
```javascript
document.getElementsByClassName("className");
```

### HTML Example
```html
<p class="info">JavaScript</p>
<p class="info">HTML</p>
<p class="info">CSS</p>
```

### JavaScript Example
```javascript
let data = document.getElementsByClassName("info");

console.log(data);
```

**Output**
```
HTMLCollection(3)
```

**Explanation**
1. Three elements have the class `"info"`.
2. All are returned inside an HTMLCollection.

### Applications
1. Updating multiple paragraphs.
2. Changing multiple images.
3. Styling multiple cards.

---

## 7.3 `getElementsByTagName()`

### Definition
This method selects all elements with a particular HTML tag.

### Syntax
```javascript
document.getElementsByTagName("tagName");
```

### HTML Example
```html
<h2>HTML</h2>
<h2>CSS</h2>
<h2>JavaScript</h2>
```

### JavaScript Example
```javascript
let headings = document.getElementsByTagName("h2");

console.log(headings);
```

**Output**
```
HTMLCollection(3)
```

**Explanation**
1. All `<h2>` elements are selected.
2. The result is an HTMLCollection.

### Applications
1. Selecting all headings.
2. Styling all images.
3. Processing tables.

---

## 7.4 `querySelector()`

### Definition
The `querySelector()` method selects the **first** element that matches a CSS selector.

### Syntax
```javascript
document.querySelector("selector");
```

### HTML Example
```html
<p class="info">HTML</p>
<p class="info">CSS</p>
<p class="info">JavaScript</p>
```

### JavaScript Example
```javascript
let item = document.querySelector(".info");

console.log(item);
```

**Output**
```html
<p class="info">HTML</p>
```

**Explanation**
1. Only the first matching element is selected.
2. It accepts CSS selectors like:
   - id (`#id`)
   - class (`.class`)
   - tag (`p`)

### Applications
1. Selecting the first button.
2. Selecting the first image.
3. Updating a heading.

---

## 7.5 `querySelectorAll()`

### Definition
The `querySelectorAll()` method selects **all** matching elements based on a CSS selector.

It returns a **NodeList**.

### Syntax
```javascript
document.querySelectorAll("selector");
```

### HTML Example
```html
<li>Apple</li>
<li>Mango</li>
<li>Banana</li>
```

### JavaScript Example
```javascript
let fruits = document.querySelectorAll("li");

console.log(fruits);
```

**Output**
```
NodeList(3)
```

**Explanation**
1. All `<li>` elements are selected.
2. The returned value is a NodeList.
3. NodeLists can be traversed using `forEach()`.

### Applications
1. Selecting all buttons.
2. Selecting all images.
3. Selecting multiple cards.

---

## Difference Between HTMLCollection and NodeList

| HTMLCollection | NodeList |
|---|---|
| Returned by `getElementsByClassName()` and `getElementsByTagName()` | Returned by `querySelectorAll()` |
| Live Collection | Static Collection |
| Doesn't directly support `forEach()` | Supports `forEach()` |

---

## Real-Life Example

### HTML
```html
<h1 id="title">Welcome</h1>
<p class="info">HTML</p>
<p class="info">CSS</p>
<p class="info">JavaScript</p>
```

### JavaScript
```javascript
let heading = document.getElementById("title");

console.log(heading.innerText);

let subjects = document.querySelectorAll(".info");

subjects.forEach(function(subject){
    console.log(subject.innerText);
});
```

**Output**
```
Welcome
HTML
CSS
JavaScript
```

**Explanation**
1. `getElementById()` selects the heading.
2. `innerText` displays the heading text.
3. `querySelectorAll()` selects all paragraphs with the class `info`.
4. `forEach()` prints each paragraph's text.

---

## Conclusion (Part 1)

In this section, we learned the basics of the Document Object Model (DOM) and how JavaScript interacts with HTML documents. We covered:

1. The DOM tree structure.
2. `getElementById()`
3. `getElementsByClassName()`
4. `getElementsByTagName()`
5. `querySelector()`
6. `querySelectorAll()`

These methods are fundamental for locating and manipulating elements on a webpage.

# 7. DOM (Document Object Model) – Part 2

## 7.6 `innerHTML` Property

### Definition
The `innerHTML` property is used to get or set the HTML content inside an element. It reads or modifies both the text and HTML tags within the selected element.

### Syntax
```javascript
element.innerHTML;

// To change the content:
element.innerHTML = "New HTML Content";
```

### HTML Example
```html
<p id="demo">Hello</p>
```

### JavaScript Example
```javascript
let element = document.getElementById("demo");

element.innerHTML = "<h2>Welcome to JavaScript</h2>";
```

**Output**
```html
<h2>Welcome to JavaScript</h2>
```

**Explanation**
1. The paragraph content is replaced.
2. Since `innerHTML` understands HTML tags, `<h2>` is rendered as a heading.

### Applications
1. Displaying dynamic HTML.
2. Updating tables.
3. Creating dynamic web pages.

---

## 7.7 `innerText` Property

### Definition
The `innerText` property gets or sets only the visible text inside an element. It ignores HTML tags and respects CSS styling such as hidden elements.

### Syntax
```javascript
element.innerText;
```

### HTML Example
```html
<p id="message">Hello World</p>
```

### JavaScript Example
```javascript
let msg = document.getElementById("message");

msg.innerText = "JavaScript Tutorial";
```

**Output**
```
JavaScript Tutorial
```

**Explanation**
1. Only text changes.
2. No HTML formatting is applied.

### Applications
1. Updating labels.
2. Displaying messages.
3. Showing notifications.

---

## 7.8 `textContent` Property

### Definition
The `textContent` property returns or changes all text inside an element, including hidden text. It does not interpret HTML tags.

### Syntax
```javascript
element.textContent;
```

### Practical Example
```html
<p id="data">Old Text</p>
```
```javascript
let text = document.getElementById("data");

text.textContent = "New Text";
```

**Output**
```
New Text
```

---

## Difference Between `innerHTML`, `innerText`, and `textContent`

| Property | Reads HTML Tags | Reads Visible Text | Includes Hidden Text |
|---|---|---|---|
| `innerHTML` | ✅ Yes | ✅ Yes | ❌ No |
| `innerText` | ❌ No | ✅ Yes | ❌ No |
| `textContent` | ❌ No | ✅ Yes | ✅ Yes |

---

## 7.9 `setAttribute()` Method

### Definition
The `setAttribute()` method adds a new attribute or changes the value of an existing attribute.

### Syntax
```javascript
element.setAttribute("attribute", "value");
```

### HTML Example
```html
<img id="image">
```

### JavaScript Example
```javascript
let img = document.getElementById("image");

img.setAttribute("src", "photo.jpg");
img.setAttribute("alt", "Nature Image");
```

**Output**
```html
<img id="image" src="photo.jpg" alt="Nature Image">
```

### Applications
1. Changing image sources.
2. Setting hyperlinks.
3. Updating form fields.

---

## 7.10 `getAttribute()` Method

### Definition
The `getAttribute()` method returns the value of an attribute.

### Syntax
```javascript
element.getAttribute("attribute");
```

### Practical Example
```html
<a id="link" href="https://example.com">Visit</a>
```
```javascript
let link = document.getElementById("link");

console.log(link.getAttribute("href"));
```

**Output**
```
https://example.com
```

**Explanation**
1. Reads the value of the `href` attribute.
2. Returns it as a string.

---

## 7.11 `removeAttribute()` Method

### Definition
The `removeAttribute()` method removes an attribute from an element.

### Syntax
```javascript
element.removeAttribute("attribute");
```

### Practical Example
```html
<input id="box" disabled>
```
```javascript
let input = document.getElementById("box");

input.removeAttribute("disabled");
```

**Output**
```html
<input id="box">
```

**Explanation**
1. The `disabled` attribute is removed.
2. The input field becomes editable.

---

## 7.12 Changing CSS Styles

### Definition
JavaScript can change CSS styles dynamically using the `style` property.

### Syntax
```javascript
element.style.property = "value";
```

### Practical Example
```html
<h1 id="title">JavaScript</h1>
```
```javascript
let heading = document.getElementById("title");

heading.style.color = "blue";
heading.style.backgroundColor = "yellow";
heading.style.fontSize = "40px";
```

**Output**

The heading appears:
1. Blue text
2. Yellow background
3. Font size: 40px

### Applications
1. Dark mode.
2. Theme switching.
3. Dynamic styling.

---

## 7.13 `classList.add()`

### Definition
The `classList.add()` method adds one or more CSS classes to an element.

### Syntax
```javascript
element.classList.add("className");
```

### Practical Example
```html
<p id="demo">Hello</p>
```
```javascript
let para = document.getElementById("demo");

para.classList.add("highlight");
```

**Output**
```html
<p id="demo" class="highlight">Hello</p>
```

---

## 7.14 `classList.remove()`

### Definition
The `classList.remove()` method removes an existing CSS class.

### Syntax
```javascript
element.classList.remove("className");
```

### Practical Example
```javascript
para.classList.remove("highlight");
```

**Output**
```html
<p id="demo">Hello</p>
```

---

## 7.15 `classList.toggle()`

### Definition
The `classList.toggle()` method adds a class if it is not present and removes it if it already exists.

### Syntax
```javascript
element.classList.toggle("className");
```

### Practical Example
```javascript
let heading = document.getElementById("title");

heading.classList.toggle("darkMode");
```

**Explanation**
1. First click → Class is added.
2. Second click → Class is removed.
3. Third click → Added again.

### Applications
1. Dark mode.
2. Show/Hide menu.
3. Expand/Collapse sections.

---

## Real-Life Example

### HTML
```html
<h2 id="heading">Welcome</h2>

<button onclick="changeStyle()">Change Style</button>
```

### JavaScript
```javascript
function changeStyle(){
    let heading = document.getElementById("heading");

    heading.innerText = "JavaScript DOM";
    heading.style.color = "red";
    heading.style.fontSize = "35px";
}
```

**Output**

Initially:
```
Welcome
```

After clicking the button:
```
JavaScript DOM
```

The heading becomes:
1. Red in color
2. Font size: 35px

**Explanation**
1. The button calls the `changeStyle()` function.
2. The function selects the heading using `getElementById()`.
3. `innerText` changes the displayed text.
4. The `style` property updates the text color and font size dynamically.

---

## Conclusion (Part 2)

In this section, we learned how to modify webpage content and appearance using DOM properties and methods. We covered:

1. `innerHTML`
2. `innerText`
3. `textContent`
4. Attribute methods (`setAttribute()`, `getAttribute()`, `removeAttribute()`)
5. CSS styling through JavaScript
6. `classList` methods (`add()`, `remove()`, and `toggle()`)

These features enable developers to create dynamic and interactive web pages.

# 7. DOM (Document Object Model) – Part 3

## 7.16 `createElement()` Method

### Definition
The `createElement()` method is used to create a new HTML element dynamically using JavaScript. The created element is not displayed on the webpage until it is added to the DOM.

### Syntax
```javascript
document.createElement("tagName");
```

### Practical Example

**HTML**
```html
<div id="container"></div>
```

**JavaScript**
```javascript
let heading = document.createElement("h2");

heading.innerText = "Welcome to JavaScript";

console.log(heading);
```

**Output**
```html
<h2>Welcome to JavaScript</h2>
```

**Explanation**
1. `createElement("h2")` creates a new `<h2>` element.
2. `innerText` adds text to the heading.
3. The element exists in memory but is not yet visible on the webpage.

### Applications
1. Creating dynamic cards.
2. Generating product lists.
3. Building menus dynamically.

---

## 7.17 `appendChild()` Method

### Definition
The `appendChild()` method adds a newly created element as the last child of a parent element.

### Syntax
```javascript
parentElement.appendChild(childElement);
```

### Practical Example

**HTML**
```html
<div id="container"></div>
```

**JavaScript**
```javascript
let container = document.getElementById("container");

let para = document.createElement("p");

para.innerText = "This paragraph was created using JavaScript.";

container.appendChild(para);
```

**Output**
```html
<div id="container">
    <p>This paragraph was created using JavaScript.</p>
</div>
```

**Explanation**
1. A paragraph element is created.
2. `appendChild()` inserts it inside the div.
3. The paragraph becomes visible on the webpage.

### Applications
1. Adding comments.
2. Creating notifications.
3. Dynamic product cards.

---

## 7.18 `removeChild()` Method

### Definition
The `removeChild()` method removes a child element from its parent.

### Syntax
```javascript
parentElement.removeChild(childElement);
```

### Practical Example

**HTML**
```html
<ul id="list">
    <li>Apple</li>
    <li id="remove">Banana</li>
</ul>
```

**JavaScript**
```javascript
let list = document.getElementById("list");

let item = document.getElementById("remove");

list.removeChild(item);
```

**Output**
```html
<ul id="list">
    <li>Apple</li>
</ul>
```

**Explanation**
1. The `<li>` containing "Banana" is selected.
2. `removeChild()` removes it from the list.

### Applications
1. Removing completed tasks.
2. Deleting products.
3. Removing notifications.

---

## 7.19 `replaceChild()` Method

### Definition
The `replaceChild()` method replaces an existing child element with a new element.

### Syntax
```javascript
parentElement.replaceChild(newChild, oldChild);
```

### Practical Example

**HTML**
```html
<div id="box">
    <p id="old">Old Paragraph</p>
</div>
```

**JavaScript**
```javascript
let box = document.getElementById("box");

let oldPara = document.getElementById("old");

let newPara = document.createElement("p");

newPara.innerText = "New Paragraph";

box.replaceChild(newPara, oldPara);
```

**Output**
```html
<div id="box">
    <p>New Paragraph</p>
</div>
```

**Explanation**
1. A new paragraph is created.
2. `replaceChild()` removes the old paragraph and inserts the new one.

---

## 7.20 DOM Navigation

DOM navigation allows JavaScript to move between related HTML elements.

### `parentElement`

**Definition**: Returns the parent element of the selected element.

```html
<div id="box">
    <p id="text">Hello</p>
</div>
```
```javascript
let text = document.getElementById("text");

console.log(text.parentElement);
```

**Output**
```html
<div id="box">
    <p id="text">Hello</p>
</div>
```

### `children`

**Definition**: Returns all child elements of an element as an HTMLCollection.

```javascript
let box = document.getElementById("box");

console.log(box.children);
```

**Output**
```
HTMLCollection(1)
```

### `firstElementChild`

**Definition**: Returns the first child element.

```javascript
console.log(box.firstElementChild);
```

**Output**
```html
<p id="text">Hello</p>
```

### `lastElementChild`

**Definition**: Returns the last child element.

```javascript
console.log(box.lastElementChild);
```

**Output**
```html
<p id="text">Hello</p>
```

### `nextElementSibling`

**Definition**: Returns the next sibling element.

**HTML**
```html
<h2 id="first">HTML</h2>
<h2 id="second">CSS</h2>
```

**JavaScript**
```javascript
let first = document.getElementById("first");

console.log(first.nextElementSibling);
```

**Output**
```html
<h2 id="second">CSS</h2>
```

### `previousElementSibling`

**Definition**: Returns the previous sibling element.

```javascript
let second = document.getElementById("second");

console.log(second.previousElementSibling);
```

**Output**
```html
<h2 id="first">HTML</h2>
```

---

## Real-Life Project Example

### HTML
```html
<!DOCTYPE html>
<html>
<head>
    <title>Student List</title>
</head>
<body>

    <h2>Students</h2>

    <ul id="studentList">
        <li>Rahul</li>
        <li>Amit</li>
    </ul>

    <button onclick="addStudent()">Add Student</button>

</body>
</html>
```

### JavaScript
```javascript
function addStudent(){
    let list = document.getElementById("studentList");

    let student = document.createElement("li");

    student.innerText = "Ritesh";

    list.appendChild(student);
}
```

**Output**

Initially:
```
Students
• Rahul
• Amit
```

After clicking "Add Student":
```
Students
• Rahul
• Amit
• Ritesh
```

**Explanation**
1. The button calls the `addStudent()` function.
2. A new `<li>` element is created.
3. `"Ritesh"` is added as its text.
4. `appendChild()` inserts it into the student list.

---

## Applications of DOM

1. Interactive websites.
2. Login and registration forms.
3. Shopping cart systems.
4. Online quizzes.
5. To-Do list applications.
6. Dynamic dashboards.
7. Chat applications.
8. E-commerce websites.
9. Content management systems.
10. Social media platforms.

---

## Advantages of DOM

1. Enables dynamic webpage updates.
2. Allows JavaScript to manipulate HTML and CSS.
3. Supports event-driven programming.
4. Improves user experience.
5. Makes websites interactive.
6. Easy integration with HTML and CSS.
7. Supports dynamic content creation.