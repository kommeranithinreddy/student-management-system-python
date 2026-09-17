import csv
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

from student import Student

def export_students(students : list[Student], file_path : Path) -> None:
    try:
        with file_path.open('w', newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["sid", "name", "age", "course"]
            )
            writer.writeheader()

            for student in students:
                writer.writerow({
                    "sid": student.sid,
                    "name": student.name,
                    "age": student.age,
                    "course": student.course
                })
        logger.info(f"Students data successfully exported to {file_path}")

    except OSError as error:
        logger.error(f"File error while exporting students to {file_path} : {error}")
        raise


def import_students(file_path : Path) -> list[Student]:
    try:
        with file_path.open('r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            students = []
            for row in reader:
                student = Student(None, row["name"], int(row["age"]), row["course"])
                students.append(student)

            logger.info(
                f"Students data imported successfully from {file_path}"
            )
            return students

    except (OSError, UnicodeDecodeError, ValueError, KeyError) as error:
        logger.error(
            f"Error importing students from {file_path}: {error}"
        )
        raise