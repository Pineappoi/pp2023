class Student:
    def __init__(self, name, DOB, student_ID):
        self.name = name
        self.DOB = DOB
        self.marks = {}
        self.courses = []
        self.student_ID = student_ID

    def enroll(self, course_ID):
        self.courses.append(course_ID)
        print("Success!")

    def get_marks(self, course_ID):
        return self.marks.get(course_ID)

    def input_mark(self, course_ID, mark):
        self.marks[course_ID] = mark

class Course:
    def __init__(self, name, course_ID):
        self.name = name
        self.marks = {}
        self.course_ID = course_ID

ALL_STUDENTS = {}
ALL_COURSES = {}

def STUDENT_input():
    STUDENT_num = int(input("Enter the number of students: "))
    for i in range (STUDENT_num):
        name = input("Enter the student's name: ")
        DOB = input("Enter the student's date of birth: ")
        ID = (input("Enter the student's ID: "))
        student = Student(name, DOB, ID)
        ALL_STUDENTS[ID] = student

def COURSE_input():
    COURSE_num = int(input("Enter the number of courses: "))
    for i in range (COURSE_num):
        name = input("Enter the name of the course: ")
        ID = (input("Enter the ID of the course: "))
        course = Course(name, ID)
        ALL_COURSES[ID] = course

def COURSE_select():
    while True:
        student_ID = (input("Enter your student ID: "))
        course_ID = (input("Enter the ID of the course you want to enroll in: "))
        if course_ID in ALL_COURSES and student_ID in ALL_STUDENTS:
            ALL_STUDENTS[student_ID].enroll(course_ID)
            break
        else:
            print("Please input a valid course/student ID.")

def MARK_input():
    while True:
        course_ID = (input("Enter the ID of the course: "))
        student_ID = (input("Enter the ID of the student: "))
        if course_ID in ALL_COURSES and student_ID in ALL_STUDENTS:
            MARK = int(input("Enter mark: "))
            ALL_STUDENTS[student_ID].input_mark(course_ID, MARK)
            ALL_COURSES[course_ID].marks[student_ID] = MARK
            break
        else: 
            print("Please input a valid course/student ID.")
                
def STUDENT_list():
    for student_ID in ALL_STUDENTS:
        print(ALL_STUDENTS)

def COURSE_list():
    for course_ID in ALL_COURSES:
        print(ALL_COURSES)

def MARK_show():
    while True:
        student_ID = (input("Enter the ID of the student: "))
        course_ID = (input("Enter the ID of the course: "))
        if course_ID in ALL_COURSES and student_ID in ALL_STUDENTS:
            mark = ALL_STUDENTS[student_ID].get_marks(course_ID)
            print(mark)
            break
        else: 
            print("Please input a valid course/student ID.")


while True:
    print("Choose a function to use:")
    print("1. STUDENT_input()")
    print("2. COURSE_input()")
    print("3. COURSE_select()")
    print("4. MARK_input()")
    print("5. MARK_show()")
    print("6. STUDENT_list()")
    print("7. COURSE_list()")
    print("8. Exit")
    user_input = int(input())
    if user_input == 1:
        STUDENT_input()
    elif user_input == 2:
        COURSE_input()
    elif user_input == 3:
        COURSE_select()
    elif user_input == 4:
        MARK_input()
    elif user_input == 5:
        MARK_show()
    elif user_input == 6:
        STUDENT_list()
    elif user_input == 7:
        COURSE_list()
    elif user_input == 8:
        break