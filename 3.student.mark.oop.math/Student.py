import math, numpy as np
from StudentBasicInfo import StudentBasicInfo
import curses, time
from curses.textpad import Textbox, rectangle

class Student(StudentBasicInfo):
    __students = []

    def __init__(self, studentId=None, studentName=None, birthdate=None):
        super().__init__(studentId, studentName, birthdate)
        self.__marks = {}
        self.__marksInArray = np.array([])
        self.__average = 0
        if not self.isStudentDuplicate():
            Student.getStudents().append(self)

    def __eq__(self, other):
        return self.getStudentId() == other.getStudentId()
    
    @classmethod
    def getStudents(cls):
        return Student.__students
    
    def isStudentDuplicate(self):
        return any(self == student for student in Student.getStudents())

    def setMark(self, courseId, studentId, stdscr):
        while True:
            stdscr.clear()
            # n = int(input("Number of students: "))
            stdscr.addstr(0, 0, f"Enter mark of student {studentId} in course {courseId}: ")
            
            win = curses.newwin(2, 7, 2, 1)
            box = Textbox(win)
            rectangle(stdscr, 1, 0, 4, 9)

            stdscr.refresh()

            box.edit()
            try:
                mark = float(box.gather().replace(" ",  ""))
                self.__marks[courseId.upper()] = mark
                self.setMarksInArray()
                self.setAverageGPA()
                break
            except ValueError:
                stdscr.addstr(5, 0, "Invalid input.")
                time.sleep(1)
        # mark = math.floor(
        #     float(input("Enter mark:")) * 10
        # ) / 10

    def getMarks(self):
        return self.__marks
    
    def getMarksInArray(self):
        return self.__marksInArray
    
    def setMarksInArray(self):
        temp = []
        for key, value in self.__marks.items():
            temp.append(value)
        self.__marksInArray = np.array(temp)

    def averageGPA(self):
        return np.mean(self.__marksInArray)
    
    def setAverageGPA(self):
        self.__average = self.averageGPA()

    def getAverageGPA(self):
        return self.__average
    
    @classmethod
    def printAllStudents(cls, stdscr):
        stdscr.clear()

        student_list = Student.getStudents()

        if not student_list:
            stdscr.addstr("No students.")
            stdscr.refresh()
            stdscr.getch()
            return

        stdscr.addstr(1, 0, "Student list: ")
        stdscr.addstr(2, 2, "ID")
        stdscr.addstr(2, 16, "Name")
        stdscr.addstr(2, 42, "Birthdate")

        for s in student_list:
            stdscr.addstr(3 + student_list.index(s), 0, s.getStudentId())
            stdscr.addstr(3 + student_list.index(s), 13, s.getStudentName())
            stdscr.addstr(3 + student_list.index(s), 40, s.getBirthDate())

        stdscr.refresh()
        stdscr.getch()
    
    @classmethod
    def printAllGPA(cls, stdscr):
        stdscr.clear()

        student_list = Student.getStudents()

        if not student_list:
            stdscr.addstr("No students.")
            stdscr.refresh()
            stdscr.getch()
            return
        
        stdscr.addstr(1, 0, "GPA:")
        stdscr.addstr(3, 2, "ID")
        stdscr.addstr(3, 16, "Name")
        stdscr.addstr(3, 42, "Birthdate")
        stdscr.addstr(3, 56, "GPA")

        for s in student_list:
            stdscr.addstr(4 + student_list.index(s), 0, s.getStudentId())
            stdscr.addstr(4 + student_list.index(s), 13, s.getStudentName())
            stdscr.addstr(4 + student_list.index(s), 40, s.getBirthDate())
            stdscr.addstr(4 + student_list.index(s), 54, str(s.getAverageGPA()))

        stdscr.refresh()
        stdscr.getch()