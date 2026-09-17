import sqlite3
from pathlib import Path
import logging


from student import Student
from exceptions import StudentNotFoundError


logger = logging.getLogger(__name__)

class StudentRepository:
    def __init__(self, db_path : Path):
        self.connection : sqlite3.Connection = sqlite3.connect(db_path)
        cursor = self.connection.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS students(
        sid INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        course TEXT NOT NULL);
        ''')

        cursor.execute('''
        SELECT COUNT(*) FROM sqlite_sequence
        WHERE name = 'students'
        ''')

        sequence_exists = cursor.fetchone()[0]

        if not sequence_exists: #This makes the ID generation continue even if we delete all rows in student table.
            cursor.execute('''
                    INSERT INTO sqlite_sequence(name, seq)
                    VALUES ('students', 2000)
                    ''')

        self.connection.commit()

    def add_student(self, student : Student) -> None:
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                    INSERT INTO  students(name, age, course)
                    VALUES (?, ?, ?);''', (student.name, student.age, student.course))

            self.connection.commit()
            student.sid = cursor.lastrowid  # To get id and assign it to Student

            logger.info(f"Student {student.sid} added successfully")

        except sqlite3.Error as error:
            logger.error(f"Database error while adding student {error}")
            raise

    def get_student(self, sid : int) -> Student:
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                    SELECT * FROM students
                    WHERE sid = ?;''', (sid,))
            row = cursor.fetchone()
            if row is not None:
                return Student(*row)

            logger.warning(
                f"Attempted to retrieve non-existent student {sid}"
            )
            raise StudentNotFoundError(
                f'No student available with ID : {sid}'
            )

        except sqlite3.Error as error:
            logger.error(
                f"Database error while retrieving student {sid} : {error}"
            )
            raise


    def get_all_students(self) -> list[Student]:
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                    SELECT * FROM students''')
            rows = cursor.fetchall()
            result = []
            for row in rows:
                student = Student(*row)
                result.append(student)

            return result

        except sqlite3.Error as error:
            logger.error(
                f"Database error while retrieving all students {error}"
            )
            raise

    def update_student(self, sid : int, name : str, age : int, course : str) -> None:
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                    UPDATE students
                    SET name = ?, age = ?, course = ?
                    WHERE sid = ?;''', (name, age, course, sid))

            if cursor.rowcount == 0:
                logger.warning(f"Attempted to update non-existent student {sid}")
                raise StudentNotFoundError(f'No Student found with ID : {sid}')

            self.connection.commit()
            logger.info(f"Student {sid} updated successfully")

        except sqlite3.Error as error:
            logger.error(f"Database error while updating student {sid} : {error}")
            raise

    def delete_student(self, sid : int) -> None:
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                    DELETE FROM students
                    WHERE sid = ?;''', (sid,))

            if cursor.rowcount == 0:
                logger.warning(f"Attempted to delete non-existent student {sid}")
                raise StudentNotFoundError(f'No Student found with ID : {sid}')

            self.connection.commit()
            logger.info(f"Student {sid} deleted successfully")

        except sqlite3.Error as error:
            logger.error(f"Database error while deleting the student {sid} : {error}")
            raise

    def search_by_name(self, name : str) -> list[Student]:
        try:
            cursor = self.connection.cursor()

            cursor.execute('''
                    SELECT * FROM students
                    WHERE name LIKE ?;''', (f'%{name}%',))

            rows = cursor.fetchall()

            if not rows:
                logger.warning(
                    f"No Students found matching name : {name}"
                )
                raise StudentNotFoundError(f'No student available with name : {name}')

            result = []
            for row in rows:
                result.append(Student(*row))

            return result

        except sqlite3.Error as error:
            logger.error(
                f"Database error while searching by name '{name}' : {error}"
            )
            raise

    def search_by_course(self, course : str) -> list[Student]:
        try:
            cursor = self.connection.cursor()

            cursor.execute('''
                    SELECT * FROM students
                    WHERE course LIKE ?;''', (f'%{course}%',))

            rows = cursor.fetchall()

            if not rows:
                logger.warning(
                    f"No student found matching course name : {course}"
                )
                raise StudentNotFoundError(f'No student available with course : {course}')

            result = []
            for row in rows:
                result.append(Student(*row))

            return result

        except sqlite3.Error as error:
            logger.error(
                f"Database error while searching by course '{course}' : {error}"
            )
            raise

    def close(self) -> None:
        self.connection.close()