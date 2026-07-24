import re
class Student:
    def __init__(self, sid, name, age, course):
        self.sid = sid
        self.set_name(name)
        self.set_age(age)
        self.set_course(course)

    def set_name(self, name):
        if re.fullmatch(r'[a-zA-Z ]{3,10}', name):
            self.name = name
        else:
            print('Name should be in range of 3 to 10 and alphabet')
    def set_age(self, age):
        if 5<=age<60:
            self.__age = age
        else:
            print('Age should be in range of 5 and 60')
    def set_course(self, course):
        if re.fullmatch(r'\w{3,10}', course):
            self.__course = course
        else:
            print('Invalid course name >> please try again')

    def __repr__(self):
        return f'({self.sid}, {self.name}, {self.__age}, {self.__course})'

    def update(self, new_name = None, new_age=None, new_course = None):
        if new_name is not None:
            self.set_name(new_name)
        if new_age is not None:
            self.set_age(new_age)
        if new_course is not None:
            self.set_course(new_course)

    def display(self):
        return f'Student ID : {self.sid}\t Name : {self.name}\t Age : {self.__age}\t Course : {self.__course}'

class StudentManager:
    next_id = 2001
    def __init__(self):
        self.students = []
    def add_student(self, name, age, course):
        obj =  Student(self.next_id, name, age, course)
        self.students.append(obj)
        print('Student Created')
        print(f'Student ID : {self.next_id}')
        self.next_id += 1

    def view_students(self):
        if self.students:
            for student in self.students:
                print(student.display())
        else:
            print('No student is added')

    def search_student(self, *, sid = None, sname = None):
        if sid:
            for std in self.students:
                if sid == std.sid:
                    return std
            return None
        else:
            details = []
            for std in self.students:
                if sname == std.name:
                    details.append(std)
            return details

    def update_student(self, sid):
        std = self.search_student(sid=sid)
        if std is not None:
            while True:
                print('To update name : 1')
                print('To update age : 2')
                print('To update course : 3')
                print('To exit : 4')
                opt = input('Enter your option: ')

                if opt == '1':
                    new_name = input('Enter the new name to update: ')
                    std.update(new_name=new_name)
                    print('Student updated successfully')
                elif opt == '2':
                    new_age = int(input('Enter updated age: '))
                    std.update(new_age=new_age)
                    print('Student updated successfully')
                elif opt == '3':
                    new_course = input('Enter new course to update: ')
                    std.update(new_course=new_course)
                    print('Student updated successfully')
                elif opt == '4':
                    break
                else:
                    print('Invalid update please try again')
        else:
            print(f'{sid} is not available please try again')


    def delete_student(self, sid):
        std = self.search_student(sid=sid)
        if std:
            opt = input('Student found please confirm to delete: Y/N: ')
            if opt.lower() == 'y':
                self.students.remove(std)
                print('Student removed successfully')
            elif opt.lower() == 'n':
                print('Thanks for the confirmation')
            else:
                print('Invalid input, please try again')
        else:
            print(f'No student available with ID : {sid}')

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
        name = input('Enter student name: ')
        age = int(input('Enter student age: '))
        course = input('Enter Student course: ')
        manager.add_student(name, age, course)
    elif option == '2':
        manager.view_students()
    elif option == '3':
        opt = input('''
1 -- to search using Student ID. 
2 -- to search using Name
Enter: ''')
        if opt == '1':
            s_id = int(input('Enter Student ID: '))
            result = manager.search_student(sid = s_id)
            print(result)
        elif opt == '2':
            name = input('Enter Student Name: ')
            result = manager.search_student(sname = name)
            if result:
                for student in result:
                    print(student)
            else:
                print(None)
        else:
            print('Invalid Option - Please try again')

    elif option == '4':
        sid = int(input('Enter Student ID to update: '))
        manager.update_student(sid)
    elif option == '5':
        sid = int(input('Enter Student ID to delete: '))
        manager.delete_student(sid)

    elif option == '6':
        break
    else :
        print('Invalid option')