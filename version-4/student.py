import re
from exceptions import InvalidNameError, InvalidAgeError, InvalidCourseError
from course import VALID_COURSES

class Student:
    def __init__(
            self,
            sid : None | int,
            name : str,
            age : int,
            course : str
    ):

        self.__sid = sid
        self.name = name
        self.age = age
        self.course = course

    @property
    def sid(self) -> int | None:
        return self.__sid

    @sid.setter
    def sid(self, sid : int | None):
        self.__sid = sid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name : str):
        name = name.strip().title()
        if not 3 <= len(name) <= 50:
            raise InvalidNameError(
                'Name should be in range of 3 to 50 and alphabet'
            )

        if not re.fullmatch(r'[A-Za-z]+(?: [A-Za-z]+)*', name):
            raise InvalidNameError(
                'Name should contain only alphabets and single spaces'
            )

        self.__name = name

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age : int):
        if 5 <= age < 60:
            self.__age = age
        else:
            raise InvalidAgeError('Age should be in range of 5 and 60')


    @property
    def course(self) -> str:
        return self.__course

    @course.setter
    def course(self, course : str):
        course = course.strip().title()
        if course in VALID_COURSES:
            self.__course = course
        else:
            raise InvalidCourseError('Please enter valid course name')

    def __str__(self) -> str:
        return f'Student ID : {self.__sid}\t Name : {self.__name}\t Age : {self.__age}\t Course : {self.__course}'
