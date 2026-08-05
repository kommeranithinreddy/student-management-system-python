from student_manager import StudentManager
import exceptions as e
from storage import StorageJson

json_storage = StorageJson('students.json')
manager = StudentManager()
students_list = json_storage.load_students()
manager.load_students(students_list)


while True:
    print('1 -- To add student')
    print('2 -- To view students')
    print('3 -- To search student')
    print('4 -- To update Student')
    print('5 -- To delete student')
    print('6 - Quit')
    option = input('Please select option to continue: ')
    if option == '1':
        try:
            name = input('Enter student name: ')
            age = int(input('Enter student age: '))
            course = input('Enter Student course: ')
            manager.add_student(name, age, course)
            json_storage.save_students(manager.get_all_students())
            print('Student Created')
        except e.InvalidNameError:
            print('Name consists only Alphabets in range of 3 to 10')
        except (e.InvalidAgeError, ValueError):
            print('Age should be integer and in range of 5 and 60')
        except e.InvalidCourseError:
            print('Course name should consists only Alphabets in range of 3 to 10')
    elif option == '2':
        student_list = manager.get_all_students()
        if student_list:
            for student in student_list:
                print(student)
        else:
            print('No student data available')
    elif option == '3':
        try:
            sid = int(input('Enter Student ID: '))
            result = manager.get_student(sid=sid)
            print(result)
        except e.StudentNotFoundError:
            print(f'No student available with ID : {sid}')

    elif option == '4':
        try:
            sid = int(input('Enter Student ID to update: '))
            print('To update name : 1')
            print('To update age : 2')
            print('To update course : 3')
            opt = input('Enter your option: ')
            if opt == '1':
                new_name = input('Enter new name: ')
                manager.update_student(sid, new_name=new_name)
                json_storage.save_students(manager.get_all_students())
                print('Student Updated Successfully')
            elif opt == '2':
                new_age = int(input('Enter new age: '))
                manager.update_student(sid, new_age=new_age)
                json_storage.save_students(manager.get_all_students())
                print('Student Updated Successfully')
            elif opt == '3':
                new_course = input('Enter new course: ')
                manager.update_student(sid, new_course=new_course)
                json_storage.save_students(manager.get_all_students())
                print('Student Updated Successfully')
            else:
                print('Invalid Input')
        except e.StudentNotFoundError:
            print(f'No student available with ID : {sid}')
        except e.InvalidNameError:
            print('Name consists only Alphabets in range of 3 to 10')
        except e.InvalidAgeError, ValueError:
            print('Age should be integer and in range of 5 and 60')
        except e.InvalidCourseError:
            print('Course name should consists only Alphabets in range of 3 to 10')

    elif option == '5':
        try:
            sid = int(input('Enter Student ID to delete: '))
            manager.delete_student(sid)
            json_storage.save_students(manager.get_all_students())
            print('Student Deleted Successfully')
        except e.StudentNotFoundError:
            print(f'No student available with ID : {sid}')
    elif option == '6':
        json_storage.save_students(manager.get_all_students())
        break
    else:
        print('Invalid option')