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

    def COURSE_enroll(self):
        while True:
            student_ID = (input("Enter your student ID: "))
            course_ID = (input("Enter the ID of the course you want to enroll in: "))
            if course_ID in self.ALL_COURSES and student_ID in self.ALL_STUDENTS:
                self.ALL_STUDENTS[student_ID].enroll(course_ID)
                break
            else:
                print("Please input a valid course/student ID.")

    def MARK_input(self):
        while True:
            course_ID = (input("Enter the ID of the course: "))
            student_ID = (input("Enter the ID of the student: "))
            if course_ID in self.ALL_COURSES and student_ID in self.ALL_STUDENTS:
                MARK = int(input("Enter mark: "))
                self.ALL_STUDENTS[student_ID].input_mark(course_ID, MARK)
                self.ALL_COURSES[course_ID].input_mark(student_ID, MARK)
                break
            else: 
                print("Please input a valid course/student ID.")

    def STUDENT_list(self):
        for i, student_ID in enumerate(self.ALL_STUDENTS):
            print(str(i+1)+". "+self.ALL_STUDENTS[student_ID].name)
            print("   "+self.ALL_STUDENTS[student_ID].DOB)
            print("   ID:"+self.ALL_STUDENTS[student_ID].student_ID)
            print("   GPA: "+str(self.ALL_STUDENTS[student_ID].GPA))
            print("   Courses: "+str(self.ALL_STUDENTS[student_ID].courses))

    def COURSE_list(self):
        for i, course_ID in enumerate(self.ALL_COURSES):
            print(str(i+1)+". "+self.ALL_COURSES[course_ID].name)
            print("   "+self.ALL_COURSES[course_ID].course_ID)
            print("   "+str(self.ALL_COURSES[course_ID].credits)+" credits")
            print("   Marks: "+str(self.ALL_COURSES[course_ID].marks))

    def MARK_show(self):
        while True:
            student_ID = (input("Enter the ID of the student: "))
            course_ID = (input("Enter the ID of the course: "))
            if course_ID in self.ALL_COURSES and student_ID in self.ALL_STUDENTS:
                mark = self.ALL_STUDENTS[student_ID].get_marks(course_ID)
                print(mark)
                break
            else: 
                print("Please input a valid course/student ID.")

    def get_GPA(self, student_ID):
        total_credit = 0
        total_score = 0
        for course in self.ALL_STUDENTS[student_ID].marks:
            total_score += self.ALL_COURSES[course].credits * self.ALL_STUDENTS[student_ID].marks[course]
            total_credit += self.ALL_COURSES[course].credits
        self.ALL_STUDENTS[student_ID].GPA = round(np.average(total_score / total_credit), 2)
        return self.ALL_STUDENTS[student_ID].GPA

    def sort_by_GPA(self):
        student_GPA = []
        for student_ID in MANAGEMENT.ALL_STUDENTS:
            student_GPA.append(MANAGEMENT.get_GPA(student_ID))
        sorted_GPA = sorted(student_GPA, reverse = True)
        for student_ID in MANAGEMENT.ALL_STUDENTS:
            if MANAGEMENT.get_GPA(student_ID) in sorted_GPA:
                sorted_GPA.remove(MANAGEMENT.get_GPA(student_ID))
                print("[+] " + MANAGEMENT.ALL_STUDENTS[student_ID].name + ": " + str(MANAGEMENT.get_GPA(student_ID)))
