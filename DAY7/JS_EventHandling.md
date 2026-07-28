# 8. Event Handling – Part 1

## Introduction

**Event Handling** is the process of responding to user actions on a webpage using JavaScript. An **event** is any action performed by the user or the browser, such as clicking a button, pressing a key, moving the mouse, submitting a form, or loading a page.

JavaScript allows developers to detect these events and execute specific code in response, making web pages interactive and dynamic.

For example:

1. Clicking a button displays a message.
2. Typing in a textbox validates input.
3. Moving the mouse changes an image.
4. Submitting a form checks whether all required fields are filled.

## Why Do We Use Event Handling?

Event handling is used to:

1. Respond to user actions.
2. Create interactive websites.
3. Validate forms.
4. Improve user experience.
5. Control webpage behavior dynamically.

## Advantages of Event Handling

1. Makes websites interactive.
2. Improves user experience.
3. Supports dynamic content.
4. Reduces manual page refreshes.
5. Enables real-time responses.

## Types of Events in JavaScript

JavaScript supports many types of events, including:

1. Mouse Events
2. Keyboard Events
3. Form Events
4. Window Events
5. Clipboard Events
6. Drag and Drop Events

Some commonly used events are:

1. `onclick`
2. `ondblclick`
3. `onmouseover`
4. `onmouseout`
5. `onkeydown`
6. `onkeyup`
7. `onsubmit`

---

## 8.1 `onclick` Event

### Definition
The `onclick` event occurs when the user clicks on an HTML element.

It is one of the most commonly used events in JavaScript.

### Syntax
```html
<button onclick="functionName()">Click</button>
```

### Practical Example

**HTML**
```html
<button onclick="showMessage()">Click Me</button>
```

**JavaScript**
```javascript
function showMessage(){
    alert("Welcome to JavaScript!");
}
```

**Output**

When the button is clicked:
```
Welcome to JavaScript!
```

**Explanation**
1. The button is clicked.
2. `showMessage()` is called.
3. `alert()` displays a popup message.

### Applications
1. Login buttons.
2. Submit buttons.
3. Menu buttons.

---

## 8.2 `ondblclick` Event

### Definition
The `ondblclick` event occurs when the user double-clicks an element.

### Syntax
```html
<button ondblclick="changeText()">Double Click</button>
```

### Practical Example

**HTML**
```html
<h2 id="heading">Hello</h2>

<button ondblclick="changeText()">Double Click</button>
```

**JavaScript**
```javascript
function changeText(){
    document.getElementById("heading").innerText = "Welcome";
}
```

**Output**

Initially:
```
Hello
```

After double-click:
```
Welcome
```

**Explanation**
1. Double-clicking the button changes the heading text.

### Applications
1. Edit mode.
2. Opening files.
3. Image zoom.

---

## 8.3 `onmouseover` Event

### Definition
The `onmouseover` event occurs when the mouse pointer moves over an element.

### Syntax
```javascript
element.onmouseover
```

### Practical Example

**HTML**
```html
<h2 id="title">Move Mouse Here</h2>
```

**JavaScript**
```javascript
document.getElementById("title").onmouseover = function(){
    this.style.color = "red";
};
```

**Output**

When the mouse moves over the heading:
1. Text color changes to red.

**Explanation**
1. Mouse enters the heading.
2. JavaScript changes the text color.

### Applications
1. Hover effects.
2. Tooltips.
3. Menu highlighting.

---

## 8.4 `onmouseout` Event

### Definition
The `onmouseout` event occurs when the mouse pointer leaves an element.

### Practical Example
```javascript
document.getElementById("title").onmouseout = function(){
    this.style.color = "black";
};
```

**Output**

When the mouse leaves:
1. Text color returns to black.

### Applications
1. Reset hover effects.
2. Navigation menus.
3. Image galleries.

---

## 8.5 `onkeydown` Event

### Definition
The `onkeydown` event occurs when a keyboard key is pressed.

### Syntax
```html
<input onkeydown="display()">
```

### Practical Example

**HTML**
```html
<input type="text" onkeydown="typing()">
```

**JavaScript**
```javascript
function typing(){
    console.log("Key Pressed");
}
```

**Output**

Whenever a key is pressed:
```
Key Pressed
```

**Explanation**
1. Every key press triggers the event.
2. The function executes immediately.

### Applications
1. Search suggestions.
2. Keyboard shortcuts.
3. Game controls.

---

## 8.6 `onkeyup` Event

### Definition
The `onkeyup` event occurs when the user releases a keyboard key.

### Practical Example

**HTML**
```html
<input type="text" onkeyup="showText()">

<p id="output"></p>
```

**JavaScript**
```javascript
function showText(){
    let value = document.querySelector("input").value;

    document.getElementById("output").innerText = value;
}
```

