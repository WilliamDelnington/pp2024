import curses, time
from curses.textpad import Textbox, rectangle

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
        # newId = input("Enter course id: ")
        # for course in Course.getAllCourses():
        #     if newId == course.getCourseId():
        #         print("Course Id already exists")
        #         return
        stdscr.clear()
        newId = None
        while True:
            stdscr.clear()
            stdscr.addstr(0, 0, "Add Course ID")
            stdscr.addstr(1, 0, "Enter course's id (Please do not space out):")

            win = curses.newwin(3, 18, 3, 1)
            box = Textbox(win)
            rectangle(stdscr, 2, 0, 4, 19)
            stdscr.addstr(8, 0, "Press Ctrl + G to confirm the input.")

            stdscr.refresh()

            box.edit()
            newId = box.gather().replace("\n", "").replace(" ", "")
            
            if (newId == "") or (any(newId == course.getCourseId() for course in Course.getAllCourses())):
                stdscr.clear()
                stdscr.addstr("Course ID already exists or can't be blanked.")
                stdscr.refresh()
                stdscr.getch()
                time.sleep(2)
            else:
                break

        stdscr.addstr(10, 0, f"The value you entered is: {newId}")
        stdscr.addstr(11, 0, "Press any key to continue...")

        self.__courseId = newId
        stdscr.getch()
    
    def getCourseId(self):
        return self.__courseId
    
    def __setCourseName(self, stdscr):
        #newName = input("Enter course name: ")
        stdscr.clear()
        stdscr.addstr(0, 0, "Add Course Name")
        stdscr.addstr(1, 0, "Enter course's name:")

        win = curses.newwin(3, 29, 3, 1)
        box = Textbox(win)
        rectangle(stdscr, 2, 0, 4, 30)
        stdscr.addstr(8, 0, "Press Ctrl + G to exit the input progress.")

        stdscr.refresh()

        box.edit()
        newName = box.gather().replace("\n", "")
        stdscr.addstr(10, 0, f"The value you entered is: {newName}")
        stdscr.addstr(11, 0, "Press any key to continue.")

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
            stdscr.addstr(0, 0, "No courses available.")
            stdscr.addstr(2, 0, "Press any key to continue.")
            stdscr.refresh()
            stdscr.getch()
            return False
        # print("Course list:")
        # print("ID----Name")
        # for c in course_list:
        #     print("{}----{} ".format(
        #         c.getCourseId(), 
        #         c.getCourseName()
        #     ))

        stdscr.addstr(1, 0, "Course list: ")
        stdscr.addstr(2, 2, "ID")
        stdscr.addstr(2, 16, "Name")

        for c in course_list:
            stdscr.addstr(3 + course_list.index(c), 0, c.getCourseId())
            stdscr.addstr(3 + course_list.index(c), 13, c.getCourseName())

        stdscr.refresh()
        stdscr.getch()

        return True

# def main(stdscr):
#     cr1 = Course()
#     cr1.setCourse(stdscr)

#     cr2 = Course()
#     cr2.setCourse(stdscr)

#     Course.printAllCourses(stdscr)

# curses.wrapper(main)