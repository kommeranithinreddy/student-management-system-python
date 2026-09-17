# Student Management System

A console-based Student Management System built with Python.

This project was developed incrementally across four versions, with each
version focusing on improving Python programming, OOP, persistence,
architecture, and software engineering practices.

## Features

- Add student
- View all students
- View student by ID
- Update student
- Delete student
- Search students by name
- Search students by course
- Export students to CSV
- Import students from CSV
- Input validation
- Custom exceptions
- Logging
- SQLite database persistence
- Unit testing

## Technologies Used

- Python
- SQLite
- DB-API 2.0 (`sqlite3`)
- `unittest`
- CSV
- `pathlib`
- `logging`
- Regular expressions (`re`)
- Type hints

## Project Versions

### Version 1 — Basic CRUD

- List-based storage
- Basic OOP
- CRUD operations

### Version 2 — Improved OOP

- Dictionary-based storage
- Encapsulation
- Custom exceptions
- Improved code organization

### Version 3 — Maintainable Architecture

- Separation of responsibilities
- JSON persistence
- Serialization
- Repository-based storage

### Version 4 — SQLite & Software Engineering

V4 is the final version of the project.

Improvements include:

- SQLite database persistence
- DB-API 2.0
- Repository pattern
- Service layer
- Input validation
- Custom exceptions
- Search functionality
- CSV import/export
- Logging
- Type hints
- Unit tests

## Project Structure
```text
student-management-system-python/
│
├── version-1/
├── version-2/
├── version-3/
│
└── version-4/
    ├── tests/
    │   ├── __init__.py
    │   ├── test_student.py
    │   ├── test_repository.py
    │   ├── test_service.py
    │   └── test_csv_handler.py
    │
    ├── data/
    │
    ├── main.py
    ├── student.py
    ├── student_service.py
    ├── storage.py
    ├── exceptions.py
    ├── course.py
    ├── csv_handler.py
    ├── logging_config.py
    └── README.md

```

## Architecture

The application follows a simple layered structure:

User
  ↓
main.py
  ↓
StudentService
  ↓
StudentRepository
  ↓
SQLite Database

Student
└── Domain Model & Validation

The `Student` class acts as the domain model and handles student
data validation.

### Responsibilities

**main.py**
- Handles user interaction and menu operations.

**StudentService**
- Provides the application/service layer.
- Coordinates operations between the UI and repository.

**StudentRepository**
- Handles SQLite database operations.

**Student**
- Represents a student.
- Performs validation for name, age, and course.

**csv_handler.py**
- Handles CSV import and export.

**logging_config.py**
- Configures application logging.

## Database

Version 4 uses SQLite for persistent storage.

The database is automatically created when the application is started,
along with the required `students` table.

## Testing

Unit tests are written using Python's built-in `unittest` framework.

The project currently contains **20 unit tests**, covering:

- Student validation
- Student creation
- Repository CRUD operations
- Searching
- Service operations
- CSV export/import

All tests currently pass.

**20 tests — 20 passed — 0 failed** ✅

```text
Ran 20 tests

OK
```

## How to Run

1. Open the `version-4` folder.
2. Run `main.py`.
3. Follow the menu displayed in the console.

The SQLite database will be created inside the `data` folder.

## What I Learned

Through the four versions of this project, I practiced:

- Python fundamentals and advanced Python
- Object-oriented programming
- Encapsulation and properties
- Custom exceptions
- File handling
- JSON persistence
- SQLite and DB-API 2.0
- Repository and service layers
- CSV processing
- Logging
- Type hints
- Unit testing
- Writing maintainable Python code

## Project Status

**Completed — Version 4**

This project is complete. The main goal was to practice Python,
object-oriented programming, database persistence, software architecture,
logging, CSV processing, and unit testing.
