import unittest

from exceptions import InvalidNameError, InvalidAgeError, InvalidCourseError

from student import Student

class TestStudent(unittest.TestCase):
    def test_valid_student(self):
        student = Student(None, "nithin reddy", 23, "Data Science")

        self.assertEqual(student.name, "Nithin Reddy")
        self.assertEqual(student.age, 23)
        self.assertEqual(student.course, "Data Science")
        self.assertIsNone(student.sid)

    def test_name_normalization(self):
        student =  Student(None, "  nIthin rEDdy", 23, "Data science")

        self.assertEqual(student.name, "Nithin Reddy")

    def test_invalid_name(self):
        with self.assertRaises(InvalidNameError):
            Student(None, "n", 23, "Data Science")

    def test_invalid_age(self):
        with self.assertRaises(InvalidAgeError):
            Student(None, "Nithin", 2, "Data Science")


    def test_invalid_course(self):
        with self.assertRaises(InvalidCourseError):
            Student(None, 'Nithin', 23, "Python")


if __name__ == "__main__":
    unittest.main()
