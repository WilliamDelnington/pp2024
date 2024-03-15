import curses
from domains.Course import Course
from domains.Student import Student
import time
from output import print_message
from input import cursesInput

def setStudents(stdscr):
    while True:
        stdscr.clear()

        stdscr.addstr(0, 0, "Enter number of students: ")
        
        # win = curses.newwin(2, 7, 2, 1)
        # box = Textbox(win)
        # rectangle(stdscr, 1, 0, 4, 9)
        # stdscr.refresh()
        # box.edit()

        val = cursesInput(stdscr, 7, 2, 2, 1)
        try:
            n = int(val.replace("\n",  "").replace(" ", ""))
            for _ in range(n):
                s = Student()
                s.setStudent(stdscr)
            break
        except ValueError:
            print_message(stdscr, 6, 0, "Invalid input.")
            time.sleep(1)

def setCourses(stdscr):
    while True:
        stdscr.clear()

        stdscr.addstr(0, 0, "Enter number of courses: ")

        # win = curses.newwin(2, 7, 2, 1)
        # box = Textbox(win)
        # rectangle(stdscr, 1, 0, 4, 9)
        # stdscr.refresh()
        # box.edit()

        val = cursesInput(stdscr, 7, 2, 2, 1)
        try:
            # n = int(input("Number of courses: "))
            n = int(val.replace(" ",  "").replace("\n", ""))
            for _ in range(n):
                c = Course()
                c.setCourse(stdscr)
            break
        except ValueError:
            # print("Invalid input.")
            print_message(stdscr, 5, 0, "Invalid input.")
            time.sleep(1)

def setSpecificMark(stdscr):
    continuing = Course.printAllCourses(stdscr)
    if not continuing:
        return
    courseId = coursePicking(stdscr)
    if not Student.getStudents():
        stdscr.clear()
        print_message(stdscr, 0, 0, "No students.")
        stdscr.refresh()
        stdscr.getch()
    for s in Student.getStudents():
        s.setMark(courseId, s.getStudentId(), stdscr)

def coursePicking(stdscr):
    # courseId = input("Write course id: ")
    l = len(Course.getAllCourses())
    while True:
        stdscr.addstr(l + 3, 0, "Write course id:")

        ncols, nlines = 7, 3
        uly, ulx = l + 5, 2
        # win = curses.newwin(nlines, ncols, uly, ulx)
        # box = Textbox(win)
        # rectangle(stdscr, uly-1, ulx-1, uly+nlines, ulx+ncols)
        # stdscr.refresh()
        # box.edit()

        courseId = cursesInput(stdscr, ncols, nlines, uly, ulx).replace(" ", "").replace("\n", "")
        if any(courseId.lower() == course.getCourseId().lower() for course in Course.getAllCourses()):
            return courseId
        stdscr.addstr(l + 11, 0, "Course not found.")

def printCourseMark(stdscr):
    continuing = Course.printAllCourses(stdscr)
    if not continuing:
        return
    courseId = coursePicking(stdscr)
    stdscr.clear()
    print_message(stdscr, 0, 0, "Student marks: ")
    print_message(stdscr, 2, 0, "Student ID")
    print_message(stdscr, 2, 13, "Student Name")
    print_message(stdscr, 2, 40, "Course ID")
    print_message(stdscr, 2, 50, "Mark")
    # print("Student ID----Student Name----Course Id----Mark")
    i = 0
    students = Student.getStudents()
    while i < len(students):
        print_message(stdscr, i + 3, 0, students[i].getStudentId())
        print_message(stdscr, i + 3, 13, students[i].getStudentName())
        print_message(stdscr, i + 3, 40, courseId)
        print_message(stdscr, i + 3, 50, students[i].getMarks()[courseId.upper()])
        i += 1
    
    stdscr.addstr(i + 5, 0, "Press any key to continue...")