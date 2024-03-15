import math, numpy as np
from domains.StudentBasicInfo import StudentBasicInfo
import time
from input import cursesInput
from output import print_message

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

            stdscr.addstr(0, 0, f"Enter mark of student {studentId} in course {courseId}: ")

            val = cursesInput(stdscr, 7, 2, 2, 1)
            try:
                mark = float(val.replace(" ",  ""))
                self.__marks[courseId.upper()] = mark
                self.setMarksInArray()
                self.setAverageGPA()
                break
            except ValueError:
                print_message(stdscr, 5, 0, "Invalid input.")
                time.sleep(1)

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
            print_message(stdscr, 0, 0, "No students.")
            stdscr.refresh()
            stdscr.getch()
            return

        print_message(stdscr, 1, 0, "Student list: ")
        print_message(stdscr, 2, 2, "ID")
        print_message(stdscr, 2, 16, "Name")
        print_message(stdscr, 2, 42, "Birthdate")

        for s in student_list:
            print_message(stdscr, 3 + student_list.index(s), 0, s.getStudentId())
            print_message(stdscr, 3 + student_list.index(s), 13, s.getStudentName())
            print_message(stdscr, 3 + student_list.index(s), 40, s.getBirthDate())

        stdscr.refresh()
        stdscr.getch()
    
    @classmethod
    def printAllGPA(cls, stdscr):
        stdscr.clear()

        student_list = Student.getStudents()

        if not student_list:
            print_message(stdscr, 0, 0, "No students.")
            stdscr.refresh()
            stdscr.getch()
            return
        
        print_message(stdscr, 1, 0, "GPA:")
        print_message(stdscr, 3, 2, "ID")
        print_message(stdscr, 3, 16, "Name")
        print_message(stdscr, 3, 42, "Birthdate")
        print_message(stdscr, 3, 56, "GPA")

        for s in student_list:
            print_message(stdscr, 4 + student_list.index(s), 0, s.getStudentId())
            print_message(stdscr, 4 + student_list.index(s), 13, s.getStudentName())
            print_message(stdscr, 4 + student_list.index(s), 40, s.getBirthDate())
            print_message(stdscr, 4 + student_list.index(s), 54, str(s.getAverageGPA()))

        stdscr.refresh()
        stdscr.getch()