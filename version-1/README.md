# Student Management System - Version 1

## Overview

Version 1 is the initial implementation of the Student Management System.

The goal of this version was to practice Python classes, object-oriented programming, CRUD operations, and basic validation using a menu-driven console application.

---

## Features

- Add student
- View students
- Search by Student ID
- Search by Name
- Update student details
- Delete student
- Automatic Student ID generation

---

## Concepts Used

- Python Classes
- Objects
- Constructors
- Methods
- Encapsulation (partial)
- Regular Expressions
- Lists
- CRUD Operations

---

## Data Storage

Student records are stored in a Python list.

---

## Validation

Validation is performed inside the Student class using:

- Regular Expressions
- Conditional statements

Invalid input displays error messages using `print()`.

---

## Limitations

- Uses a list for storing students.
- Searching requires iterating through the list.
- Validation does not stop object creation.
- Uses print statements instead of exceptions.
- Business logic and user interface are tightly coupled.
- Search by name may return multiple students.

---

## Purpose

This version focuses on learning fundamental Python OOP concepts before introducing better software design practices.
