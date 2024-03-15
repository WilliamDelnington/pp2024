import time
from input import cursesInput
from output import print_message

class Course:
    # list of courses
    __courses = []

    #defining attributes
    def __init__(self, courseId=None, courseName=None):
        self.__courseId = courseId
        self.__courseName = courseName
        if not self.isCourseDuplicate():
            Course.getAllCourses().append(self)

    def __setCourseId(self, stdscr):
        stdscr.clear()
        newId = None
        while True:
            stdscr.clear()
            stdscr.addstr(0, 0, "Add Course ID")
            stdscr.addstr(1, 0, "Enter course's id (Please do not space out):")

            input_val = cursesInput(stdscr, 18, 3, 3, 1)
            newId = input_val.replace("\n", "").replace(" ", "")
            
            if (newId == "") or (any(newId == course.getCourseId() for course in Course.getAllCourses())):
                stdscr.clear()
                print_message(stdscr, 0, 0, "Id is already existed or can't be blanked.")
                stdscr.refresh()
                stdscr.getch()
                time.sleep(2)
            else:
                break

        print_message(stdscr, 10, 0, f"The value you entered is: {newId}")
        print_message(stdscr, 11, 0, "Press any key to continue...")

        self.__courseId = newId
        stdscr.getch()
    
    def getCourseId(self):
        return self.__courseId
    
    def __setCourseName(self, stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, "Add Course Name")
        stdscr.addstr(1, 0, "Enter course's name:")

        newName = cursesInput(stdscr, 29, 3, 3, 1).replace("\n", "")
        print_message(stdscr, 10, 0, f"The value you entered is: {newName}")
        print_message(stdscr, 11, 0, "Press any key to continue.")

        self.__courseName = newName
        stdscr.getch()

    def getCourseName(self):
        return self.__courseName
    
    def isCourseDuplicate(self):
        for c in Course.getAllCourses():
            if (self == c):
                return True
        return False
    
    def setCourse(self, stdscr):
        self.__setCourseId(stdscr)
        self.__setCourseName(stdscr)
    
    @classmethod
    def getAllCourses(course):
        return course.__courses
    
    def __eq__(self, other):
        return (self.getCourseId() == other.getCourseId())
    
    @classmethod
    def printAllCourses(cls, stdscr):
        stdscr.clear()

        course_list = Course.getAllCourses()

        if not course_list:
            print_message(stdscr, 0, 0, "No courses available.")
            print_message(stdscr, 2, 0, "Press any key to continue.")
            stdscr.refresh()
            stdscr.getch()
            return False

        print_message(stdscr, 1, 0, "Course list: ")
        print_message(stdscr, 2, 2, "ID")
        print_message(stdscr, 2, 16, "Name")

        for c in course_list:
            print_message(stdscr, 3 + course_list.index(c), 0, c.getCourseId())
            print_message(stdscr, 3 + course_list.index(c), 13, c.getCourseName())

        stdscr.refresh()
        stdscr.getch()

        return True