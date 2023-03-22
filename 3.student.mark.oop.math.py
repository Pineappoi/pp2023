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
        for student_ID in self.ALL_STUDENTS:
            print(self.ALL_STUDENTS[student_ID].__dict__)

    def COURSE_list(self):
        for course_ID in self.ALL_COURSES:
            print(self.ALL_COURSES[course_ID].__dict__)

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
                print(MANAGEMENT.ALL_STUDENTS[student_ID].name + ": " + str(MANAGEMENT.get_GPA(student_ID)))

MANAGEMENT = MANAGEMENT()

#Test
# Create 3 students
student1 = STUDENT('John', '01/01/2001', '1')
student2 = STUDENT('Tom', '02/02/2002', '2')
student3 = STUDENT('Alice', '03/03/2003', '3')

# Add the students to the MANAGEMENT class
MANAGEMENT.ALL_STUDENTS['1'] = student1
MANAGEMENT.ALL_STUDENTS['2'] = student2
MANAGEMENT.ALL_STUDENTS['3'] = student3

# Create 3 courses 
course1 = COURSE('Math', 'M001', 3)
course2 = COURSE('English', 'E001', 4)
course3 = COURSE('Science', 'S001', 5)

# Add the courses to the MANAGEMENT class
MANAGEMENT.ALL_COURSES['M001'] = course1
MANAGEMENT.ALL_COURSES['E001'] = course2
MANAGEMENT.ALL_COURSES['S001'] = course3

# Add marks to the students and courses
MANAGEMENT.ALL_STUDENTS['1'].input_mark('M001', 70)
MANAGEMENT.ALL_STUDENTS['1'].input_mark('E001', 80)
MANAGEMENT.ALL_STUDENTS['1'].input_mark('S001', 90)
MANAGEMENT.ALL_STUDENTS['2'].input_mark('M001', 80)
MANAGEMENT.ALL_STUDENTS['2'].input_mark('E001', 90)
MANAGEMENT.ALL_STUDENTS['2'].input_mark('S001', 100)
MANAGEMENT.ALL_STUDENTS['3'].input_mark('M001', 90)
MANAGEMENT.ALL_STUDENTS['3'].input_mark('E001', 100)
MANAGEMENT.ALL_STUDENTS['3'].input_mark('S001', 110)

MANAGEMENT.ALL_COURSES['M001'].input_mark('1', 70)
MANAGEMENT.ALL_COURSES['M001'].input_mark('2', 80)
MANAGEMENT.ALL_COURSES['M001'].input_mark('3', 90)
MANAGEMENT.ALL_COURSES['E001'].input_mark('1', 80)
MANAGEMENT.ALL_COURSES['E001'].input_mark('2', 90)
MANAGEMENT.ALL_COURSES['E001'].input_mark('3', 100)
MANAGEMENT.ALL_COURSES['S001'].input_mark('1', 90)
MANAGEMENT.ALL_COURSES['S001'].input_mark('2', 100)
MANAGEMENT.ALL_COURSES['S001'].input_mark('3', 110)

# Get the GPAs of the students
MANAGEMENT.get_GPA('1')
MANAGEMENT.get_GPA('2')
MANAGEMENT.get_GPA('3')


while True:
    print("Choose a function to use:")
    print("1. STUDENT_input()")
    print("2. COURSE_input()")
    print("3. COURSE_enroll()")
    print("4. MARK_input()")
    print("5. MARK_show()")
    print("6. STUDENT_list()")
    print("7. COURSE_list()")
    print("8. Get GPA of a student")
    print("9. Sort students by GPA")
    print("10. Exit")
    user_input = int(input())
    if user_input == 1:
        MANAGEMENT.STUDENT_input()
    elif user_input == 2:
        MANAGEMENT.COURSE_input()
    elif user_input == 3:
        MANAGEMENT.COURSE_enroll()
    elif user_input == 4:
        MANAGEMENT.MARK_input()
    elif user_input == 5:
        MANAGEMENT.MARK_show()
    elif user_input == 6:
        MANAGEMENT.STUDENT_list()
    elif user_input == 7:
        MANAGEMENT.COURSE_list()
    elif user_input == 8:
        student_ID = (input("Enter the ID of the student: "))
        GPA = MANAGEMENT.get_GPA(student_ID)
        print("Student "+MANAGEMENT.ALL_STUDENTS[student_ID].name+"'s GPA is "+str(GPA))
    elif user_input == 9:
        MANAGEMENT.sort_by_GPA()
    elif user_input == 10:
        break