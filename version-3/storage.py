import json
from student import Student

class StorageJson:
    def __init__(self, filename):
        self.__filename = filename

    def save_students(self, student_objects):
        students_list = []
        for student in student_objects:
            students_list.append(student.to_dict())

        with open(self.__filename, 'w') as fobj:
            json.dump(students_list, fobj, indent = 4)


    def load_students(self):
        students_list = []
        try:
            with open(self.__filename, 'r') as fobj:
                json_list = json.load(fobj)

            for obj in json_list:
                student = Student.from_dict(obj)
                students_list.append(student)

            return students_list
        except (FileNotFoundError, json.JSONDecodeError):
            return []