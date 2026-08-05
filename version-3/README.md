# Student Management System - Version 3

A command-line Student Management System built in Python to practice Object-Oriented Programming, software design, and JSON persistence.

## Purpose

This project was built to practice designing maintainable software using Object-Oriented Programming rather than focusing only on CRUD functionality. The emphasis is on separation of responsibilities, persistence, serialization, and clean project structure.

## Features

- Add a student
- View all students
- Search a student by ID
- Update student details
- Delete a student
- Automatic data loading on startup
- Automatic data saving after every modification
- Custom exception handling
- Input validation
- JSON-based persistent storage

---

## Project Structure

```
student_management/
│
├── main.py
├── student.py
├── student_manager.py
├── storage.py
├── exceptions.py
├── students.json
└── README.md
```

### Responsibilities

- **Student**
  - Represents a student object
  - Performs data validation
  - Converts itself to and from dictionaries

- **StudentManager**
  - Manages student objects
  - Performs CRUD operations
  - Maintains unique student IDs

- **StorageJson**
  - Saves student data to JSON
  - Loads student data from JSON

- **main**
  - Handles user interaction
  - Coordinates StudentManager and StorageJson

- **exceptions**
  - Contains custom exception classes

---

## Concepts Practiced

### Python

- Classes and Objects
- Modules and Packages
- File Handling
- JSON
- Regular Expressions
- Custom Exceptions
- Class Methods

### Object-Oriented Programming

- Encapsulation
- Single Responsibility Principle
- Separation of Concerns
- Object Ownership

### Software Design

- Layered Architecture
- Serialization (`to_dict`)
- Deserialization (`from_dict`)
- Persistence
- Data Validation
- Error Handling

---

## Project Workflow

```
Application Starts
        │
        ▼
Load students from JSON
        │
        ▼
Create Student objects
        │
        ▼
Load into StudentManager
        │
        ▼
Display Menu
        │
        ▼
Perform CRUD Operations
        │
        ▼
Automatically Save Changes
```

---

## Future Improvements

- SQLite database support
- CSV import/export
- Search by name and course
- Unit testing
- Logging
- Type hints
- Properties (`@property`)
- Graphical User Interface (GUI)

---

## How to Run

```bash
python main.py
```

---

## Version

Current Version: **v3.0.0**

This version focuses on learning software architecture, object-oriented programming, and persistent data storage using JSON.
