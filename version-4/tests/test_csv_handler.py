import unittest
import tempfile
from pathlib import Path
import csv

from csv_handler import export_students, import_students
from student import Student

class TestCSVHandler(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.file_path = Path(self.temp_dir.name) / "students.csv"

    def tearDown(self):
        self.temp_dir.cleanup()


    def test_export_students(self):
        student1 = Student(None, "Nithin", 23, "Data Science")
        student2 = Student(None, "Sunny", 24, "Machine Learning")

        students = [student1, student2]

        export_students(students, self.file_path)

        self.assertTrue(self.file_path.exists())

        with self.file_path.open("r", encoding="utf-8") as file:
            content = file.read()

        self.assertIn("Nithin", content)
        self.assertIn("Data Science", content)

    def test_import_students(self):
        with self.file_path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow(["sid", "name", "age", "course"])
            writer.writerow([1, "Nithin", 23, "Data Science"])
            writer.writerow([2, "Sunny", 24, "Machine Learning"])

        result = import_students(self.file_path)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].name, "Nithin")
        self.assertEqual(result[1].course, "Machine Learning")



