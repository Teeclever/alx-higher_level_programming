# 0x13 JavaScript - Objects, Scopes, and Closures

## Overview

This repository contains examples and explanations related to JavaScript concepts, specifically focusing on Objects, Scopes, and Closures. Whether you're a beginner looking to grasp the fundamentals or an experienced developer aiming to deepen your understanding, this resource aims to provide clarity on these crucial aspects of JavaScript.

## Table of Contents

- [Objects](#objects)
- [Scopes](#scopes)
- [Closures](#closures)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Objects

In JavaScript, objects are a fundamental data structure that allows you to store and organize data. This section covers the basics of creating and manipulating objects, understanding properties and methods, and exploring various object-related concepts.

### Example:

```javascript
// Creating an object
const person = {
  firstName: 'John',
  lastName: 'Doe',
  age: 30,
  getFullName: function() {
    return `${this.firstName} ${this.lastName}`;
  }
};

// Accessing object properties
console.log(person.firstName); // Output: John

// Calling object methods
console.log(person.getFullName()); // Output: John Doe
```