**Output**

Typing:
```
JavaScript
```

Displays:
```
JavaScript
```

**Explanation**
1. After every key release, the input value is read.
2. The paragraph updates instantly.

### Applications
1. Live search.
2. Password strength checker.
3. Character counter.

---

## 8.7 `onsubmit` Event

### Definition
The `onsubmit` event occurs when a form is submitted.

It is mainly used for form validation.

### Syntax
```html
<form onsubmit="validateForm()">
```

### Practical Example

**HTML**
```html
<form onsubmit="return validate()">
    <input type="text" id="name">
    <input type="submit">
</form>
```

**JavaScript**
```javascript
function validate(){
    let name = document.getElementById("name").value;

    if(name==""){
        alert("Name Required");
        return false;
    }

    return true;
}
```

**Output**

If the textbox is empty:
```
Name Required
```

**Explanation**
1. Before the form submits, `validate()` runs.
2. If the field is empty, submission is cancelled.
3. Otherwise, the form submits successfully.

### Applications
1. Registration forms.
2. Login forms.
3. Payment forms.

---

## Real-Life Example

### HTML
```html
<h2 id="message">Welcome</h2>

<button onclick="changeColor()">Click Me</button>
```

### JavaScript
```javascript
function changeColor(){
    let heading = document.getElementById("message");

    heading.style.color = "blue";
    heading.innerText = "Button Clicked";
}
```

**Output**

Initially:
```
Welcome
```

After clicking the button:
```
Button Clicked
```

The text color changes to blue.

**Explanation**
1. Clicking the button triggers the `changeColor()` function.
2. The function selects the heading using `getElementById()`.
3. It changes the text content and updates the text color, demonstrating how event handling can dynamically modify webpage content.

---

## Conclusion (Part 1)

In this section, we learned the basics of JavaScript Event Handling and explored common events such as:

1. `onclick`
2. `ondblclick`
3. `onmouseover`
4. `onmouseout`
5. `onkeydown`
6. `onkeyup`
7. `onsubmit`

These events allow JavaScript to respond to user interactions, making web pages more dynamic, interactive, and user-friendly.

# 8. Event Handling – Part 2

## 8.8 `addEventListener()` Method

### Definition
The `addEventListener()` method is the modern and recommended way to attach events to HTML elements. Unlike inline event handlers (`onclick`), it allows multiple event listeners to be attached to the same element without overwriting existing ones.

### Syntax
```javascript
element.addEventListener("event", functionName);

// or

element.addEventListener("event", function(){
    // Code to execute
});
```

### Practical Example

**HTML**
```html
<button id="btn">Click Me</button>
```

**JavaScript**
```javascript
let button = document.getElementById("btn");

button.addEventListener("click", function(){
    alert("Button Clicked!");
});
```

**Output**

When the button is clicked:
```
Button Clicked!
```

**Explanation**
1. The button is selected using `getElementById()`.
2. `addEventListener()` listens for the `"click"` event.
3. When clicked, the anonymous function executes and displays an alert.

### Advantages over `onclick`
1. Multiple event listeners can be added.
2. Cleaner code.
3. Better separation of HTML and JavaScript.
4. Easy to remove events later.

### Applications
1. Buttons
2. Forms
3. Menus
4. Interactive applications

---

## 8.9 Event Object

### Definition
Whenever an event occurs, JavaScript automatically creates an **Event Object**. This object contains information about the event, such as:

1. Event type
2. Target element
3. Mouse position
4. Keyboard key pressed
5. Timestamp

### Syntax
```javascript
element.addEventListener("click", function(event){

});
```

### Practical Example
```html
<button id="btn">Click</button>
```
```javascript
let btn = document.getElementById("btn");

btn.addEventListener("click", function(event){
    console.log(event.type);
    console.log(event.target);
});
```

**Output**
```
click
<button id="btn">Click</button>
```

**Explanation**
1. `event.type` returns `"click"`.
2. `event.target` returns the clicked HTML element.

### Common Event Object Properties

| Property | Description |
|---|---|
| `event.type` | Type of event |
| `event.target` | Element that triggered the event |
| `event.key` | Key pressed on keyboard |
| `event.clientX` | Mouse X position |
| `event.clientY` | Mouse Y position |

---

## 8.10 `preventDefault()` Method

### Definition
The `preventDefault()` method prevents the browser's default behavior for an event.

For example:
1. Prevent form submission.
2. Prevent opening a hyperlink.
3. Prevent page refresh.

### Syntax
```javascript
event.preventDefault();
```

### Practical Example

**HTML**
```html
<a href="https://google.com" id="link">Google</a>
```

