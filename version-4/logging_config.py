import logging

logging.basicConfig(
    level = logging.INFO,
    filename = "student_management.log",
    format = "%(asctime)s | %(levelname)s | %(message)s"
)

logging.info("Logging configuration loaded")