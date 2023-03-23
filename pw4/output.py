import math
import numpy as np

class STUDENT:
    def __init__(self, name, DOB, student_ID):
        self.name = name
        self.DOB = DOB
        self.marks = {}
        self.courses = []
        self.student_ID = student_ID
        self.GPA = 0

    def enroll(self, course_ID):
        self.courses.append(course_ID)
        print("Success!")

    def get_marks(self, course_ID):
        return self.marks.get(course_ID)

    def input_mark(self, course_ID, mark):
        self.marks[course_ID] = mark

class COURSE:
    def __init__(self, name, course_ID, credits):
        self.name = name
        self.marks = {}
        self.credits = credits
        self.course_ID = course_ID

    def input_mark(self, student_ID, mark):
        self.marks[student_ID] = mark

class MANAGEMENT:
    def __init__(self):
        self.ALL_STUDENTS = {}
        self.ALL_COURSES = {}

    def STUDENT_input(self):
        STUDENT_num = int(input("Enter the number of students: "))
        for i in range (STUDENT_num):
            name = input("Enter the student's name: ")
            DOB = input("Enter the student's date of birth: ")
            ID = (input("Enter the student's ID: "))
            student = STUDENT(name, DOB, ID)
            self.ALL_STUDENTS[ID] = student

    def COURSE_input(self):
        COURSE_num = int(input("Enter the number of courses: "))
        for i in range (COURSE_num):
            name = input("Enter the name of the course: ")
            ID = (input("Enter the ID of the course: "))
            credits = int(input("Enter the number of credits: "))
            course = COURSE(name, ID, credits)
            self.ALL_COURSES[ID] = course