**JavaScript**
```javascript
let link = document.getElementById("link");

link.addEventListener("click", function(event){
    event.preventDefault();
    alert("Navigation Blocked");
});
```

**Output**
```
Navigation Blocked
```

The browser does not open Google.

**Explanation**
1. Clicking the link normally opens another page.
2. `preventDefault()` stops the default navigation.
3. Only the alert is displayed.

### Applications
1. Form validation.
2. Prevent accidental navigation.
3. Custom button behavior.

---

## 8.11 `stopPropagation()` Method

### Definition
The `stopPropagation()` method stops an event from propagating (moving) to parent elements.

### Syntax
```javascript
event.stopPropagation();
```

### Practical Example

**HTML**
```html
<div id="parent">
    <button id="child">Click</button>
</div>
```

**JavaScript**
```javascript
document.getElementById("parent").addEventListener("click", function(){
    alert("Parent Clicked");
});

document.getElementById("child").addEventListener("click", function(event){
    event.stopPropagation();
    alert("Button Clicked");
});
```

**Output**

Clicking the button shows:
```
Button Clicked
```

The parent alert does not appear.

**Explanation**
1. The button event executes.
2. `stopPropagation()` stops the event from reaching the parent element.

---

## 8.12 Event Bubbling

### Definition
Event Bubbling is the default event flow in JavaScript. The event starts from the target element and then moves upward through its parent elements.

### Example

**HTML**
```html
<div id="parent">
    <button id="child">Click</button>
</div>
```

**JavaScript**
```javascript
document.getElementById("parent").addEventListener("click", function(){
    console.log("Parent");
});

document.getElementById("child").addEventListener("click", function(){
    console.log("Child");
});
```

**Output**

When clicking the button:
```
Child
Parent
```

**Explanation**
1. First, the button's event executes.
2. Then, the event bubbles up to the parent `<div>`.

---

## 8.13 Event Capturing

### Definition
Event Capturing is the opposite of event bubbling. The event starts from the outermost parent and moves inward toward the target element.

To enable capturing, pass `true` as the third argument of `addEventListener()`.

### Syntax
```javascript
element.addEventListener("click", function(){

}, true);
```

### Practical Example
```javascript
document.getElementById("parent").addEventListener("click", function(){
    console.log("Parent");
}, true);

document.getElementById("child").addEventListener("click", function(){
    console.log("Child");
}, true);
```

**Output**
```
Parent
Child
```

**Explanation**
1. Parent executes first.
2. Then the child executes.

---

## Difference Between Bubbling and Capturing

| Event Bubbling | Event Capturing |
|---|---|
| Bottom → Top | Top → Bottom |
| Default behavior | Enabled using `true` |
| Child executes first | Parent executes first |

---

## Real-Life Example

### HTML
```html
<button id="btn">Show Date</button>

<p id="result"></p>
```

### JavaScript
```javascript
let button = document.getElementById("btn");

button.addEventListener("click", function(){
    document.getElementById("result").innerText = new Date();
});
```

**Output**

Initially:
```
Show Date
```

After clicking:
```
(current date and time are displayed)
```

**Explanation**
1. The button listens for a click event using `addEventListener()`.
2. When clicked, the callback function executes.
3. `new Date()` generates the current date and time, which is displayed inside the paragraph.

# 8. Event Handling – Part 3 (Final)

## 8.14 Event Delegation

### Definition
Event Delegation is a technique in JavaScript where a single event listener is attached to a parent element instead of attaching event listeners to multiple child elements.

It works because of event bubbling. When a child element is clicked, the event bubbles up to the parent, where it can be handled.

### Why Use Event Delegation?
1. Reduces memory usage.
2. Improves performance.
3. Works for dynamically added elements.
4. Makes code cleaner and easier to maintain.

### Syntax
```javascript
parentElement.addEventListener("click", function(event){
    if(event.target.tagName === "LI"){
        // Code
    }
});
```

### Practical Example

**HTML**
```html
<ul id="fruits">
    <li>Apple</li>
    <li>Mango</li>
    <li>Banana</li>
</ul>
```

**JavaScript**
```javascript
let list = document.getElementById("fruits");

list.addEventListener("click", function(event){
    if(event.target.tagName === "LI"){
        alert(event.target.innerText);
    }
});
```

**Output**

Clicking Apple:
```
Apple
```

Clicking Mango:
```
Mango
```

**Explanation**
1. Only one event listener is attached to `<ul>`.
2. Clicking any `<li>` triggers the parent listener.
3. `event.target` identifies which list item was clicked.

### Applications
1. Dynamic menus.
2. To-Do Lists.
3. Shopping carts.
4. Chat applications.

---

## 8.15 `removeEventListener()` Method

### Definition
The `removeEventListener()` method removes an event listener that was previously added using `addEventListener()`.

