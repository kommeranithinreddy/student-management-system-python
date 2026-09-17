from pathlib import Path

from csv_handler import export_students as export_students_from_csv, import_students as import_students_from_csv
from storage import StudentRepository
from student import Student


class StudentService:
    def __init__(self, repository: StudentRepository):
        self.__repository = repository

    def add_student(self, student : Student) -> None:
        self.__repository.add_student(student)

    def get_all_students(self) -> list[Student]:
        return self.__repository.get_all_students()

    def get_student(self, *, sid : int) -> Student:
        return self.__repository.get_student(sid)

    def update_student(
            self,
            sid : int,
            new_name : str | None = None,
            new_age : int | None = None,
            new_course : str | None = None
    ) -> None:

        current_student = self.get_student(sid=sid)

        name = new_name if new_name is not None else current_student.name
        age =  new_age if new_age is not None else current_student.age
        course = new_course if new_course is not None else current_student.course

        updated_student = Student(sid, name, age, course) # only for validations.

        self.__repository.update_student(
            sid,
            name,
            age,
            course
        )

    def delete_student(self, sid : int) -> None:
        self.get_student(sid=sid)
        self.__repository.delete_student(sid)

    def search_by_name(self, name : str) -> list[Student]:
        return self.__repository.search_by_name(name)

    def search_by_course(self, course : str) -> list[Student]:
        return self.__repository.search_by_course(course)

    def export_students(self, file_path : Path) -> None:
        students = self.get_all_students()
        export_students_from_csv(students, file_path)

    def import_students(self, file_path : Path) -> None:
        students = import_students_from_csv(file_path)

        for student in students:
            self.add_student(student)





