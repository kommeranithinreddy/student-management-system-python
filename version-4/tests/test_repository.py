import unittest
import tempfile
from pathlib import Path

from storage import StudentRepository
from student import Student
from exceptions import StudentNotFoundError


class TestStudentRepository(unittest.TestCase):

    def setUp(self): #runs before each test
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = Path(self.temp_dir.name) / "test.db"
        self.repository = StudentRepository(self.db_path)

    def tearDown(self): #for cleanup #runs after each test
        self.repository.close()
        self.temp_dir.cleanup()


    def test_add_student(self):
        student = Student(None, "nithin", 23, "Data Science")

        self.repository.add_student(student)

        self.assertIsNotNone(student.sid)

    def test_get_student(self):
        student = Student(None, "nithin", 23, "Data Science")
        self.repository.add_student(student)

        result = self.repository.get_student(student.sid)

        self.assertEqual(result.name, student.name)
        self.assertEqual(result.age, student.age)
        self.assertEqual(result.course, student.course)
        self.assertEqual(result.sid, student.sid)

    def test_get_student_not_found(self):
        with self.assertRaises(StudentNotFoundError):
            self.repository.get_student(9999)

    def test_get_all_students(self):
        student1 = Student(None, "Nithin", 23, "Data Science")
        student2 = Student(None, "Sunny", 24, "Machine Learning")
        self.repository.add_student(student1)
        self.repository.add_student(student2)

        result = self.repository.get_all_students()

        self.assertEqual(len(result), 2)

    def test_update_student(self):
        student1 = Student(None, "Sunny", 22, "Data Science")

        self.repository.add_student(student1)
        self.repository.update_student(student1.sid, "Nithin", 23, "Machine Learning")

        result = self.repository.get_student(student1.sid)


        self.assertEqual(result.name, "Nithin")
        self.assertEqual(result.age, 23)
        self.assertEqual(result.course, "Machine Learning")


    def test_delete_student(self):
        student1 = Student(None, "Nithin", 23, "Data Science")

        self.repository.add_student(student1)
        self.repository.delete_student(student1.sid)

        with self.assertRaises(StudentNotFoundError):
            self.repository.get_student(student1.sid)


    def test_search_by_name(self):
        student1 = Student(None, "Nithin", 23, "Data Science")
        student2 = Student(None, "Sunny", 24, "Machine Learning")

        self.repository.add_student(student1)
        self.repository.add_student(student2)

        result = self.repository.search_by_name("Nithin")
        self.assertEqual(len(result), 1)


    def test_search_by_course(self):
        student1 = Student(None, "Nithin", 23, "Data Science")
        student2 = Student(None, "Sunny", 24, "Machine Learning")

        self.repository.add_student(student1)
        self.repository.add_student(student2)

        result = self.repository.search_by_course("Data")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].course, "Data Science")

    def test_search_by_name_not_found(self):
        student1 = Student(None, "Nithin", 23, "Data Science")
        self.repository.add_student(student1)

        with self.assertRaises(StudentNotFoundError):
            self.repository.search_by_name("Sunny")


if __name__ == "__main__":
    unittest.main()