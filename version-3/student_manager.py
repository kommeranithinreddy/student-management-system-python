from student import Student
from exceptions import StudentNotFoundError

class StudentManager:
    def __init__(self):
        self.__students = dict()
        self.__next_id = 2001

    def add_student(self, name, age, course):
        obj =  Student(self.__next_id, name, age, course)
        self.__students[self.__next_id] = obj
        self.__next_id += 1

    def load_students(self, student_list):
        highest_id = 2000
        for student in student_list:
            self.__students[student.get_sid()] = student

            if highest_id < student.get_sid():
                highest_id = student.get_sid()

        self.__next_id = highest_id + 1


    def get_all_students(self):
        return self.__students.values()

    def get_student(self, *, sid):
        if sid in self.__students:
            return self.__students[sid]
        else:
            raise StudentNotFoundError(f'No student available with ID : {sid}')


    def update_student(self, sid, new_name = None, new_age = None, new_course = None):
        std = self.get_student(sid=sid)
        std.update(new_name=new_name,
                   new_age=new_age,
                   new_course=new_course)

    def delete_student(self, sid):
        self.get_student(sid=sid)
        del self.__students[sid]


