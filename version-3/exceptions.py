class StudentError(Exception):
    pass

class StudentNotFoundError(StudentError):
    pass

class InvalidAgeError(StudentError):
    pass

class InvalidNameError(StudentError):
    pass

class InvalidCourseError(StudentError):
    pass
