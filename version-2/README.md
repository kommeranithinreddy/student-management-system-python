# Student Management System - Version 2

## Overview

Version 2 is a major refactoring of Version 1.

The focus shifted from adding features to improving software design, code quality, exception handling, and maintainability while keeping the application console-based.

---

## Improvements over Version 1

### Architecture

- Better separation between business logic and user interface
- Cleaner responsibilities for each class

### Data Storage

- Replaced list with a dictionary
- Student ID mapped directly to Student objects
- Faster student lookup

### Exception Handling

Introduced a custom exception hierarchy:

- StudentError
- StudentNotFoundError
- InvalidNameError
- InvalidAgeError
- InvalidCourseError

Validation failures now raise exceptions instead of printing messages.

### Encapsulation

- Student attributes made private
- Updates performed through setter methods

### Validation

Validation includes:

- Name validation using Regular Expressions
- Course validation using Regular Expressions
- Age validation using range checking

### CRUD Improvements

- Cleaner method names
- Dedicated methods for retrieving students
- Simplified update and delete operations
- Removed searching by name

---

## Concepts Used

- Object-Oriented Programming
- Encapsulation
- Custom Exceptions
- Exception Handling
- Dictionary Data Structure
- Regular Expressions
- CRUD Operations
- Code Refactoring

---

## Data Storage

Student records are stored in a dictionary.

```
Student ID -> Student Object
```

---

## Version Goals

This version focuses on writing cleaner, more maintainable Python code by improving architecture instead of simply adding functionality.

It serves as the foundation for future versions that will introduce persistence, modularization, testing, and additional Python features.
