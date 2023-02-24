ALL_STUDENTS = {}
ALL_COURSES = {}


def STUDENT_input():
    STUDENT_num = int(input("Enter the number of students: "))
    for i in range (STUDENT_num):
        STUDENT = {}
        STUDENT["name"] = input("Enter the student's name: ")
        STUDENT["DOB"] = input("Enter the student's date of birth: ")
        STUDENT["marks"] = {}
        STUDENT["courses"] = []
        ID = int(input("Enter the student's ID: "))
        STUDENT["student_ID"] = ID
        ALL_STUDENTS[ID] = STUDENT

def COURSE_input():
    COURSE_num = int(input("Enter the number of courses: "))
    for i in range (COURSE_num):
        COURSE = {}
        COURSE["name"] = input("Enter the name of the course: ")
        COURSE["marks"] = {}
        ID = int(input("Enter the ID of the course: "))
        COURSE["course_ID"] = ID
        ALL_COURSES[ID] = COURSE

def COURSE_select():
    while True:
        student_ID = int(input("Enter your student ID: "))
        course_ID = int(input("Enter the ID of the course you want to enroll in: "))
        if course_ID in ALL_COURSES and student_ID in ALL_STUDENTS:
            ALL_STUDENTS[student_ID]["courses"] = course_ID
            print("SUCESS!")
            break
        else:
            print("Please input a valid course/student ID.")

def MARK_input():
    while True:
        course_ID = int(input("Enter the ID of the course: "))
        student_ID = int(input("Enter the ID of the student: "))
        if course_ID in ALL_COURSES and student_ID in ALL_STUDENTS:
            MARK = int(input("Enter mark: "))
            ALL_STUDENTS[student_ID]["marks"][course_ID] = MARK
            ALL_COURSES[course_ID]["marks"][student_ID] = MARK
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
        student_ID = int(input("Enter the ID of the student: "))
        course_ID = int(input("Enter the ID of the course: "))
        if course_ID in ALL_COURSES and student_ID in ALL_STUDENTS:
            mark = ALL_STUDENTS[student_ID]["marks"].get(course_ID)
            print(mark)
            break
        else: 
            print("Please input a valid course/student ID.")


STUDENT_input()
COURSE_input()
COURSE_select()
MARK_input()
MARK_show()
STUDENT_list()
COURSE_list()