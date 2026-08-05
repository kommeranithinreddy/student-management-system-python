import re
from exceptions import InvalidNameError, InvalidAgeError, InvalidCourseError

class Student:
    def __init__(self, sid, name, age, course):
        self.__sid = sid
        self.set_name(name)
        self.set_age(age)
        self.set_course(course)

    def set_name(self, name):
        if re.fullmatch(r'[a-zA-Z ]{3,10}', name):
            self.__name = name
        else:
            raise InvalidNameError('Name should be in range of 3 to 10 and alphabet')
    def set_age(self, age):
        if 5<=age<60:
            self.__age = age
        else:
            raise InvalidAgeError('Age should be in range of 5 and 60')
    def set_course(self, course):
        if re.fullmatch(r'[a-zA-Z]{3,10}', course):
            self.__course = course
        else:
            raise InvalidCourseError('Course name should consists only Alphabets in range of 3 to 10')

    def __str__(self):
        return f'Student ID : {self.__sid}\t Name : {self.__name}\t Age : {self.__age}\t Course : {self.__course}'

    def update(self, new_name = None, new_age=None, new_course = None):
        if new_name is not None:
            self.set_name(new_name)
        if new_age is not None:
            self.set_age(new_age)
        if new_course is not None:
            self.set_course(new_course)

    def get_sid(self):
        return self.__sid

    #for storing data in storage
    def to_dict(self):
        return {'sid' : self.__sid, 'name' : self.__name, 'age' : self.__age, 'course' : self.__course}

    #data loading from storage and creating objects
    @classmethod
    def from_dict(cls, data):
        sid, name, age, course = data['sid'], data['name'], data['age'], data['course']
        return cls(sid, name, age, course)