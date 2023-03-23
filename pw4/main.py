from input import STUDENT, COURSE, MANAGEMENT

MANAGEMENT = MANAGEMENT()

#Test
# Create 3 students
student1 = STUDENT('Hieu', '01/01/2001', '1')
student2 = STUDENT('Tien', '02/02/2002', '2')
student3 = STUDENT('Hai', '03/03/2003', '3')

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
MANAGEMENT.ALL_STUDENTS['1'].input_mark('M001', 14)
MANAGEMENT.ALL_STUDENTS['1'].input_mark('E001', 12)
MANAGEMENT.ALL_STUDENTS['1'].input_mark('S001', 11)
MANAGEMENT.ALL_STUDENTS['2'].input_mark('M001', 15)
MANAGEMENT.ALL_STUDENTS['2'].input_mark('E001', 8)
MANAGEMENT.ALL_STUDENTS['2'].input_mark('S001', 6)
MANAGEMENT.ALL_STUDENTS['3'].input_mark('M001', 10)
MANAGEMENT.ALL_STUDENTS['3'].input_mark('E001', 11)
MANAGEMENT.ALL_STUDENTS['3'].input_mark('S001', 13)

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
    print("1. Input student information")
    print("2. Input course information")
    print("3. Enroll a student to a course")
    print("4. Input mark of a student for a course")
    print("5. Show mark of a student for a course")
    print("6. List all students")
    print("7. List all courses")
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