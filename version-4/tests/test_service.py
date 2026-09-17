import unittest
import tempfile
from pathlib import Path

from student_service import StudentService
from storage import StudentRepository
from student import Student
from exceptions import StudentNotFoundError


class TestStudentService(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = Path(self.temp_dir.name) / "test.db"

        self.repository = StudentRepository(self.db_path)
        self.service = StudentService(self.repository)

    def tearDown(self):
        self.repository.close()
        self.temp_dir.cleanup()


    def test_add_student(self):
        student = Student(None, "Nithin", 23, "Data Science")

        self.service.add_student(student)
        self.assertIsNotNone(student.sid)

    def test_get_student(self):
        student = Student(None, "Nithin", 23, "Data Science")
        self.service.add_student(student)
        result = self.service.get_student(sid = student.sid)

        self.assertEqual(student.sid, result.sid)
        self.assertEqual(result.name, student.name)
        self.assertEqual(result.age, student.age)
        self.assertEqual(result.course, student.course)

    def test_update_student(self):
        student = Student(None, "Sunny", 22, "Data Science")
        self.service.add_student(student)
        self.service.update_student(student.sid, "nithin", 23)

        result = self.service.get_student(sid = student.sid)

        self.assertEqual(result.name, "Nithin")
        self.assertEqual(result.age, 23)
        self.assertEqual(result.course, "Data Science")

    def test_delete_student(self):
        student = Student(None, "Nithin", 23, "Data Science")
        self.service.add_student(student)

        self.service.delete_student(student.sid)

        with self.assertRaises(StudentNotFoundError):
            self.service.get_student(sid = student.sid)








