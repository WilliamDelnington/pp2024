# student_infos = []
# courses = []
import math, numpy as np
import curses
from curses.textpad import Textbox, rectangle
from Course import Course
from Student import Student
import time

def setStudents(stdscr):
    while True:
        stdscr.clear()
        # n = int(input("Number of students: "))
        stdscr.addstr(0, 0, "Enter number of students: ")
        
        win = curses.newwin(2, 7, 2, 1)
        box = Textbox(win)
        rectangle(stdscr, 1, 0, 4, 9)

        stdscr.refresh()

        box.edit()
        try:
            n = int(box.gather().replace(" ",  ""))
            for _ in range(n):
                s = Student()
                s.setStudent(stdscr)
            break
        except ValueError:
            stdscr.addstr(5, 0, "Invalid input.")
            time.sleep(1)

def setCourses(stdscr):
    while True:
        stdscr.clear()

        stdscr.addstr(0, 0, "Enter number of courses: ")

        win = curses.newwin(2, 7, 2, 1)
        box = Textbox(win)
        rectangle(stdscr, 1, 0, 4, 9)

        stdscr.refresh()

        box.edit()
        try:
            # n = int(input("Number of courses: "))
            n = int(box.gather().replace(" ",  ""))
            for _ in range(n):
                c = Course()
                c.setCourse(stdscr)
            break
        except ValueError:
            # print("Invalid input.")
            stdscr.addstr(5, 0, "Invalid input.")
            time.sleep(1)

def setSpecificMark(stdscr):
    continuing = Course.printAllCourses(stdscr)
    if not continuing:
        return
    courseId = coursePicking(stdscr)
    if not Student.getStudents():
        stdscr.clear()
        stdscr.addstr("No students.")
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
        win = curses.newwin(nlines, ncols, uly, ulx)
        box = Textbox(win)
        rectangle(stdscr, uly-1, ulx-1, uly+nlines, ulx+ncols)

        stdscr.refresh()

        box.edit()
        courseId = box.gather().replace(" ", "").replace("\n", "")
        if any(courseId.lower() == course.getCourseId().lower() for course in Course.getAllCourses()):
            return courseId
        stdscr.addstr(l + 11, 0, "Course not found.")

def printCourseMark(stdscr):
    continuing = Course.printAllCourses(stdscr)
    if not continuing:
        return
    courseId = coursePicking(stdscr)
    stdscr.clear()
    stdscr.addstr("Student marks: ")
    stdscr.addstr(2, 0, "Student ID")
    stdscr.addstr(2, 13, "Student Name")
    stdscr.addstr(2, 40, "Course ID")
    stdscr.addstr(2, 50, "Mark")
    # print("Student ID----Student Name----Course Id----Mark")
    i = 0
    students = Student.getStudents()
    while i < len(students):
        stdscr.addstr(i + 3, 0, students[i].getStudentId())
        stdscr.addstr(i + 3, 13, students[i].getStudentName())
        stdscr.addstr(i + 3, 40, courseId)
        stdscr.addstr(i + 3, 50, students[i].getMarks()[courseId.upper()])
        i += 1
    
    stdscr.addstr(i + 5, 0, "Press any key to continue...")
        

def main(stdscr):
    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Make your choice (Enter numbers only and press Ctrl + G to confirm your choice):")

        stdscr.addstr(2, 0, "1. Input students information")
        stdscr.addstr(3, 0, "2. Input courses information")
        stdscr.addstr(4, 0, "3. Input marks based on course")
        stdscr.addstr(5, 0, "4. Display students information")
        stdscr.addstr(6, 0, "5. Display courses information")
        stdscr.addstr(7, 0, "6. Display students marks based on course")
        stdscr.addstr(8, 0, "7. Display student GPA")
        stdscr.addstr(9, 0, "8. Exit")
        # m = input("Your choice (enter number only): ")
        ncols, nlines = 8, 3
        uly, ulx = 11, 2

        win = curses.newwin(nlines, ncols, uly, ulx)
        rectangle(stdscr, uly-1, ulx-1, uly + nlines, ulx + ncols)

        stdscr.refresh()

        box = Textbox(win)
        box.edit()
        m = box.gather().replace("\n", "").replace(" ", "")

        match m:
            case "1":
                setStudents(stdscr)
            case "2":
                setCourses(stdscr)
            case "3":
                setSpecificMark(stdscr)
            case "4":
                Student.printAllStudents(stdscr)
            case "5":
                Course.printAllCourses(stdscr)
            case "6":
                printCourseMark(stdscr)
            case "7":
                Student.printAllGPA(stdscr)
            case "8":
                break
            case _:
                # print("Invalid input.")
                stdscr.clear()
                stdscr.addstr("Invalid input")
                stdscr.refresh()
                stdscr.getch()

def get_input(stdscr, prompt):
    pass

curses.wrapper(main)