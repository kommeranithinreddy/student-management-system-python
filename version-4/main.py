from pathlib import Path
import sqlite3

import logging_config
from student_service import StudentService
from storage import StudentRepository
import exceptions as e
from student import Student
from course import VALID_COURSES


path = Path("data") / "students.db"
path.parent.mkdir(parents=True, exist_ok=True)

repository = StudentRepository(path)
service = StudentService(repository)


while True:
    print('1 -- To add student')
    print('2 -- To view students')
    print('3 -- To search student')
    print('4 -- To update Student')
    print('5 -- To delete student')
    print('6 -- Export students to csv')
    print('7 -- Import students from csv')
    print('8 - Quit')
    option = input('Please select option to continue: ')
    if option == '1':
        try:
            name = input('Enter student name: ')
            age = int(input('Enter student age: '))
            print('Available Courses: ')
            for course in sorted(VALID_COURSES):
                print(f"- {course}")
            course = input('Enter Student course from the above list: ')
            student = Student(None, name, age, course)
            service.add_student(student)
            print(f'Student Created with ID : {student.sid}')
        except e.InvalidNameError:
            print('Invalid name - Please try again')
        except (e.InvalidAgeError, ValueError):
            print('Age should be integer and in range of 5 and 60')
        except e.InvalidCourseError:
            print('Invalid course - please add only valid courses')
        except sqlite3.Error:
            print("A database error occurred. Please try again.")


    elif option == '2':
        try:
            student_list = service.get_all_students()
            if student_list:
                for student in student_list:
                    print(student)
            else:
                print('No student data available')

        except sqlite3.Error:
            print("A database error occurred. Please try again")

    elif option == '3':
        print('1 -- Search by ID')
        print('2 -- Search by name')
        print('3 -- Search by course')
        search_option = input('Enter your option: ')
        if search_option == '1':
            try:
                sid = int(input('Enter Student ID: '))
                result = service.get_student(sid=sid)
                print(result)
            except e.StudentNotFoundError:
                print(f'No student available with ID : {sid}')
            except sqlite3.Error:
                print("A database error occurred. Please try again.")

        elif search_option == '2':
            try:
                name = input('Enter Student name: ')
                result = service.search_by_name(name)
                for student in result:
                    print(student)
            except e.StudentNotFoundError:
                print(f'No student available with name: {name}')
            except sqlite3.Error:
                print("A database error occurred. Please try again.")

        elif search_option == '3':
            try:
                course = input('Enter Course name: ')
                result = service.search_by_course(course)
                for student in result:
                    print(student)
            except e.StudentNotFoundError:
                print(f'No student available with course: {course}')
            except sqlite3.Error:
                print("A database error occurred. Please try again.")

    elif option == '4':
        try:
            sid = int(input('Enter Student ID to update: '))
            print('To update name : 1')
            print('To update age : 2')
            print('To update course : 3')
            opt = input('Enter your option: ')
            if opt == '1':
                new_name = input('Enter new name: ')
                service.update_student(sid, new_name=new_name)
                print('Student Updated Successfully')
            elif opt == '2':
                new_age = int(input('Enter new age: '))
                service.update_student(sid, new_age=new_age)
                print('Student Updated Successfully')
            elif opt == '3':
                new_course = input('Enter new course: ')
                service.update_student(sid, new_course=new_course)
                print('Student Updated Successfully')
            else:
                print('Invalid Input')
        except e.StudentNotFoundError:
            print(f'No student available with ID : {sid}')
        except e.InvalidNameError:
            print('Name consists only Alphabets in range of 3 to 10')
        except (e.InvalidAgeError, ValueError):
            print('Age should be integer and in range of 5 and 60')
        except e.InvalidCourseError:
            print('Course name should consists only Alphabets in range of 3 to 10')
        except sqlite3.Error:
            print("A database error occurred. Please try again.")

    elif option == '5':
        try:
            sid = int(input('Enter Student ID to delete: '))
            service.delete_student(sid)
            print('Student Deleted Successfully')
        except e.StudentNotFoundError:
            print(f'No student available with ID : {sid}')
        except sqlite3.Error:
            print("A database error occurred. Please try again.")

    elif option == '6':
        try:
            file_path = Path("data") / "students_export.csv"
            service.export_students(file_path)
            print(f"Students data exported successfully to {file_path}")

        except FileNotFoundError:
            print("csv file not found")
        except PermissionError:
            print("permission denied while accessing the csv file")
        except OSError:
            print(f"A error occurred. Please try again")


    elif option == '7':
        try:
            file_path = Path("data") / "students_import.csv"
            service.import_students(file_path)
            print("Students imported successfully")

        except FileNotFoundError:
            print("csv file not found")
        except PermissionError:
            print("permission denied while accessing the csv file")
        except (UnicodeDecodeError, ValueError, KeyError):
            print("Invalid CSV data.")

    elif option == '8':
        repository.close()
        break
    else:
        print('Invalid option')