### Syntax
```javascript
element.removeEventListener("event", functionName);
```

### Practical Example

**HTML**
```html
<button id="btn">Click Me</button>
```

**JavaScript**
```javascript
let button = document.getElementById("btn");

function message(){
    alert("Button Clicked");
}

button.addEventListener("click", message);

// Remove the event
button.removeEventListener("click", message);
```

**Output**

Clicking the button:
```
No output
```

**Explanation**
1. The event listener is added.
2. It is immediately removed.
3. Clicking the button does nothing because the listener no longer exists.

### Applications
1. Disable buttons after one click.
2. Stop timers.
3. Remove temporary events.
4. Improve application performance.

---

## Complete Event Handling Project

### HTML
```html
<!DOCTYPE html>
<html>
<head>
<title>Event Handling Demo</title>
</head>
<body>

<h2 id="heading">Welcome</h2>
<button id="btn">Change Text</button>

</body>
</html>
```

### JavaScript
```javascript
let button = document.getElementById("btn");

button.addEventListener("click", function(){
    let heading = document.getElementById("heading");

    heading.innerText = "JavaScript Event Handling";
    heading.style.color = "blue";
    heading.style.fontSize = "35px";
});
```

**Output**

Initially:
```
Welcome
```

After clicking the button:
```
JavaScript Event Handling
```

The heading changes:
1. Color → Blue
2. Font Size → 35px

**Explanation**
1. The button is selected using `getElementById()`.
2. `addEventListener()` listens for the click event.
3. When clicked:
   - The heading text changes.
   - The text color becomes blue.
   - The font size increases to 35px.

This example demonstrates how event handling can dynamically update webpage content and styling.

---

## Applications of Event Handling

Event handling is widely used in:

1. Login forms.
2. Registration forms.
3. Online shopping websites.
4. Banking applications.
5. Social media platforms.
6. Online quizzes.
7. Games.
8. Chat applications.
9. Image galleries.
10. Dashboards.

---

## Advantages of Event Handling

1. Makes web pages interactive.
2. Improves user experience.
3. Supports dynamic content updates.
4. Enables real-time responses.
5. Reduces unnecessary page reloads.
6. Easy integration with the DOM.
7. Supports complex user interactions.

---

## Disadvantages of Event Handling

1. Too many event listeners can reduce performance.
2. Complex event flows can make debugging difficult.
3. Improper event handling may cause memory leaks.
4. Event propagation can sometimes lead to unexpected behavior if not managed correctly.

---

## Summary of Common JavaScript Events

| Event | Description |
|---|---|
| `onclick` | Triggered when an element is clicked |
| `ondblclick` | Triggered when an element is double-clicked |
| `onmouseover` | Triggered when the mouse enters an element |
| `onmouseout` | Triggered when the mouse leaves an element |
| `onkeydown` | Triggered when a key is pressed |
| `onkeyup` | Triggered when a key is released |
| `onsubmit` | Triggered when a form is submitted |
| `addEventListener()` | Attaches one or more event handlers |
| `removeEventListener()` | Removes an event handler |
| `preventDefault()` | Prevents the browser's default behavior |
| `stopPropagation()` | Stops event propagation |
| Event Bubbling | Event flows from child to parent |
| Event Capturing | Event flows from parent to child |
| Event Delegation | Parent handles events for child elements |

---

## Real-Life Example – To-Do List

### HTML
```html
<input type="text" id="task" placeholder="Enter Task">

<button id="addBtn">Add Task</button>

<ul id="taskList"></ul>
```

### JavaScript
```javascript
let addButton = document.getElementById("addBtn");

addButton.addEventListener("click", function(){
    let task = document.getElementById("task").value;

    let li = document.createElement("li");
    li.innerText = task;

    document.getElementById("taskList").appendChild(li);

    document.getElementById("task").value = "";
});
```

**Output**

If the user types:
```
Study JavaScript
```

After clicking "Add Task", the webpage displays:
```
• Study JavaScript
```

**Explanation**
1. The user enters a task.
2. Clicking "Add Task" triggers the click event.
3. A new `<li>` element is created.
4. The task is added to the list using `appendChild()`.
5. The input field is cleared for the next task.

---

## Final Conclusion

Event Handling is one of the most important concepts in JavaScript because it allows web pages to respond to user interactions such as clicks, keyboard input, mouse movements, and form submissions. By using events like `onclick`, `onkeyup`, `onsubmit`, and methods such as `addEventListener()`, `removeEventListener()`, `preventDefault()`, and `stopPropagation()`, developers can build responsive, interactive, and user-friendly applications.

Combined with the DOM, event handling enables developers to create dynamic web applications such as online shopping websites, social media platforms, banking systems, dashboards, games, and real-time chat applications.

