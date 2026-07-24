import re

class StudentError(Exception):
    pass

class StudentNotFoundError(StudentError):
    pass

class InvalidAgeError(StudentError):
    pass

class InvalidNameError(StudentError):
    pass

class InvalidCourseError(StudentError):
    pass


class Student:
    def __init__(self, sid, name, age, course):
        self.__sid = sid
        self.set_name(name)
        self.set_age(age)
        self.set_course(course)

    def set_name(self, name):
        if re.fullmatch(r'[a-zA-Z ]{3,10}', name):
            self.__name = name
        else:
            raise InvalidNameError('Name should be in range of 3 to 10 and alphabet')
    def set_age(self, age):
        if 5<=age<60:
            self.__age = age
        else:
            raise InvalidAgeError('Age should be in range of 5 and 60')
    def set_course(self, course):
        if re.fullmatch(r'[a-zA-Z]{3,10}', course):
            self.__course = course
        else:
            raise InvalidCourseError('Course name should consists only Alphabets in range of 3 to 10')

    def __str__(self):
        return f'Student ID : {self.__sid}\t Name : {self.__name}\t Age : {self.__age}\t Course : {self.__course}'

    def update(self, new_name = None, new_age=None, new_course = None):
        if new_name is not None:
            self.set_name(new_name)
        if new_age is not None:
            self.set_age(new_age)
        if new_course is not None:
            self.set_course(new_course)

class StudentManager:
    def __init__(self):
        self.students = dict()
        self.next_id = 2001

    def add_student(self, name, age, course):
        obj =  Student(self.next_id, name, age, course)
        self.students[self.next_id] = obj
        print('Student Created')
        print(f'Student ID : {self.next_id}')
        self.next_id += 1

    def get_all_students(self):
        return self.students.values()

    def get_student(self, *, sid):
        if sid in self.students:
            return self.students[sid]
        else:
            raise StudentNotFoundError(f'No student available with ID : {sid}')


    def update_student(self, sid, new_name = None, new_age = None, new_course = None):
        std = self.get_student(sid=sid)
        std.update(new_name=new_name,
                   new_age=new_age,
                   new_course=new_course)

    def delete_student(self, sid):
        self.get_student(sid=sid)
        del self.students[sid]


manager = StudentManager()


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
        except InvalidNameError:
            print('Name consists only Alphabets in range of 3 to 10')
        except (InvalidAgeError, ValueError):
            print('Age should be integer and in range of 5 and 60')
        except InvalidCourseError:
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
        except StudentNotFoundError:
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
                print('Student Updated Successfully')
            elif opt == '2':
                new_age = int(input('Enter new age: '))
                manager.update_student(sid, new_age=new_age)
                print('Student Updated Successfully')
            elif opt == '3':
                new_course = input('Enter new course: ')
                manager.update_student(sid, new_course=new_course)
                print('Student Updated Successfully')
            else:
                print('Invalid Input')
        except StudentNotFoundError:
            print(f'No student available with ID : {sid}')
        except InvalidNameError:
            print('Name consists only Alphabets in range of 3 to 10')
        except InvalidAgeError, ValueError:
            print('Age should be integer and in range of 5 and 60')
        except InvalidCourseError:
            print('Course name should consists only Alphabets in range of 3 to 10')

    elif option == '5':
        try:
            sid = int(input('Enter Student ID to delete: '))
            manager.delete_student(sid)
            print('Student Deleted Successfully')
        except StudentNotFoundError:
            print(f'No student available with ID : {sid}')
    elif option == '6':
        break
    else:
        print('Invalid option')