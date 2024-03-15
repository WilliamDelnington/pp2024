# student_infos = []
# courses = []
import curses
from domains.Course import Course
from domains.Student import Student
from output import print_message
from input import cursesInput

from domains.Fucnctions import setStudents, setCourses, setSpecificMark, printCourseMark
        
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

        # win = curses.newwin(nlines, ncols, uly, ulx)
        # rectangle(stdscr, uly-1, ulx-1, uly + nlines, ulx + ncols)

        # stdscr.refresh()

        # box = Textbox(win)
        # box.edit()
        # m = box.gather().replace("\n", "").replace(" ", "")
        m = cursesInput(stdscr, ncols, nlines, uly, ulx).replace("\n", "").replace(" ", "")

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
                print_message(stdscr, 0, 0, "Invalid input.")
                stdscr.refresh()
                stdscr.getch()

curses.wrapper(main)